# Wall Paint calculator
# To round up so that even if the paint is 12.2, then we cant buy .2 litres but rather have to buy the whole can
# So the value must be rounded up and this can be achieved by using the ceiling math function

import math
def paint_calc(height, width, cover):
    capacity = math.ceil((height * width) / cover)
    print(f"You will need {capacity} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Height of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)