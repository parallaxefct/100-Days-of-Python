import os
import found_items

def left():
    print("\n\n\nYou start running.")
    print("\nAs you're headed down the hallway you pass your neighbors apartment, the door slightly ajar. You remember they are prepers. The \"preparing for dooms-day\" type.")
    choice = input("\nDo you go in? ")
    choice = choice.lower()

    if choice == 'yes':
        choice3_found_items.insideApartment()

    else:
        choice3_keep_going.keepGoing()
