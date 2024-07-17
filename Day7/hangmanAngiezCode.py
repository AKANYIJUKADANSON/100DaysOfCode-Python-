import random
nameList = ['jane', 'ahmed', 'annabelle']

chosenWord = random.choice(nameList)

print(f"The chosen word is: {chosenWord}")

# Display the underscore representing each letter in the chosen word, if the chosenword is 4 char long then it should print ['_', '_', '_', '_']
display = []

for letter in chosenWord:
    display.append('_')
    
print(display)
    


# getting the position of each letter in the chosenword, then check the letter at that position and replace/display that letter if it matches the one on the same position in the chosen word
wordLenght = len(chosenWord)
# for position in range(wordLenght):
#     # Get the letter in position of the chosen word
#     letter = chosenWord[position]
#     if letter == guessLetter:
#         display[position] = letter
    
# print(display)

endGame = False
while not endGame:
    guessLetter = input("Enter any letter: ").lower()
    
    for position in range(wordLenght):
        letter = chosenWord[position]
        if letter == guessLetter:
            display[position] = letter
    
    print(display)  
    
    if '_' not in display:
        endGame = True
        print("congratulations, you won")
        exit()   
    

    
