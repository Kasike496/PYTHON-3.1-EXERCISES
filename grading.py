#grading system
"""prompt user to enter marks for 3 units"""
computer=int(input("enter computer score:")) 
java=int(input("enter java score:"))
python=int(input("enter python score:"))
average_score=((computer+java+python)/3) #calculates the average score for the three units
print("average_score", average_score) #prints the average score of the three units 
if average_score>=70 and average_score<=100: #prints grade A
    grade=("A")
    print(grade)
elif average_score>=60 and average_score<=69: #prints grade B
    grade=("B")
    print(grade)
elif average_score>=50 and average_score<=59: #prints grade C
    grade=("C")
    print(grade)
elif average_score>=40 and average_score<=49: #prints grade D
    grade=("D")
    print("grade")
else:
    #prints failed 
    grade=("failed")
    print("grade")                 