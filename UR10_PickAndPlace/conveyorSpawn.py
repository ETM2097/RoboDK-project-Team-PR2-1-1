from robodk import robolink, robomath
import time

RDK = robolink.Robolink()

# Teneis que añadir los siguientes elementos en la estación de RoboDK:
# 1. Un Frame llamado 'conveyorMover' que simule el movimiento de la cinta. 
# 2. Un Frame llamado 'spawnPick' que indique el punto de generación de piezas. (al inicio de la cinta)
# 3. Un Frame llamado 'sensorPickFrame' que indique la posición del sensor. (a la altura de pick)

# Configuración
FRAME_MOVER_NAME  = 'conveyorMover'
FRAME_SPAWN_NAME  = 'spawnPick'
FRAME_SENSOR_NAME = 'sensorPickFrame'
TEMPLATE_NAME     = 'materialPick'

# Reset inicial de seguridad
RDK.setParam('IO_PiezaLista', 0)
RDK.setParam('IO_NombrePieza', '')

# Referencias
frame_spawn  = RDK.Item(FRAME_SPAWN_NAME, robolink.ITEM_TYPE_FRAME)
frame_sensor = RDK.Item(FRAME_SENSOR_NAME, robolink.ITEM_TYPE_FRAME)
frame_mover  = RDK.Item(FRAME_MOVER_NAME, robolink.ITEM_TYPE_FRAME)
material     = RDK.Item(TEMPLATE_NAME, robolink.ITEM_TYPE_OBJECT)

# IMPORTANTE: Ocultamos el template original
if material.Valid():
    material.setVisible(False)

# Parámetros Cinta
CONVEYOR_SPEED   = 10.0   
SPAWN_FREQUENCY  = 40     
RESET_THRESHOLD  = 2000.0 

active_parts = []         
loop_counter = 0
current_conveyor_pos = 0.0
SENSOR_X_WORLD = frame_sensor.PoseAbs().Pos()[0]

print("Cinta con Protocolo IO iniciada.")

# Establecemos siempre las coordenadas del punto de conveyorMover a [  6083.405762, -1985.255249,    66.091003,     0.000000,     0.000000,     0.000000 ]
# Si no existe, se crea en la misma posición que el frame del spawnPick
if not frame_mover.Valid():
    frame_mover = RDK.AddFrame(FRAME_MOVER_NAME)
    frame_mover.setPose(frame_spawn.PoseAbs())
# Si existe pero tiene unas coordenadas distintas a las del spawnPick, se ponen en la misma y si no se encuentra alguna de ellas, se lanza error
else:
    pose_mover = frame_mover.PoseAbs()
    pose_spawn = frame_spawn.PoseAbs()
    for i in range(3):
        if abs(pose_mover.Pos()[i] - pose_spawn.Pos()[i]) > 0.01:
            pose_mover.setPos(pose_spawn.Pos())
            frame_mover.setPose(pose_mover)
            break
    

while True:
    start_time = time.time()
    
    # A. Movimiento
    current_conveyor_pos += CONVEYOR_SPEED
    frame_mover.setPose(robomath.transl(-current_conveyor_pos, 0, 0) * frame_spawn.PoseAbs())
    
    # B. Reset (Cinta Infinita)
    if current_conveyor_pos > RESET_THRESHOLD:
        RDK.Render(False)
        
        # Guardar posiciones absolutas de las piezas antes del reset
        part_absolute_poses = []
        for p in active_parts:
            if p.Valid():
                part_absolute_poses.append(p.PoseAbs())
        
        # Reset del frame a la posición inicial
        frame_mover.setPose(frame_spawn.PoseAbs())
        current_conveyor_pos = 0.0
        
        # Reposicionar las piezas en coordenadas relativas al frame reseteado
        for i, p in enumerate(active_parts):
            if p.Valid() and i < len(part_absolute_poses):
                p.setParent(frame_mover)
                p.setPose(frame_mover.Pose().inv() * part_absolute_poses[i])
        
        RDK.Render(True)

    # C. Spawn (Generación)
    if loop_counter % SPAWN_FREQUENCY == 0:
        if material.Valid():
            material.Copy()
            new_part = RDK.Paste()
            if new_part.Valid():
                new_part.setName(f"Part_{loop_counter}") 
                new_part.setParent(frame_mover)
                new_part.setPose(frame_mover.Pose().inv() * frame_spawn.PoseAbs())
                new_part.setVisible(True)
                active_parts.append(new_part)

    # D. Sensor con Semáforo (Protocolo IO)
    if len(active_parts) > 0:
        oldest_part = active_parts[0]
        
        if not oldest_part.Valid():
            active_parts.pop(0)
        else:
            part_x = oldest_part.PoseAbs().Pos()[0]
            dist = part_x - SENSOR_X_WORLD
            
            # Ventana de detección
            if (-(CONVEYOR_SPEED*2) < dist < CONVEYOR_SPEED+1) and not hasattr(oldest_part, 'sent_signal'):
                
                print(f"Cinta: {oldest_part.Name()} lista. Esperando robot...")
                
                # AVISO AL ROBOT
                RDK.setParam('IO_NombrePieza', oldest_part.Name())
                RDK.setParam('IO_PiezaLista', 1) # SEMÁFORO VERDE
                
                oldest_part.sent_signal = True
                oldest_part.Recolor([0, 1, 0, 1]) # VISUAL
                
                # ESPERA ACTIVA (Hasta que el robot se la lleve)
                while oldest_part.Valid() and oldest_part.Parent().Name() == FRAME_MOVER_NAME:
                    time.sleep(0.05)
                
                print("Cinta: Pieza recogida. Reiniciando semáforo.")
                RDK.setParam('IO_PiezaLista', 0) # SEMÁFORO ROJO
                active_parts.pop(0)

            elif dist < -800: # Limpieza de seguridad, en caso de que la pieza no sea recogida o pase algo
                active_parts.pop(0)

    loop_counter += 1
    
    # Control de CPU
    elapsed = time.time() - start_time
    if elapsed < 0.01: time.sleep(0.01 - elapsed)
