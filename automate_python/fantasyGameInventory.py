#!/usr/bin/env python3
import pprint

inv = {
    'rope'      : 111,
    'torch'     : 6,
    'gold coin' : 42,
    'dagger'    : 1,
    'arrow'     : 12 ,
    }

dragonLoot = ['gold coin', 'rope' , 'dagger', 'gold coin', 'ruby',
              'dragon claw', 'dragon claw', 'dragon claw', 'dragon claw',
              'hammer', 'rope', 'dragon claw', 'hammer'  ]

def addToInventory(inventory, addItems):
    value = 0
    for key in addItems:
##        print('key = ' + key + '\t value =' + str(value) )
        inv.setdefault(key, 0)
##        inv[key] = inv[key] +1 
        inv[key] += 1 
##    pprint.pprint(str(inv))
    return inv

def displayInventory(inv):
    totalInv = 0
    print('==( Your Updated Inventory )==')
    for item, value in inv.items():
        print( str(value) + '\t = \t' + str(item))
        totalInv = totalInv + int(value)
    print('+' * 30)
    print( str(totalInv) + ' Total items Inventory')
    return totalInv

addToInventory(inv,dragonLoot)
displayInventory(inv)

