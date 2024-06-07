#program to check if a number is divisible by 5
number=int(input("enter a number:")) #ask user to enter a number
if number%5==0: #if the remainder after division is 0 the number is divisible by 5
    print("divisible by 5")
else:
    print("not divisible by 5")