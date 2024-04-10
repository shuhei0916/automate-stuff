def display_inventory(inventory):
    print("Inventory List: ")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + ' ' + k)
    print('total items: ' + str(item_total))

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

inv = {'coins': 42, 'rope': 1}

dragon_loot = ['coins', 'shuriken', 'coins', 'coins', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

# stuff = {'rope': 1, 'toarch': 6, 'coins': 42, 'shuriken': 1, 'arrows': 12}
# display_inventory(stuff)