from containers import *
from map_class import Grid
from object_creator import Create

# needed to object test
from objects import *

def generate(grid_z, lower=True):
    # GRID defines the grid size, generate with define the biome, 
    # Thus: this is where we change the grid size and we wont pass it into generate.
    
    map_area = Grid(grid_biome='village')
    WORLD_CONTAINER.append(map_area)
    
    # Stairs
    if grid_z > 0:
        [(entrance_x, entrance_y)] = [(object.x, object.y) for object in OBJECT_CONTAINER]
        stair_object = Stairs(not lower)
        entrance = Object_Place(entrance_x, entrance_y, grid_z, 'Up Stair', '<', stairs=stair_object)
        if not lower:
            stair_object = Stairs(lower)
            entrance = Object_Place(entrance_x, entrance_y, grid_z, 'Down Stair', '>', stairs=stair_object)            
        OBJECT_CONTAINER.append(entrance)

    exit_x, exit_y = map_area.exit_point
    stair_object = Stairs(lower)
    exit = Object_Place(exit_x, exit_y, grid_z, 'Down Stair', '>', stairs=stair_object)
    if not lower and grid_z > 0:
        stair_object = Stairs(lower)
        exit = Object_Place(exit_x, exit_y, grid_z, 'Up Stair', '<', stairs=stair_object)
    OBJECT_CONTAINER.append(exit)
        
    
    food = Create(grid_z).food()

    bucket_storage = Storage(capacity=25, contains=[food])
    bucket = Object_Place(5, 3, grid_z, 'bucket', 'u', storage=bucket_storage)
    OBJECT_CONTAINER.append(bucket)
    
    make_weapon = Create(7, 5, grid_z).weapon()
    OBJECT_CONTAINER.append(make_weapon)
    
    ring_item = Item(weight=2, value=30)
    ring_equip = Equipment(['Finger'], magnitute=78, affect='power')
    ring = Object_Place(None, None, grid_z, 'Ring Of Power', 'o', item=ring_item, equipment=ring_equip)
    
    animal_object = Creature(hp=12, power=5, death=creature_death, inventory=[], attire=[ring])
    final_animal = Object_Place(5, 7, grid_z, 'pig', 'p', creature=animal_object)
    OBJECT_CONTAINER.append(final_animal)

    for building in map_area.rooms:
        # should pass 'structure_value' into the creation property distribution
        structure_value = building.room.value
        
        for (x, y) in building.room.door_space:
            # need unlocked doors on shop and low value houses
            place = Create(x, y, grid_z, structure_value)
            door = place.door()
            OBJECT_CONTAINER.append(door)
            
        for (x, y) in building.room.object_space:
            place = Create(x, y, grid_z, structure_value)
            animal = place.tame_animal()
            # if structure_value > 80:
                # animal = obj.create_tame_animal(x, y, map_area)
            # elif structure_value < 10:
                # animal = obj.create_tame_animal(x, y, map_area)
            # else:
                # animal = obj.create_tame_animal(x, y, map_area)
            OBJECT_CONTAINER.append(animal)

 
