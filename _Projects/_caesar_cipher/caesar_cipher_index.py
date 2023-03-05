#this is how to accomplish the cipher with index method
#the index() method will pull the index of a given letter in the alphabet list


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(given_text, shift_amount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.

    #source_text = []
    #encrypted_text  = []
    #length_text = len(alphabet)

    #creates a list for the word given
    #for i in t:
        #source_text.append(i)

    #this assigns the each letter to X varibale
    for x in given_text:
        #establishes variable
        cipher_text = ''

        #finds the position of given_text letters
        position = alphabet.index(x)
        #adds shift amount to position
        new_position = position + shift_amount
        #pulls the letter of new_position
        new_letter = alphabet[new_position]

        #adds letter to STRING variable
        cipher += new_letter

    #this joins the list to a STRING and outputs the sentence requested
    encrypted_text = ''.join(encrypted_text)
    print(f'\nThe encoded text is {encrypted_text}\n')

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == 'encode':
    encrypt(given_text=text, shift_amount=shift)

#else:
