#this is how to accomplish the cipher with index method
#the index() method will pull the index of a given letter in the alphabet list


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(given_text, shift_amount):
    #establishes variable
    cipher_text = ''
    #this assigns the each letter to X varibale
    for x in given_text:
        #finds the position of given_text letters
        position = alphabet.index(x)
        #adds shift amount to position
        new_position = position + shift_amount
        #pulls the letter of new_position
        new_letter = alphabet[new_position]

        #adds letter to STRING variable
        cipher_text += new_letter

    print(f'\nThe encoded text is {cipher_text}\n')

def decrypt(cipher_text, shift_amount):
    #establishes variable
    decrypted_text = ''
    #this assigns the each letter to X varibale
    for x in cipher_text:
        #finds the position of given_text letters
        position = alphabet.index(x)
        #adds shift amount to position
        new_position = position - shift_amount
        #pulls the letter of new_position
        new_letter = alphabet[new_position]

        #adds letter to STRING variable
        cipher_text += new_letter

    print(f'\nThe encoded text is {decrypted_text}\n')



if direction == 'encode':
    encrypt(given_text=text, shift_amount=shift)
else:
    decrypt(cipher_text=text, shift_amount=shift)
