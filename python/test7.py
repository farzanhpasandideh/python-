import math
while True:
    a=int(input("please enter a:"))
    b=int(input("please enter b:"))
    op=input("choose the operation")


    if op=="+":
        result=a+b

    if op=="_":
        result=a-b

    if op=="*":
        result=a*b

    if op=="/":
        if b==0:
            print("Error")
        else:
            result= a/b

    if op=="radical":
        result=math.sqrt(a)

    if op=="sin":
        result=math.sin(a)

    if op=="cos":
        result=math.cos(a)  

    if op=="tan":
        result=math.tan(a)

    if op=="factorical":
        result=math.factorial(a)
    
    if op=="cot":
        result=math.cos(a)/math.sin(a)

    print(result)

    op2= input("to exit enter 'q', to continue enter 'c' :")
    if op2 == "q":
        print("finished")