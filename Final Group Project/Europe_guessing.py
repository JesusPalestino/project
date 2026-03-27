import Europe



continents=["Asia","Europe","South America","North America","Australia","Africa"]
user_input=input(f"Pick what continent you want to do {continents}: ")
done=False
total=0
while not done:
    if user_input=="Europe" or user_input=="europe":
        user_picking_countries=input("Enter a European country: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Europe.europe_countries:
            total+=1
        else:
            total+=0
        print(f'{total}/{len(Europe.europe_countries)}')