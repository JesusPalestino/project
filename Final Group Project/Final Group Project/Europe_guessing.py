import Europe
import time

my_time=int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    seconds=x%60
    minutes=int(x/60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
    time.sleep(1)
print("Times UP!")

continents=["Asia","Europe","South America","North America","Australia","Africa"]
user_input=input(f"Pick what continent you want to do {continents}: ")
user_input_2=input("Please enter if you want to guess the countries or capitals: ")
done=False
total=0
countries_guessed=[]
if (user_input=="Europe" or user_input=="europe") and (user_input_2=="countries" or user_input_2=="Countries"):
    while not done:
        user_picking_countries=input("Enter a European country: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Europe.europe_capitals.keys() and user_picking_countries not in countries_guessed:
            total+=1
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Europe.europe_capitals)}')
        print(countries_guessed)
if (user_input=="Europe" or user_input=="europe") and (user_input_2=="capitals" or user_input_2=="Capitals"):
    while not done:
        user_picking_countries=input("Enter a European capital: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Europe.europe_capitals.values() and user_picking_countries not in countries_guessed:
            total+=1
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Europe.europe_capitals)}')
        print(countries_guessed)




