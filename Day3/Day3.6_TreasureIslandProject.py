
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

# Where to go
where_to_go = input('You are at cross roads, where do you want to go? Type "Left" or "Right"\n')
if where_to_go.lower() == "left":
    swim_or_wait = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat. Type "swim" to swim accross.\n')
    if swim_or_wait.lower() == "wait":
        choose_door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n')
        if choose_door.lower() == "yellow":
            print("You found the treasure. You win!")
        else:
            print("The game is over, you fell into a room of hyenas")
    else:
        print("The game is over, crocodiles are patiently waiting to feast")   
else:
    print("The game is over, to the right you will fall into a den of lions")
