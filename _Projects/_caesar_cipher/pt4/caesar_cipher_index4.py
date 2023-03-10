alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

  print(f"Here's the {cipher_direction}d result: {end_text}")

#Imports and prints the logo from art.py when the program starts.
import cipher_art
print(cipher_art.logo)

#OR

#from cipher_art import logo
#print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#this if statement ensures that regardless of the SHIFT amount that is input, the program will stay within the 26 characters in the alphabet
if shift > len(alphabet):
    shift = shift % 26

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
