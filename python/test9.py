num=input("Enter the number of the students:")
for i in range(num):
    name=int(input("please enter your first name:"))
    family=input("please enter your family name:")
    course1=float(input("please enter your first corse grade:"))
    course2=float(input("please enter your second corse grade:"))
    course3=float(input("please enter your third corse grade:"))
    average= (course1+course2+course3)/3

    if average>=17:
        result=("Great.")
    if 12<=average and average<17:
        result= ("normal.")
    if average<12:
        result=("fail.")

    print("the student's name is ", name,family,"and her/his status is ", result)