#figure out how many cans of paint are needed, provided given surface areas

def paint_calc(height, width, cover):
    numbers_of_cans = (height * width) / cover
    numbers_of_cans = round(numbers_of_cans)
    print(f'You\'ll need {numbers_of_cans} cans of paint.')

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
