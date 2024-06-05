season=input("enter season(summer or winter):")
season=season.lower()
activity_preference=input("enter activity preference(relaxation or adventure)")
activity_preference=activity_preference.lower()
if season=="summer":
    if activity_preference== "relaxation":
        print("recommendation:Kihunguro")
    if activity_preference== "adventure":
        print("recommendation:Nyeri")
elif season=="winter":
    if activity_preference== "relaxation":
        print("recommendation:Nairobi")
    if activity_preference== "adventure":
        print("recommendation:Australia")
else:
        print("stay at home")