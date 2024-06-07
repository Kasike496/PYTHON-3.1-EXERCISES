# a program to recommend a vacation event according to season
season=input("enter season(summer or winter):") #ask user to enter season
season=season.lower() #print  season in lowercase
activity_preference=input("enter activity preference(relaxation or adventure)") #ask user to enter activity preference
activity_preference=activity_preference.lower() #prints activity preference in lowercase
if season=="summer": #recommendations for summer
    if activity_preference== "relaxation":
        print("recommendation:Kihunguro")
    if activity_preference== "adventure":
        print("recommendation:Nyeri")
elif season=="winter": #recommendations for winter
    if activity_preference== "relaxation":
        print("recommendation:Nairobi")
    if activity_preference== "adventure":
        print("recommendation:Australia")
else:
        print("stay at home")