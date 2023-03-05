#this project will look create Caesar Cipher


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(t, s):
    #estalishes variable
    encrypted_text  = ''
    length_text = len(alphabet)

    #this assigns the first letter of the word given, to LETTER
    for letter in t:
        #this steps through each letter of the alphabet
        for y in range(0, length_text):
            #this checks X against the index of alphabet and adds the encrypted letters based on SHIFT given
            if letter == alphabet[y]:
                y = y + s
                encrypted_text += alphabet[y]

    #this joins the list to a STRING and outputs the sentence requested
    print(f'\nThe encoded text is {encrypted_text}\n')

def decrypt(t, s):
    #establishes variable
    decrypted_text = ''
    length_text = len(alphabet)

    #this assigns the first letter of the word given, to LEETTER
    for letter in t:
        #this steps through each letter of the alphabet
        for y in range(0, length_text):
            #this checks X against the index of alphabet and adds the encrypted letters based on SHIFT given
            if letter == alphabet[y]:
                y = y - s
                decrypted_text += alphabet[y]

    print(f'\nThe encoded text is {decrypted_text}\n')




if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)
