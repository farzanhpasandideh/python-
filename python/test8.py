a= float(input("please enter a="))
b= float(input("please enter b="))
c= float(input("please enter c="))

if a+b>c and a+c>b and b+c>a:
    result=print("it is a triangle.")
else:
    result=print("it is not triangle.")

print(result)