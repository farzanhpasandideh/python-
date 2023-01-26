import random

number1=random.randint(1,6)

if number1==6:
    number2=random.randint(1, 6)
    number3=random.randint(1, 6)
    print("you've got a 6! your second attempt is ", number2, "and your third attempt is ",number3)

else:
    print("you've got a", number1)
