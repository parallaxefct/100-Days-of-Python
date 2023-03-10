alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1

  for char in start_text:
    #this if statement ensures that if the character is not in alphabet it will do nothing with it
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")
  restart = input('\nDo you want to restart the cipher program?: ')

  if restart == 'yes':
      cipher_start()


def cipher_start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #this if statement ensures that regardless of the SHIFT amount that is input, the program will stay within the 26 characters in the alphabet
    if shift > len(alphabet):
        shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#Imports and prints the logo from art.py when the program starts.
import cipher_art
print(cipher_art.logo)
cipher_start()

#OR

#from cipher_art import logo
#print(logo)
