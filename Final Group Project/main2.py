#****Disclaimer used AI only for the timer parts!!*****

import Asia #imported from the asia code i made in a seperate folder
import Europe #same as asia but different folder with different content
import time #imported to make the timer work
#name different contries from different continents
continents=["Asia","Europe","South America","North America","Australia","Africa"] 
user_input=input(f"Pick what continent you want to do {continents}: ") 
user_input_2=input("Please enter if you want to do the countries or capitals: ")

my_time=int(input("Please enter the time in seconds: ")) #AI
end_time=time.time()+my_time    #AI
countries_guessed=[]

done=False
total=0
if (user_input=="Asia" or user_input=="asia") and (user_input_2=="countries" or user_input_2=="Countries"): #for if the user picks asia countries
    while not done:
        remaining=int(end_time-time.time()) 
        if remaining<=0: #when the timer hits zero the code stops
            print("Times UP!")
            break
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer
        user_picking_countries=input("Enter a Asian country: ")
            
        if user_picking_countries=="done":       
            done=True
        elif user_picking_countries in Asia.asia_capitals.keys() and user_picking_countries not in countries_guessed:
            total+=1
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Asia.asia_capitals)}')
        print(countries_guessed)
        new_file=open("Countriesguessed.csv","w")
        new_file.write(str(countries_guessed)+'\n')
        new_file.close()

if (user_input=="Asia" or user_input=="asia") and (user_input_2=="capitals" or user_input_2=="Capitals"): #for if the user picks asia capital
    while not done:
        remaining=int(end_time-time.time())
        if remaining<=0:
            print("Times UP!")
            break
        print(f"Time remaining: {remaining} seconds")
        user_picking_countries=input("Enter a Asian capital: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Asia.asia_capitals.values() and user_picking_countries not in countries_guessed:
            total+=1
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Asia.asia_capitals)}')
        print(countries_guessed)
        new_file=open("Countriesguessed.csv","w")
        new_file.write(str(countries_guessed)+'\n')
        new_file.close()

if (user_input=="Europe" or user_input=="europe") and (user_input_2=="countries" or user_input_2=="Countries"): #for if the user picks europe countries
    while not done:
        remaining=int(end_time-time.time())
        if remaining<=0:
            print("Times UP!")
            break
        print(f"Time remaining: {remaining} seconds")
        user_picking_countries=input("Enter a European country: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Europe.europe_capitals.keys() and user_picking_countries not in countries_guessed: #.keys if for the countries in the code i imported
            total+=1
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Europe.europe_capitals)}')
        print(countries_guessed)
        new_file=open("Countriesguessed.csv","w")
        new_file.write(str(countries_guessed)+'\n')
        new_file.close()
if (user_input=="Europe" or user_input=="europe") and (user_input_2=="capitals" or user_input_2=="Capitals"): #for if the user picks europe countries
    while not done:
        remaining=int(end_time-time.time())
        if remaining<=0:
            print("Times UP!")
            break
        print(f"Time remaining: {remaining} seconds")
        user_picking_countries=input("Enter a European capital: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Europe.europe_capitals.values() and user_picking_countries not in countries_guessed: #.values is for the capitals in my code i imported
            total+=1
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Europe.europe_capitals)}')
        print(countries_guessed)

        new_file=open("Countriesguessed.csv","w")
        new_file.write(str(countries_guessed)+'\n')
        new_file.close()