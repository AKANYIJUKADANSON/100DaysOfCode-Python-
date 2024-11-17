# Dictionaries use the key:value method
creatures_dictionary = {
    "Bird": "Hen, Dove, Turkey",
    "DomesticAnimals":"Goat, cow, Pig, Sheep",
    "WilAnimals": "Lion, Elephant, Cheeter"
}

# Retrieving data ina dictionary
# print("Wild Animals Include: " + creatures_dictionary["WilAnimals"])

# Adding data in a dictionary
creatures_dictionary['pets'] = "Cat, Dog"

# print(creatures_dictionary)

# Wiping a dictionary
# creatures_dictionary = {}

# Editing an item in a dictionary
# creatures_dictionary["Bird"] = "Hello, Woodie, Wekesa"
# print(creatures_dictionary)

# Looping through a dictionary
for key in creatures_dictionary:
    print(key)
    print(creatures_dictionary[key]) 