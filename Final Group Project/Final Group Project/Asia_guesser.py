import Asia

#name different contries from different continents
continents=["Asia","Europe","South America","North America","Australia","Africa"]
user_input=input(f"Pick what continent you want to do {continents}: ")
user_input_2=input("Please enter if you want to do the countries or capitals: ")
countries_guessed=[]
done=False
total=0
if (user_input=="Asia" or user_input=="asia") and (user_input_2=="countries" or user_input_2=="Countries"):
    while not done:
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
if (user_input=="Asia" or user_input=="asia") and (user_input_2=="capitals" or user_input_2=="Capitals"):
    while not done:
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