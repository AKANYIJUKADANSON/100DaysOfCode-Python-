import random

dice_side = random.randint(1,6)

if dice_side == 6:
    print(f"You toased a {dice_side}, move 6 steps and toas again")
elif dice_side == 5:
    print(f"You toased a {dice_side}, move five steps")
elif dice_side == 4:
    print(f"You toased a {dice_side}, move four steps")
elif dice_side == 3:
    print(f"You toased a {dice_side}, move 3 steps")
elif dice_side == 2:
    print(f"You toased a {dice_side}, move 2 steps")
else:
    print(f"You toased a {dice_side}, move one steps")