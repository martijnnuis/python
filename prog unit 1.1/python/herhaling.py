import random

def roll_dice():
    return random.randint(1,6)

dobbel = roll_dice()
dobbel2 = roll_dice()
dobbel3 = roll_dice()
dobbel4 = roll_dice()

print("rolled", dobbel)
print("rolled", dobbel2)
print("rolled", dobbel3)
print("rolled", dobbel4)

getallensort = [dobbel, dobbel2, dobbel3, dobbel4]
getallensort.sort()
print(getallensort)
getallensort.pop(0)
print(getallensort)
x = getallensort[0] + getallensort[1] + getallensort[2]
print(x)
