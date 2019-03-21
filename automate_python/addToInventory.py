#!/usr/bin/env python3

# Add to inventory

def addToInventory(inventory, addedItems):

    for item in dragonLoot:
        if item in inv.keys():
            inv[item] += 1
        else:
            inv.update({item : 1})
    return inv

def displayInventory(inv):
    z = 0
    for i in inv.values():
        print(i)
        z = z + i
    print('Total inventory is : \n' + str(z) )
    print(inv)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby' ]
 


inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
