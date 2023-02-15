import choice2
import os

def left_right():
    items = []
    input("Darkness...")
    input("\nA distant alarm grows louder. You sit up and rub your eyes...\n\n\n\n")


    print('''     _______________
    |,----------.  |\
    \n    ||           |=| |
    ||          || | |
    ||       . _o| | | __
    |`-----------' |/ /~/
     ~~~~~~~~~~~~~~~ / /
                     ~~\n\n\n''')
    print("It's not an alarm.....the TV? You know that image. It's the national EAS broadcast ")


    print("\nAs you rise from your bed, you hear muffled screams from outside. You run to your window and look out. People running, too many to count. Cars abandoned, buildings burning.")


    print("\nPounding footsteps from the hallway snap you out of your state of shock. You don't know what to do, but you know you can't stay here.")

    left_right = input("\nUneasy, you brace yourself and swing open the front door...left or right down the hall way? ")

    choice1 = left_right.lower()

    if choice1 == 'left':
        choice.left()
        os.system('clear')

    else:
        choice.right()
