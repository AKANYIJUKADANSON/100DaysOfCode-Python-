
district_list = ["Kabale", "Kasese", "Mbarara", "Mbale", "Alua", "Jinja", "Kampala"]

# Adding an item at the end of list
district_list.append("Kitgum")

# Insert an item at a given position
# NOTE: The position starts from 1 not 0 like as is in indicies
district_list.insert(3, "Kalangala")

# Remove an item
# district_list.remove("Kabale")

# removes the item at an index provided
district_list.pop(1)

# Clearing the list
# district_list.clear()

# no_of_distrcts = len(district_list)
# if district_list == []:
#     print("The list is empty")
# else:
#     print(f"List has {no_of_distrcts} items")

print(district_list)

# Sorting the list items
sortedList = district_list.reverse()
print(f"Sorted list{sortedList}")

my_copy = district_list.copy()

print(f"My copy is: {my_copy}")
print(district_list)