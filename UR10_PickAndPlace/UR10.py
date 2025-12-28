

from robodk import robolink, robomath
import time
import math

RDK = robolink.Robolink()
robot = RDK.Item('UR10', robolink.ITEM_TYPE_ROBOT)
gripper = RDK.Item('GripperR2', robolink.ITEM_TYPE_TOOL)

# Referencias
t_prepick_espuma  = RDK.Item('prepickEspuma')
t_pick_espuma     = RDK.Item('pickEspuma')
t_paso_1          = RDK.Item('puntoPaso1')
t_preplace_espuma = RDK.Item('prePlaceEspuma')
t_place_espuma    = RDK.Item('placeEspuma')

t_prepick_bot     = RDK.Item('prepickBotellas')
t_pick_bot        = RDK.Item('pickBotellas')
t_paso_2          = RDK.Item('puntoPaso2')
t_preplace_bot    = RDK.Item('prePlaceBotella')
t_place_bot       = RDK.Item('placeBotellas')
t_home            = RDK.Item('posDefault')

# Configuración
ALTURA_ESPUMA = 10.0
contador_espumas = 1
objects = [] # Array que almacena todos los objetos de dentro la caja

# Función auxiliar para mover en Z relativo
def mover_offset_z(target_item, z_offset):
    pose_base = target_item.Pose()
    robot.MoveL(pose_base * robomath.transl(0, 0, z_offset))

# Función para regenerar espumas desde Templates
def regenerar_espuma(numero):
    nombre_objetivo = f"E{numero}"
    nombre_template = f"Template_E{numero}"
    
    # Si ya existe, la usamos
    item_existente = RDK.Item(nombre_objetivo, robolink.ITEM_TYPE_OBJECT)
    if item_existente.Valid():
        return item_existente 
    
    # Si no, copiamos del template
    template = RDK.Item(nombre_template, robolink.ITEM_TYPE_OBJECT)
    if template.Valid():
        template.Copy()
        nueva = RDK.Paste()
        nueva.setName(nombre_objetivo)
        nueva.setVisible(True)
        nueva.setPose(template.Pose())
        nueva.setParent(template.Parent())
        return nueva
    return None

# Pick and Place de 16 botellas (primer formato)
def pickAndPlace16(contador_espumas):
    NUM_CICLO = 4
    for i in range(1, NUM_CICLO):
        # Si no es la segunda iteración, se hará el pick and place de las espumas
        if i != 2:
            # FASE A: ESPUMA
            
            # Regenerar espuma
            item_espuma = regenerar_espuma(contador_espumas)
            
            # Cálculo de alturas segun el caso
            z_pick = (NUM_CICLO - contador_espumas) * ALTURA_ESPUMA
            match i:
                case 1:
                    z_place = (contador_espumas - 1) * ALTURA_ESPUMA
                case 3:
                    z_place = (contador_espumas - 1) * ALTURA_ESPUMA - 143
            # Fin del match
            
            # Movimientos a zonas prepick y pick
            robot.MoveJ(t_prepick_espuma)
            mover_offset_z(t_pick_espuma, z_pick)
            
            # Agarrar espuma
            if item_espuma and item_espuma.Valid():
                item_espuma.setParentStatic(gripper)
            
            # Volver a zona prepick y luego a paso 1
            robot.MoveL(t_prepick_espuma)
            robot.MoveJ(t_paso_1)
            
            # Movimientos a zonas preplace y place
            robot.MoveJ(t_preplace_espuma)
            mover_offset_z(t_place_espuma, z_place)
            # Metemos el objeto en la lista
            objects.append(item_espuma)
            
            # Soltar espuma
            if item_espuma and item_espuma.Valid():
                item_espuma.setParentStatic(RDK.Item('Station'))
                # item_espuma.Delete() # Borramos la copia
                
            # Volver a zona preplace
            robot.MoveL(t_preplace_espuma)
            
            # CONTADOR
            contador_espumas += 1
            if contador_espumas <= NUM_CICLO:
                robot.MoveJ(t_home)
            RDK.ShowMessage(f"Contador espumas: {contador_espumas}", False)
        else:
            # Por el contrario, si es la segunda iteración se hará el pick and place de las botellas
            # FASE B: CINTA (Esperar Semáforo)
            print("Robot: Esperando pieza en cinta...")
            
            while RDK.getParam('IO_PiezaLista') != 1:
                time.sleep(0.05)
            
            # Leer nombre de la pieza
            nombre_pieza = RDK.getParam('IO_NombrePieza')
            item_botella = RDK.Item(nombre_pieza, robolink.ITEM_TYPE_OBJECT)
            print(f"Robot: Recogiendo {nombre_pieza}")
            
            # Recogida
            robot.MoveJ(t_prepick_bot)
            robot.MoveL(t_pick_bot)  # Usamos el target de referencia en vez del de la posición de la botella para asegurar que vaya a la posición
            
            # Verificar si la pieza existe antes de mover
            if item_botella.Valid():
                item_botella.setParentStatic(gripper) # Esto avisa a la cinta
            else:
                robot.MoveL(t_pick_bot) # Fallback si algo raro pasa

            robot.MoveL(t_prepick_bot)
            
            # Entrega
            robot.MoveJ(t_paso_2)
            robot.MoveJ(t_preplace_bot)
            robot.MoveL(t_place_bot)
            
            # Metemos el objeto en la lista
            objects.append(item_botella)
            
            if item_botella.Valid():
                item_botella.setParentStatic(RDK.Item('Station'))
                # item_botella.Delete()
                
            robot.MoveL(t_preplace_bot)
            
        # CONTADORES
        if contador_espumas <= NUM_CICLO:
            robot.MoveJ(t_home)
        RDK.ShowMessage(f"Contador espumas: {contador_espumas}", False)

# Pick and Place de 32 botellas (segundo formato)
def pickAndPlace32(contador_espumas):
    NUM_CICLO = 6
    for i in range(1, NUM_CICLO):
        # Si no es la segunda iteración, se hará el pick and place de las espumas
        if i != 2 and i != 4:
            # FASE A: ESPUMA
            item_espuma = regenerar_espuma(contador_espumas)
            z_pick = (NUM_CICLO - contador_espumas) * ALTURA_ESPUMA
            match i:
                case 3:
                    z_place = (contador_espumas - 1) * ALTURA_ESPUMA
                    z_place = z_place - 125
                
                case 5:
                    z_place = (contador_espumas - 1) * ALTURA_ESPUMA
                    z_place = z_place - (125 * 2) - ALTURA_ESPUMA
                    
                case _:
                    z_place = (contador_espumas - 1) * ALTURA_ESPUMA

            # Fin del match  
            robot.MoveJ(t_prepick_espuma)
            mover_offset_z(t_pick_espuma, z_pick)
            
            if item_espuma and item_espuma.Valid():
                item_espuma.setParentStatic(gripper)
            
            robot.MoveL(t_prepick_espuma)
            robot.MoveJ(t_paso_1)
            
            robot.MoveJ(t_preplace_espuma)
            mover_offset_z(t_place_espuma, z_place)
            # Metemos el objeto en la lista
            objects.append(item_espuma)
            
            if item_espuma and item_espuma.Valid():
                item_espuma.setParentStatic(RDK.Item('Station'))
                # item_espuma.Delete() # Borramos la copia
            
            robot.MoveL(t_preplace_espuma)
            contador_espumas += 1
            if contador_espumas <= NUM_CICLO:
                robot.MoveJ(t_home)
            RDK.ShowMessage(f"Contador espumas: {contador_espumas}", False)
        else:
            # FASE B: CINTA (Esperar Semáforo)
            print("Robot: Esperando pieza en cinta...")
            
            while RDK.getParam('IO_PiezaLista') != 1:
                time.sleep(0.05)
            
            # Leer nombre de la pieza
            nombre_pieza = RDK.getParam('IO_NombrePieza')
            item_botella = RDK.Item(nombre_pieza, robolink.ITEM_TYPE_OBJECT)
            print(f"Robot: Recogiendo {nombre_pieza}")
            
            # Recogida
            robot.MoveJ(t_prepick_bot)
            robot.MoveL(t_pick_bot)  # Usamos el target de referencia en vez del de la posición de la botella para asegurar que vaya a la posición
            
            # Verificar si la pieza existe antes de mover
            if item_botella.Valid():
                item_botella.setParentStatic(gripper) # Esto avisa a la cinta
            else:
                robot.MoveL(t_pick_bot) # Fallback si algo raro pasa

            robot.MoveL(t_prepick_bot)
            
            # Si es la segunda iteración, se pondrá en la base de la caja
            
            # Entrega
            robot.MoveJ(t_paso_2)
            robot.MoveJ(t_preplace_bot)
            
            # Dependiendo de la iteración, se colocará en una u otra altura
            if i == 2:
                robot.MoveL(t_place_bot)
            else:
                mover_offset_z(t_place_bot, -135)  # Colocación botella superior
            
            # Metemos el objeto en la lista
            objects.append(item_botella)
            
            if item_botella.Valid():
                item_botella.setParentStatic(RDK.Item('Station'))
                # item_botella.Delete()
            robot.MoveL(t_preplace_bot)
        # fin del if
        
        # CONTADORES
        if contador_espumas <= NUM_CICLO:
            robot.MoveJ(t_home)
        RDK.ShowMessage(f"Contador espumas: {contador_espumas}", False)
        
# =================================================================================
# INICIO DEL PROGRAMA PRINCIPAL
#==================================================================================

print("Robot: Iniciando y limpiando señales...")
RDK.setParam('IO_PiezaLista', 0) 
robot.MoveJ(t_home)

while True:
    sensor = RDK.getParam('sensor3')
    # Implementación del semáforo del sensor de la cinta de las botellas
    # while sensor != 1:
    #   time.sleep(0.1)
    
    print(f"--- Iteración {contador_espumas} ---")
    pickAndPlace32(contador_espumas)
    for i in range(len(objects)):
        objects[i].Delete()
    objects.clear()
    contador_espumas = 1
    time.sleep(5)
    pickAndPlace16(contador_espumas)
    for i in range(len(objects)):
        objects[i].Delete()
    objects.clear()
    
    RDK.setParam('sensor3', 0) # Se activa nuevamente el sensor 3 para el siguiente ciclo
    break
