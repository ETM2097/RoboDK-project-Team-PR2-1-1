# UR10 Pick and Place Program
## Project Overview

The program consists of a pick-and-place system using a UR10 robot. The main objective is for the robot to be able to identify, pick up, and place each of the objects (bottles and foam) in their assigned positions automatically.

This module of the project seeks to implement the logic that allows the robot to perform tasks related to the handling of both foam and bottles, depending on the type of method chosen (16/32 bottles).

**Responsible:** Sergio Real Gonzalvo

## Implementation Rationale

This part of the project has been carried out with the aim of optimizing the robot's execution time and the precision with which objects are placed. Various factors have been taken into account, such as the robot's speed, the trajectory to be followed, and the coordination between movements, in order to minimize errors and improve the efficiency of the process.

For this reason, different programming techniques have been used to control the robot effectively and easily, allowing any future modifications to the system parameters to be adjusted without major complications.

## Core Mechanics

> [!IMPORTANT]
> The following must be available in the RoboDK station beforehand: UR10 with its gripper (GripperR2), the defined targets, and the template foams (E1, E2, E3) for the program to work correctly.

The program is structured as follows:

- **Imports:** All libraries necessary for the robot to function correctly are imported, as well as some others to manage certain aspects of the system.


```python
from robodk import robolink, robomath
import time
import math
```

- **Extracting objects from the program:** Each of the objects to be manipulated within the project (UR10 and its gripper (GripperR2)) are obtained for later use.

```python
RDK = robolink.Robolink()
robot = RDK.Item('UR10', robolink.ITEM_TYPE_ROBOT)
gripper = RDK.Item('GripperR2', robolink.ITEM_TYPE_TOOL)
```

- **Definition of each of the targets and positions:** The different positions that the robot will use throughout the program to perform pick and place tasks are extracted.

```python
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
```

<i>Each of these targets has been previously defined in the RoboDK environment. The aim is to export them so that they can be manipulated.</i>

- **Global program configuration:** Certain parameters and settings are defined in order to avoid repeating code throughout the program. This facilitates future modification if necessary.

```python
ALTURA_ESPUMA = 10.0 # Height of each foam piece
contador_espumas = 1 # How many foam pieces have to be picked
objects = [] # List to store all program pieces (bottles and foams)
```

- **Funciones auxiliares:** A function is defined `mover_offset_z(target_item, offset_z)` which allows the robot to be moved along the Z axis a specified distance from the position of a specific target.
  <br>The purpose of this function is to avoid repeating code throughout the program.

```python
def mover_offset_z(target_item, z_offset):
    pose_base = target_item.Pose()
    robot.MoveL(pose_base * robomath.transl(0, 0, z_offset))
```

On the other hand, a function `regenerar_espuma(numero)` is defined, which is responsible for creating new foam at the initial position whenever a new piece is needed. This prevents the robot from always having foam to collect.
<br>If there is no foam available, the robot will wait until it is available again.

```python
def regenerar_espuma(numero):
    nombre_objetivo = f"E{numero}"
    nombre_template = f"Template_E{numero}"

    # If it already exists, use it
    item_existente = RDK.Item(nombre_objetivo, robolink.ITEM_TYPE_OBJECT)
    if item_existente.Valid():
        return item_existente

    # If not, copy from the template
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
```

- **Main functions:** Two different functions are defined to manage each of the pick and place programs ( `pickAndPlace16(contador_espumas)` and `pickAndPlace32(contador_espumas)` ). <br> Each one is responsible for managing the logic necessary for the robot to perform the tasks of picking up and placing the bottles and foam according to the chosen method.

<br> <i>Both functions follow a similar structure, differing in the cycles and the positions in which the bottles are placed.</i>

<details open>
<summary>Función auxiliar para pick and place de 16 botellas [Código en Python]</summary>

```python
def pickAndPlace16(contador_espumas):
    NUM_CICLO = 4
    for i in range(1, NUM_CICLO):
        # If it is not the second iteration, the pick and place of the foams will be done
        if i != 2:
            # PHASE A: FOAM

            # Regenerate foam
            item_espuma = regenerar_espuma(contador_espumas)

            # Calculation of heights according to the case
            z_pick = (NUM_CICLO - contador_espumas) * ALTURA_ESPUMA
            match i:
                case 1:
                    z_place = (contador_espumas - 1) * ALTURA_ESPUMA
                case 3:
                    z_place = (contador_espumas - 1) * ALTURA_ESPUMA - 143
            # End of match

            # Movements to prepick and pick zones
            robot.MoveJ(t_prepick_espuma)
            mover_offset_z(t_pick_espuma, z_pick)

            # Grab foam
            if item_espuma and item_espuma.Valid():
                item_espuma.setParentStatic(gripper)

            # Return to prepick zone and then to step 1
            robot.MoveL(t_prepick_espuma)
            robot.MoveJ(t_paso_1)

            # Movements to preplace and place zones
            robot.MoveJ(t_preplace_espuma)
            mover_offset_z(t_place_espuma, z_place)
            # Add the object to the list
            objects.append(item_espuma)

            # Release foam
            if item_espuma and item_espuma.Valid():
                item_espuma.setParentStatic(RDK.Item('Station'))

            # Return to preplace zone
            robot.MoveL(t_preplace_espuma)

            # COUNTER
            contador_espumas += 1
            if contador_espumas <= NUM_CICLO:
                robot.MoveJ(t_home)
            RDK.ShowMessage(f"Contador espumas: {contador_espumas}", False)
        else:
            # On the contrary, if it is the second iteration, the pick and place of the bottles will be done
            # PHASE B: CONVEYOR BELT (Wait for Semaphore)
            print("Robot: Esperando pieza en cinta...")

            while RDK.getParam('IO_PiezaLista') != 1:
                time.sleep(0.05)

            # Read the name of the piece
            nombre_pieza = RDK.getParam('IO_NombrePieza')
            item_botella = RDK.Item(nombre_pieza, robolink.ITEM_TYPE_OBJECT)
            print(f"Robot: Recogiendo {nombre_pieza}")

            # Pick up
            robot.MoveJ(t_prepick_bot)
            robot.MoveL(t_pick_bot)  # We use the reference target instead of the bottle position to ensure it goes to the position

            # Verify if the piece exists before moving
            if item_botella.Valid():
                item_botella.setParentStatic(gripper) # This notifies the conveyor belt
            else:
                robot.MoveL(t_pick_bot)

            robot.MoveL(t_prepick_bot)

            # Delivery
            robot.MoveJ(t_paso_2)
            robot.MoveJ(t_preplace_bot)
            robot.MoveL(t_place_bot)

            # Add the object to the list
            objects.append(item_botella)

            if item_botella.Valid():
                item_botella.setParentStatic(RDK.Item('Station'))
                # item_botella.Delete()

            robot.MoveL(t_preplace_bot)

        # COUNTERS
        if contador_espumas <= NUM_CICLO:
            robot.MoveJ(t_home)
        RDK.ShowMessage(f"Contador espumas: {contador_espumas}", False)

```

</details>

<details>
<summary>Auxiliary function for picking and placing 32 bottles [Python code]</summary>

```python
def pickAndPlace32(contador_espumas):
    NUM_CICLO = 6
    for i in range(1, NUM_CICLO):
        # If it is not the second iteration, the pick and place of the foams will be done
        if i != 2 and i != 4:
            # PHASE A: FOAM
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

            # End of match
            robot.MoveJ(t_prepick_espuma)
            mover_offset_z(t_pick_espuma, z_pick)

            if item_espuma and item_espuma.Valid():
                item_espuma.setParentStatic(gripper)

            robot.MoveL(t_prepick_espuma)
            robot.MoveJ(t_paso_1)

            robot.MoveJ(t_preplace_espuma)
            mover_offset_z(t_place_espuma, z_place)
            # Add the object to the list
            objects.append(item_espuma)

            if item_espuma and item_espuma.Valid():
                item_espuma.setParentStatic(RDK.Item('Station'))

            robot.MoveL(t_preplace_espuma)
            contador_espumas += 1
            if contador_espumas <= NUM_CICLO:
                robot.MoveJ(t_home)
            RDK.ShowMessage(f"Contador espumas: {contador_espumas}", False)
        else:
            # PHASE B: CONVEYOR BELT (Wait for Semaphore)
            print("Robot: Esperando pieza en cinta...")

            while RDK.getParam('IO_PiezaLista') != 1:
                time.sleep(0.05)

            # Read the name of the piece
            nombre_pieza = RDK.getParam('IO_NombrePieza')
            item_botella = RDK.Item(nombre_pieza, robolink.ITEM_TYPE_OBJECT)
            print(f"Robot: Recogiendo {nombre_pieza}")

            # Pickup
            robot.MoveJ(t_prepick_bot)
            robot.MoveL(t_pick_bot)  # We use the reference target instead of the bottle position to ensure it goes to the position

            # Verify if the piece exists before moving
            if item_botella.Valid():
                item_botella.setParentStatic(gripper) # This notifies the conveyor belt
            else:
                robot.MoveL(t_pick_bot) 

            robot.MoveL(t_prepick_bot)

            # If it is the second iteration, it will be placed at the base of the box

            # Delivery
            robot.MoveJ(t_paso_2)
            robot.MoveJ(t_preplace_bot)

            # Depending on the iteration, it will be placed at one height or another
            if i == 2:
                robot.MoveL(t_place_bot)
            else:
                mover_offset_z(t_place_bot, -135)  # Upper bottle placement

            # Insert the object into the list
            objects.append(item_botella)

            if item_botella.Valid():
                item_botella.setParentStatic(RDK.Item('Station'))
                # item_botella.Delete()
            robot.MoveL(t_preplace_bot)
        # end of if

        # COUNTERS
        if contador_espumas <= NUM_CICLO:
            robot.MoveJ(t_home)
        RDK.ShowMessage(f"Contador espumas: {contador_espumas}", False)
```

</details>

- **Main loop:** A main loop is defined that will always execute the desired program. In this case, we have chosen to include both to highlight the difference between them. It is also important to note that a loop is used to go through the entire array of objects that we have previously defined so that they can all be deleted at the end of the program.

```python
for i in range(len(objects)):
    objects[i].Delete()
    objects.clear()
    contador_espumas = 1
    time.sleep(5)
```

## System Integration

The UR10 communicates primarily with the conveyor belt that supplies the bottles. This communication is carried out through input and output signals that allow the robot to know when a bottle is ready to be picked up, thanks also to the barrier sensor. In addition, the robot interacts with the foam pads, ensuring that there is always one available for picking up and subsequent placement.

To do this, parameters from RoboDK's own library are used. <br>

From the bottle conveyor belt program, the `IO_PiezaLista` parameter is set to 1 when a bottle is ready to be picked up with the RDK.setParam ('IO_PiezaLista', 1) function. <br>

The UR10 robot monitors this parameter in a loop, waiting until its value is 1 before proceeding with the collection of the bottle. To do this, the function `RDK.getParam ('IO_PiezaLista')` is used from the robot program `UR10.py`.



<i>In [conveyorSpawn.py](conveyorSpawn.py) :</i>

```python
# ALERT FOR ROBOT
RDK.setParam('IO_NombrePieza', oldest_part.Name())
RDK.setParam('IO_PiezaLista', 1) # GREEN TRAFFIC LIGHT
RDK.RunProgram('UR10')

oldest_part.sent_signal = True
oldest_part.Recolor([0, 1, 0, 1]) # VISUAL

# ACTIVE WAIT (Until the robot takes it)
while oldest_part.Valid() and oldest_part.Parent().Name() == FRAME_MOVER_NAME:
    time.sleep(0.05)

print("Cinta: Pieza recogida. Reiniciando semáforo.")
RDK.setParam('IO_PiezaLista', 0) # RED TRAFFIC LIGHT
active_parts.pop(0)
```

<i>In [UR10.py](UR10.py) :</i>

```python
# PHASE B: CONVEYOR (Wait for Signal)
print("Robot: Esperando pieza en cinta...")

while RDK.getParam('IO_PiezaLista') != 1:
    time.sleep(0.05)

# Read bottle name
nombre_pieza = RDK.getParam('IO_NombrePieza')
```

On the other hand, foam templates created using [TemplateCreator.py](TemplateCreator.py) are also used to regenerate the foam whenever the robot needs it.

## Alternative Approaches - Methods considered and reasons for rejection

The possibility of using a vision system to identify and locate the bottles on the conveyor belt was considered. However, this option was ruled out due to the additional complexity involved in integrating the vision system with the **UR10** robot, as well as potential problems with accuracy and reliability in detecting the bottles. <br>Instead, a system based on sensors and input/output signals was chosen, which proved to be simpler and more effective for the purpose of the project.

In addition, the option of using a different robot was evaluated, but it was decided to keep the existing one due to its versatility and ability to handle the pick-and-place tasks required in this part of the automation

## Technical Specifications - Key parameters, algorithms, and design decisions

- **Robot:** UR10
- **Tool:** OnRobot VG10 Vacuum Gripper
- **Programming Language:** Python
- **Software Platform:** RoboDK
- **Key Parameters:**
- Foam height: 10.0 mm
  - Number of foam samples to be collected: Variable depending on the method (16 or 32 bottles)
- **Algorithms:**
- **Pick and place** functions to manage the logic of picking up and placing both bottles and foam.
  - **Foam regeneration** function to ensure continuous availability of parts for the robot.
- Movement function with **offset on the Z axis** to facilitate robot movements without repeating code.
- Function in the [TemplateCreator.py](TemplateCreator.py) file to create foam templates.
- **Design Decisions:**
- Use of loops and conditional structures to manage the different phases of the pick and place process.
- Implementation of a communication system based on input/output signals to coordinate the robot with the conveyor belt.
- Modularization of the code using auxiliary functions to improve the readability and maintainability of the program.

## Testing & Validation - Test results and performance report

Throughout the development of the program, multiple tests were performed to validate the effectiveness of each of the implemented functions.

It was verified that the **UR10** robot could **pick up and place** both the bottles and the foam in the correct positions without errors.
In addition, the correct **communication** between the robot and the **conveyor belt** was checked, ensuring that the **input/output** signals worked as expected.

On the other hand, the performance of the system was evaluated in terms of **cycle time** and **accuracy** in the placement of objects. The results showed that the robot could complete the pick and place tasks correctly and efficiently, with adequate accuracy for the intended purpose of the project.

## Future Improvements

In the future, some improvements could be considered to further optimize the system:

- Implement a **vision system** to improve the detection and location of bottles on the conveyor belt.
- Optimize the robot's **trajectories** to further reduce cycle time.
- Add more **functionalities** to the system, such as the ability to handle different types of objects or adapt to changes in the working environment.

However, the current system meets the requirements set for the project and provides a solid foundation for future expansions and improvements.

In addition, RoboDK offers many functionalities, but it is believed that **ROS (Robot Operating System)** could be used as an alternative to manage communication between the different components of the system, as well as to implement more advanced control algorithms for the UR10 robot.

## References & Documentation - Supporting materials and standards

- [RoboDK Documentation](https://robodk.com/doc/en/)
- [UR10 Robot Specifications](https://www.universal-robots.com/products/ur10-robot/)
- [Python Docs](https://www.python.org/doc/)

