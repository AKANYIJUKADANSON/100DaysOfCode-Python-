alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(start_text, shift_value, cipher_direction):
    final_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_value
            final_text += alphabet[new_position]
        else:
            new_position = position - shift_value
            final_text += alphabet[new_position]
            
    print(f"The {cipher_direction}d text is {final_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text = text, shift_value = shift, cipher_direction = direction)

