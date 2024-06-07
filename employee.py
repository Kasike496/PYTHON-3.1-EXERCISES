#program to calculate bonus given to employees
salary=float(input("enter salary:")) #ask employee to enter salary
years_of_service=int(input("enter years of service:")) #ask employee to enter years of service
if years_of_service>10: #calculate bonus of more than 10years of service
    bonus= (salary*0.1)
    print(bonus)
elif years_of_service>=6 and years_of_service and years_of_service<=10: #bonus of 6 to 10 years of service
    bonus=(salary*0.08)
    print(bonus)  
elif years_of_service<6: #bonus for less than 6years of service
    bonus=(salary*0.05)
    print(bonus)     
