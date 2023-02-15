def insideApartment():
    print("\n\n\nYou slowly push the door open enough to fit through. You look around.")

    print("\nTo your left are racks of water, food, and a few first aid kits.")

    print("\nTo your right 4 flash lights, packs of batteries, spindels of rope, and jugs of gasoline.")

    print("\nIn front of you is a desk with a key on top and bat resting on the right side. You're unsure of what it unlocks.")

    item1 = input("\n\nTime to start grabbing things! However you can only hold 2 items. You should have worn the cargos. Left, Right, or desk?")

    item1 = item1.lower()

    if item1 == 'left':
        lItem()
    elif item1 == 'right':
        rItem()
    elif item1 == 'desk':
        desk()
    else:
        hallwayCont()
