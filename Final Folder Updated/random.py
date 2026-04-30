#****Disclaimer used AI only for the timer parts and for the writing the countries in the csv file, and class!!*****

import Asia #imported from the asia code i made in a separate folder
import Europe #same as asia but different folder with different content
import time #imported to make the timer work
import Central_american_capitals as Central_american_capitals #the import has all the states and their capitals in a dictionary
import australia_capitals 
import State_capitals
State_capitals.States_Capitals
#name different countries from different continents
game_number=int(input("Enter game number: "))
continents=["Asia","Europe","South America","North America","Australia","Africa","U.S.A","Central America"] 
user_input=input(f"Pick what continent you want to do {continents}: ") 
user_input_2=input("Please enter if you want to do the countries or capitals or states or territory: ")
try:
    my_time=int(input("Please enter the time in seconds: ")) #AI
    end_time=time.time()+my_time    #AI
except ValueError:
    print("You typed the time in wrong try again!")    
countries_guessed=[]

#Joseph's code


done=False
total=0

#Asia and Europe works
def asia_countries(): #this function takes the import from asia and allows the user to guess asia countries
    done=False
    total=0
    if (user_input.lower()=="asia") and (user_input_2.lower()=="countries"): #for if the user picks asia countries
        while not done:
            remaining=int(end_time-time.time()) 
            if remaining<=0: #when the timer hits zero the code stops
                print("Times UP!")
                break

            user_picking_countries=input("Enter a Asian country: ").lower()
                
            if user_picking_countries=="done":       
                done=True
            elif user_picking_countries in Asia.asia_capitals.keys() and user_picking_countries not in countries_guessed:
                total+=1
                countries_guessed.append(user_picking_countries)
            else:
                total+=0
            print(f'{total}/{len(Asia.asia_capitals)}')
            print(countries_guessed)
            print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer
asia_countries()

def asia_capitals(): #this function takes the asia import and allows the user to guess asia capitals
    done=False
    total=0
    if (user_input.lower()=="asia") and (user_input_2.lower()=="capitals"): #for if the user picks asia capital
        while not done:
            remaining=int(end_time-time.time())
            if remaining<=0:
                print("Times UP!")
                break
            user_picking_countries=input("Enter a Asian capital: ").lower()
                
            if user_picking_countries=="done":
                done=True
            elif user_picking_countries in Asia.asia_capitals.values() and user_picking_countries not in countries_guessed:
                total+=1
                countries_guessed.append(user_picking_countries)
            else:
                total+=0
            print(f'{total}/{len(Asia.asia_capitals)}')
            print(countries_guessed)
            print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer
asia_capitals()

def europe_countries(): #this function takes the europe import and allows the user to guess european countries
    done=False
    total=0 
    if (user_input.lower()=="europe") and (user_input_2.lower()=="countries"): #for if the user picks europe countries
        while not done:
            remaining=int(end_time-time.time())
            if remaining<=0:
                print("Times UP!")
                break
            user_picking_countries=input("Enter a European country: ").lower()
                
            if user_picking_countries=="done":
                done=True
            elif user_picking_countries in Europe.europe_capitals.keys() and user_picking_countries not in countries_guessed: #.keys if for the countries in the code i imported
                total+=1
                countries_guessed.append(user_picking_countries)
            else:
                total+=0
            print(f'{total}/{len(Europe.europe_capitals)}')
            print(countries_guessed)
            print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer
europe_countries()
if (user_input.lower()=="europe") and (user_input_2.lower()=="capitals"): #for if the user picks europe countries, It takes the europe import and allows the user to guess european capitals
    while not done:
        remaining=int(end_time-time.time())
        if remaining<=0:
            print("Times UP!")
            break
        user_picking_countries=input("Enter a European capital: ").lower()
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Europe.europe_capitals.values() and user_picking_countries not in countries_guessed: #.values is for the capitals in my code i imported
            total+=1
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Europe.europe_capitals)}')
        print(countries_guessed)
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer


#Jesus code
#Central America Works
elif (user_input.lower()=="central america" and user_input_2.lower()=="capitals"): #this elif statement allows the user to guess central america capitals from the centrals america import

    for country, capital in Central_american_capitals.centralamerica_capitals.items(): 
        user_picking_capitals = input(f"Enter a capital of {country} or (enter 'done'): ").lower()
        remaining=int(end_time-time.time()) 

        if remaining<=0: #when the timer hits zero the code stops
            print("Times UP!")
            break
    
        #using a for loop for two reasons one is to get both state and capitals at once 
        #and to have it so the user input would become blank for each loop

        elif user_picking_capitals == capital.lower() and user_picking_capitals not in countries_guessed:
            total+=1
            countries_guessed.append(user_picking_capitals)
            print(f"you have a score of {total}")
        elif user_picking_capitals=="done":
            print(f"You finished with a total score of {total}. You named these countries: {countries_guessed}")
            break
        print(f'{total}/{len(Central_american_capitals.centralamerica_capitals)}')
        print(countries_guessed)
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer
elif user_input.lower()=="central america" and user_input_2.lower()=="countries": #this elif takes the central america import and allows the user to guess the countries
    for country in Central_american_capitals.centralamerica_capitals.keys():
        user_picking_country=input("Enter a Central American country or 'done': ").lower()
        remaining=int(end_time-time.time()) 

        if remaining<=0: #when the timer hits zero the code stops
            print("Times UP!")
            break
        if user_picking_country==country.lower() and user_picking_country not in countries_guessed:
            total+=1
            countries_guessed.append(user_picking_country)
            print(f"You have a score of {total}")

        elif user_picking_country=="done":
            print(f"You finished with a total score of {total}. You named these countries: {countries_guessed}")
            break
        print(f'{total}/{len(Central_american_capitals.centralamerica_capitals)}')
        print(countries_guessed)
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer

#Joseph's code

elif (user_input.lower()=="australia" and user_input_2.lower()=="capitals"): #This elif takes the australia import and allows the user to guess australian capitals

    for country, capital in australia_capitals.australia_capitals.items(): 
        user_picking_capitals_for_australia = input(f"Enter a capital of {country} or (enter 'done'): ").strip().lower()
        remaining=int(end_time-time.time()) 

        if remaining<=0: #when the timer hits zero the code stops
            print("Times UP!")
            break
    
        #using a for loop for two reasons one is to get both state and capitals at once 
        #and to have it so the user input would become blank for each loop
        if user_picking_capitals_for_australia=="done":
            print(f"You finished with a total score of {total}. You named these countries: {countries_guessed}")
            break
        elif user_picking_capitals_for_australia == capital.lower() and user_picking_capitals_for_australia not in countries_guessed:
            total+=1
            countries_guessed.append(user_picking_capitals_for_australia)
            print(f"you have a score of {total}")

        print(f'{total}/{len(australia_capitals.australia_capitals)}')
        print(countries_guessed)
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer



elif user_input.lower()=="australia" and user_input_2.lower()=="territory": #This elif allows the user to guess the territories from the australia import
    while not done:
        
            user_guess=input("Enter a Australian Territories or 'done': ").strip().lower()
            remaining=int(end_time-time.time())

            if remaining<=0: #when the timer hits zero the code stops
                print("Times UP!")
                break
            if user_guess=="done":
                done=True
                print(f"You finished with a total score of {total}. You named these countries: {countries_guessed}")
                break
            for territories in australia_capitals.australia_capitals.keys():
                if user_guess==territories.lower() and user_guess not in countries_guessed:
                    total+=1
                    countries_guessed.append(user_guess)
                    print(f"You have a score of {total}")


            print(f'{total}/{len(australia_capitals.australia_capitals)}')
            print(countries_guessed)
            print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer



#Levi's Code, with some of Joseph's so it would work with the rest of the code
#U.S.A works
elif user_input.lower()=="u.s.a" and user_input_2.lower()=="capitals": #This elif takes the state_capitals import and allows the user to guess capitals for the USA
    for state, capital in State_capitals.States_Capitals.items():
        remaining=int(end_time-time.time()) 

        if remaining<=0: #when the timer hits zero the code stops
            print("Times UP!")
            break
       #here was another attempt of doing a closeness thing
        closeness = 0
        length_of_capital= len(capital)
        #---------------------------------
        #print(length_of_capital)
        user_picking_countries = input(f"Enter a capital of {state} or (enter 'done'): ").lower()
        if user_picking_countries == capital.lower():
            countries_guessed.append(user_picking_countries)
            total+=1
            
        elif user_picking_countries == "done":
            break
        elif user_picking_countries!= capital and user_picking_countries!= "done":
            for x in user_picking_countries:
                for y in capital.lower():
                    if x==y:
                        closeness+=1
                        
                if closeness/len(capital)==.8:
                    user_picking_countries = ("you were close to the answer, please try again: ")
        print(f'{total}/{len(State_capitals.States_Capitals)}')
        print(countries_guessed)
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer
elif user_input.lower()=="u.s.a" and user_input_2.lower()=="states": #this takes the state_capitals import and allows the user to guess the states in the USA
    while not done:
        user_picking_states=input("Enter a State: ").lower()
        remaining=int(end_time-time.time()) 

        if remaining<=0: #when the timer hits zero the code stops
            print("Times UP!")
            break
        if user_picking_states=="done" or len(countries_guessed)==len(State_capitals.States_Capitals):
            done=True
        elif user_picking_states not in countries_guessed: #.keys if for the countries in the code i imported
            for state in State_capitals.States_Capitals.keys():
                if user_picking_states==state.lower():
                    total+=1
                    countries_guessed.append(user_picking_states)
        else:
            total+=0
        print(f'{total}/{len(State_capitals.States_Capitals)}')
        print(countries_guessed)
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer

#South America works
elif user_input.lower() == "south america" and user_input_2.lower()=="capitals": #This elif takes the south america import and allows the user to guess the capitals of south america

    for country_South_America, capital_South_America in State_capitals.south_american_capitals.items():

        user_picking_countries = input(f"Enter the capital of {country_South_America} or (enter 'done'): ").lower()
        remaining=int(end_time-time.time()) 

        if remaining<=0: #when the timer hits zero the code stops
            print("Times UP!")
            break
        if user_picking_countries == capital_South_America.lower() and user_picking_countries not in countries_guessed:
            total+=1
            countries_guessed.append(user_picking_countries)
            print(f"you have a score of {total}")
        elif user_picking_countries == "done":
            print(f"you total score is {total}")
            break
        print(f'{total}/{len(State_capitals.south_american_capitals)}')
        print(countries_guessed)
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer
elif user_input.lower()=="south america" and user_input_2.lower()=="countries": #This elif takes the south america import and allows the user to guess south american countries
    while not done:
        user_picking_country=input("Enter a country: ").lower()
        remaining=int(end_time-time.time()) 

        if remaining<=0: #when the timer hits zero the code stops
            print("Times UP!")
            break
        if user_picking_country=="done" or len(countries_guessed)==len(State_capitals.south_american_capitals):
            done=True
        elif user_picking_country not in countries_guessed: #.keys if for the countries in the code i imported
            for countries in State_capitals.south_american_capitals.keys():
                if user_picking_country==countries.lower():
                    total+=1
                    countries_guessed.append(user_picking_country)

        else:
            total+=0
        print(f'{total}/{len(State_capitals.south_american_capitals)}')
        print(countries_guessed)
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer

#africa works
elif user_input.lower() == "africa" and user_input_2.lower()=="capitals": #This elif takes the state capital import and allows the user to guess african countries
    while not done:
        user_picking_africa_capitals = input(f"Enter the capitals of Africa or (enter 'done'): ").lower()
        remaining=int(end_time-time.time()) 

        if remaining<=0: #when the timer hits zero the code stops
            print("Times UP!")
            break
        if user_picking_africa_capitals == "done" or len(countries_guessed)==len(State_capitals.african_capitals):
            done=True
        elif user_picking_africa_capitals not in countries_guessed:
            for capitals in State_capitals.african_capitals.values():
                if user_picking_africa_capitals==capitals.lower():
                    total+=1
                    countries_guessed.append(user_picking_africa_capitals)


        print(f'{total}/{len(State_capitals.african_capitals)}')
        print(countries_guessed)
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer
elif user_input.lower()=="africa" and user_input_2.lower()=="countries": #This elif takes the state capital import and allows the user to guess the africa countries
    while not done:
        user_picking_country=input("Enter a African Country: ").lower()
        remaining=int(end_time-time.time()) 

        if remaining<=0: #when the timer hits zero the code stops
            print("Times UP!")
            break

        if user_picking_country=="done" or len(countries_guessed)==len(State_capitals.african_capitals): #for if the user wants to stop or if they cant guess anymore
            done=True
        elif user_picking_country not in countries_guessed: #.keys if for the countries in the code i imported
            for countries in State_capitals.african_capitals.keys():
                if user_picking_country==countries.lower():
                    total+=1
                    countries_guessed.append(user_picking_country)
        else:
            total+=0
        print(f'{total}/{len(State_capitals.african_capitals)}')
        print(countries_guessed)
        print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer


#used ai for the class, the one i wrote didnt work and needed help on how to make it work: Joseph's Code
class NorthAmericaContinent: #this class takes the state capitals import and allows the user to guess capitals and countries of north america
    def __init__(self,mode,end_time): #to know what is going to be in the class
        self.mode=mode
        self.end_time=end_time
        self.total=0
        self.guessed=[]
        self.data=State_capitals.north_american_capitals

    def play(self): #so you can play the game
        while True:
            remaining=int(end_time-time.time()) 

            if remaining<=0: #when the timer hits zero the code stops
                print("Times UP!")
                break

            if self.mode=="countries":
                guess_north_america_countries=input("Enter a North America Country or type done: ").lower()
            else:
                guess_north_america_countries=input("Enter a capital of and North American country or type done: ").lower()

            if guess_north_america_countries=="done":
                break
            if guess_north_america_countries in self.guessed:
                print("You already guessed that!")
                continue
            if self.mode=="countries":
                for country in self.data.keys():
                    if guess_north_america_countries==country.lower():  
                        self.total+=1
                        self.guessed.append(guess_north_america_countries)
                        print(f"You have a score of {self.total}")
                        break

            else:
                for country,capital in self.data.items():
                    if guess_north_america_countries==capital.lower():
                        self.total+=1
                        self.guessed.append(guess_north_america_countries)
                        print(f"You have a score of {self.total}")
                        break
         
            print(f'{self.total}/{len(self.data)}')
            print(self.guessed)
            print(f"Time remaining: {remaining} seconds") #prints the time that is left on the timer
    def __str__(self):
        return str(self.guessed)
if user_input.lower() == "north america": #This if takes the class above and allows the user to see what they are inputting
    game = NorthAmericaContinent(user_input_2.lower(), end_time)
    game.play()
    total = game.total
    countries_guessed = game.guessed
    game.__str__()

#This takes all the info that the user types in and puts it to a csv file
import csv
import os

def save_game(game_number, countries_guessed):
    filename="Countriesguessed.csv"
    games={}


    if os.path.exists(filename):
        with open (filename,'r',encoding='utf-8') as file:
            reader=csv.reader(file)
            headers=next(reader,None)
            if headers:
                for col_index, header in enumerate(headers):
                    game_num=int(header.replace("Game ", "").replace(" Guess", ""))
                    games[game_num]=[]
                for row in reader:
                    for col_index, value in enumerate(row):
                        if value:
                            game_num=int(headers[col_index].replace("Game ", "").replace(" Guess", ""))
                            games[game_num].append(value)
    games[game_number]=countries_guessed

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer=csv.writer(file)
        sorted_games=sorted(games.keys())
        writer.writerow([f"Game {g} Guess" for g in sorted_games])
        max_rows=max(len(games[g]) for g in sorted_games)
        for i in range(max_rows):
            row=[]
            for g in sorted_games:
                row.append(games[g][i] if i < len(games[g]) else "")
            writer.writerow(row)
save_game(game_number, countries_guessed)