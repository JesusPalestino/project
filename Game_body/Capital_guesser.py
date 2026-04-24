import State_capitals #the import has all the states and their capitals in a dictionary 
lyst = [] #this is at the end we can tell them what state's capitals you got correct
score = 0 
for state, capital in State_capitals.States_Capitals.items(): 
    #using a for loop for two reasons one is to get both state and capitals at once 
    #and to have it so the user input would become blank for each loop
    user_input = input(f"Enter a capital of {state} or (enter 'done'): ")
    if user_input == capital:
        score+=1
        lyst.append(state)
        print(f"you have a score of {score}")
        var = open("contriesguess.csv","w")
        var.write(f"{state},{capital}\n")
    elif user_input == "done":
         print(f"you finished a total score of {score} and were able to name these state's capitals {lyst}")
         break 


