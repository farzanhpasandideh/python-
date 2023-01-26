import random

pc_number=random.randint(0, 20)
num= 0
while True:
    user_number= int(input("enter a number between 0 and 20:"))
    num+=1
    if pc_number==user_number:
        print("you wonl", "tries:", num)
        break

    if pc_number < user_number:
        print("lower!")


    if pc_number > user_number:
       print("higher!")