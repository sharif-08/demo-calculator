num1 = float(input("enter your number\n"))
num2 = float(input("enter your number \n"))
print(" chose 1 for add\n chose 2 for substraction\n chose 3 for multiplication\n chose 4 for divide ")
chose = int(input("please chose 1 4:\n "))
if chose == 1:
    print(num1+num2)
elif chose ==2:
    if num1 > num2:
        print(num1-num2)
    else:
        print("-",num2-num1)
elif chose == 3:
    print(num1*num2)
elif chose == 4:
    if num2 == 0:
        print("can't divide by zero ")
    else:
        print(num1/num2)
else:
    print("chose correct number ")

