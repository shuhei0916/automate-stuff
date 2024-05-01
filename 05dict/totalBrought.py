def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)

    return num_brought

all_guests = {'Alice': {'apples': 5, 'bananas': 12},
              'BoB': {'hams': 3, 'apples': 2},
              'Alice': {'cups': 3, 'applepie': 1}}

print(' - apples ' + str(total_brought(all_guests, 'apples')))
print(' - cupes ' + str(total_brought(all_guests, 'cups')))