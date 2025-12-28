from robodk import robolink, robomath

RDK = robolink.Robolink()
MAX_CICLOS = 3

for i in range(1, MAX_CICLOS + 1):
    nombre_org = f"E{i}"
    nombre_tpl = f"Template_E{i}"
    
    item_org = RDK.Item(nombre_org, robolink.ITEM_TYPE_OBJECT)
    item_tpl = RDK.Item(nombre_tpl, robolink.ITEM_TYPE_OBJECT)
    
    # Si existe E1 pero no Template_E1 -> Lo convertimos
    if item_org.Valid() and not item_tpl.Valid():
        item_org.setName(nombre_tpl)
        item_org.setVisible(False)
        print(f"OK: {nombre_org} convertido en {nombre_tpl}")
        
    # Si ya existe el Template -> Todo correcto
    elif item_tpl.Valid():
        print(f"OK: {nombre_tpl} ya existe.")
        # Si sobra un E1 suelto por ahí, lo borramos para limpiar
        if item_org.Valid(): 
            item_org.Delete()
            
    else:
        print(f"ALERTA: Falta la pieza {nombre_org} para crear el molde.")
