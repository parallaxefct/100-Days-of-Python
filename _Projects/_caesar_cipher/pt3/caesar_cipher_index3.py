#this is how to accomplish the cipher with index method
#the index() method will pull the index of a given letter in the alphabet list


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



#combined both functions into one function called caesar()

def caesar(given_text, shift_amount, direction_choice):
    #establishes variable
    converted_text = ''
    for x in given_text:
        position = alphabet.index(x)
        if direction_choice == 'decode':
            shift_amount *= -1
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        converted_text += new_letter

    print(f'The {direction_choice}d test is {converted_text}')

caesar(given_text=text, shift_amount=shift, direction_choice=direction)
