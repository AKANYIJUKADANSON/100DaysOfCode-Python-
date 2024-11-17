
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~Nested dictionaries and lists
# Syntax:
    # dictionaryName = {key : nestedDictionaryName{key:value}}
    #                   key :           value
    
    # Can use both list in a dictionary or dictionary in another
    #   {
    #       key:[List]
    #       key:{Dictionary}
    #   }
    
studentDb = {
    "Year 4" : {"Shatin" : 99, "Kloe": 89, "Vannessa": 100, "Elvis": 100},
    "Year 1" : {"Chloe" : 92, "Adewa": 100, "Aseel": 82}
}

# Nesting list in a dictionary
travel_log = {
    "France" : ["Paris", "Djon"],
    "Uganda" : ["Kampala", "Jinja"]
}

# Nesting dictionary in a dictionary
travel_log = {
    "Kenya" : {"Visted_cities" : ["Kenya", "Nairobi"]}
}

travel_log = {
    "Kenya" : {"Visted_cities" : ["Kenya", "Nairobi"], "Total_Vists": 20}
}

# Nesting a dictionary in a list
travel_log = [
    {
        "country" : "Uganda",
        "Cities_visted" : ["Kampala", "Jinja"],
        "NumOfVists" : 12
    },
    
    {
        "country" : "Kenya",
        "Cities_visted" : ["Nairobi", "Nakuru"],
        "NumOfVists" : 7
    }
]

