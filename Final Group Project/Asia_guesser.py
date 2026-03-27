import Asia

#name different contries from different continents
continents=["Asia","Europe","South America","North America","Australia","Africa"]
user_input=input(f"Pick what continent you want to do {continents}: ")
done=False
total=0
while not done:
    if user_input=="Asia" or user_input=="asia":
        user_picking_countries=input("Enter a Asian country: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Asia.asia_countries:
            total+=1
        else:
            total+=0
        print(f'{total}/{len(Asia.asia_countries)}')
            

