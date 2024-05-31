
def create_inventory(items):
    my_map = dict()
    for i in items:
        if i not in my_map:
            my_map[i] = 1
        else:
            my_map[i] += 1

    return my_map

def add_items(inventory, items):
   my_map = inventory
   for i in items:
        if i not in my_map:
            my_map[i] = 1
        else:
            my_map[i]+=1
   return my_map


def decrement_items(inventory, items):
    my_map = inventory
    for i in items:
        if i in my_map:
            my_map[i] -=1
            if my_map[i] < 0:
                my_map[i] = 0
    return my_map  


def remove_item(inventory, item):
    my_map = inventory
    if item in my_map:
        del(my_map[item])
    return my_map


def list_inventory(inventory):
    my_map = dict()
    for articulo, cantidad in inventory.items():
        if cantidad > 0:
            my_map[articulo] = cantidad
        
    return list(my_map.items())
