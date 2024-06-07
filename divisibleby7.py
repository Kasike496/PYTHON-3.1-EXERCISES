#program to check if a number is divisible by 7
number=int(input("enter a number:")) #ask user to enter a number
if number%7==0: #if remainder after division is 0, number is divisible by 7
    print("divisible by 7")
else:
    print("not divisible by 7")