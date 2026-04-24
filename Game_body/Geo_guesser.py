import State_capitals
State_capitals.States_Capitals
class Closeness:
    def __int__(self, close_input):
        self._close_input = close_input

    def get_close_input(self):
        for q in user_input:
            for t in capital:
                if x==y:
                    score+=1



var = open("contriesguess.csv","w")

correct = []
not_correct = ""
user_input = ""
score = 0
choose = input("you have the choose to gues the capitals of (U.S.A, North America, South America, Europe, Asia, Africa: ")
if choose =="U.S.A":
    for state, capital in State_capitals.States_Capitals.items():
        closeness = 0
        length_of_capital= len(capital)
        #print(length_of_capital)
        user_input = input(f"Enter a capital of {state} or (enter 'done'): ")
        if user_input == capital:
            score+=1
            correct.append(state)
            print(f"you have a score of {score}")
            
            var.write(f"{state},{capital}\n")
        elif user_input == "done":
            print(f"you total score is {score}")
            break
        elif user_input!= capital and user_input!= "done":
            for x in user_input:
                for y in capital:
                    if x==y:
                        closeness+=1
                        
                if closeness/len(capital)==.8:
                    user_input = ("you were close to the answer, please try again: ")


            
elif choose == "North America":
    for Countries_Of_North_America, Capitals_of_North_America in State_capitals.north_american_capitals.items():
        user_input = input(f"Enter the capital of {Countries_Of_North_America} or (enter 'done'): ")
        if user_input == Capitals_of_North_America:
            score+=1
            correct.append(Countries_Of_North_America)
            var.write(f"{Countries_Of_North_America},{Capitals_of_North_America}\n")
            print(f"you have a score of {score}")
        elif user_input == "done":
            print(f"you total score is {score}")
            break
elif choose == "Europe":
    for EU_country, EU_capitals in State_capitals.european_capitals.items():
        user_input = input(f"Enter the capital of {EU_country} or (enter 'done'): ")
        if user_input == EU_capitals:
            score+=1
            correct.append(EU_country)
            var.write(f"{EU_country},{EU_capitals}\n")
            print(f"you have a score of {score}")
        elif user_input == "done":
            print(f"you total score is {score}")
            break
    
elif choose == "South America":
    for country_South_America, capital_South_America in State_capitals.south_american_capitals.items():
        user_input = input(f"Enter the capital of {country_South_America} or (enter 'done'): ")
        if user_input == capital_South_America:
            score+=1
            correct.append(country_South_America)
            print(f"you have a score of {score}")
            var.write(f"{country_South_America},{capital_South_America}\n")
        elif user_input == "done":
            print(f"you total score is {score}")
            break

elif choose == "Africa":
    for africa_countries, africa_capitals in State_capitals.african_capitals.items():
        user_input = input(f"Enter the capital of {africa_countries} or (enter 'done'): ")
        if user_input == africa_capitals:
            score+=1
            correct.append(africa_countries)
            var.write(f"{africa_countries},{africa_capitals}\n")
            print(f"you have a score of {score}")
        elif user_input == "done":
            print(f"you total score is {score}")
            break

elif choose == "Asia":
    for Asia_countries, Asia_capitals in State_capitals.asian_capitals.items():
        user_input = input(f"Enter the capital of {Asia_countries} or (enter 'done'): ")
        if user_input == Asia_capitals:
            score+=1
            correct.append(Asia_countries)
            var.write(f"{Asia_countries},{Asia_capitals}\n")
            print(f"you have a score of {score}")
        elif user_input == "done":
            print(f"you total score is {score}")
            break
var.close()
var2= open("contriesguess.csv.csv","r")
print(var2)
