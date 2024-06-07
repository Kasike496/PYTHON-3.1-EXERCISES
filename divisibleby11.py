#program to check if a number is divisible by 11
number=int(input("enter a number:")) #ask user to enter a number
if number%11==0: #if the remainder is 0, number is divisible by 11
    print("divisible by 11")
else:
    print("not divisible by 11")