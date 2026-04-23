import Asia
import Europe
import time
import threading


#****Disclaimer I used AI for the timer, and the threading****
print_lock=threading.Lock()
def countdown(end_time):
    while True:

        remaining=int(end_time-time.time()) #for remainging time
        if remaining<=0:
            with print_lock:
                print("\nTimes UP!") #when the timer hits 0 the code stops
            break
        with print_lock:
            print(f"\rTime remaining: {remaining} seconds  ", end="")
        time.sleep(1)

#name different contries from different continents
continents=["Asia","Europe","South America","North America","Australia","Africa"] #for user to pick which continent
user_input=input(f"Pick what continent you want to do {continents}: ")
user_input_2=input("Please enter if you want to do the countries or capitals: ")

my_time=int(input("Please enter the time in seconds: ")) #for the timer in seconds the user wants
end_time=time.time()+my_time

#Start timer thread
timer_thread=threading.Thread(target=countdown, args=(end_time,))
timer_thread.daemon=True
timer_thread.start()

countries_guessed=[]

done=False
total=0
if (user_input.lower()=="Asia" or user_input.lower()=="asia") and (user_input_2.lower()=="countries" or user_input_2.lower()=="Countries"):
    while not done:
        if time.time()>=end_time:
            break
        with print_lock:
            user_picking_countries=input("\nEnter a Asian country: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Asia.asia_capitals.keys() and user_picking_countries not in countries_guessed: 
            total+=1 #line 28 and 29 lets the user to guess the country and the total is to add 1 to the list of numbers 
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Asia.asia_capitals)}') #This print how many countries are left
        print(countries_guessed) #prints the list of countries you guessed correctly
if (user_input.lower()=="Asia" or user_input.lower()=="asia") and (user_input_2.lower()=="capitals" or user_input_2.lower()=="Capitals"):
    while not done:
        with print_lock:
            user_picking_countries=input("\nEnter a Asian country: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Asia.asia_capitals.values() and user_picking_countries not in countries_guessed: #this pulls from the dictionary and takes the values for capitals
            total+=1
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Asia.asia_capitals)}')
        print(countries_guessed)

end_time=time.time()+my_time
done=False
total=0
countries_guessed=[]
if (user_input.lower()=="Europe" or user_input.lower()=="europe") and (user_input_2.lower()=="countries" or user_input_2.lower()=="Countries"):
    while not done:
        if time.time()>=end_time:
            break
        with print_lock:
            user_picking_countries=input("\nEnter a European country: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Europe.europe_capitals.keys() and user_picking_countries not in countries_guessed:
            total+=1
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Europe.europe_capitals)}')
        print(countries_guessed)
if (user_input.lower()=="Europe" or user_input.lower()=="europe") and (user_input_2.lower()=="capitals" or user_input_2.lower()=="Capitals"):
    while not done:
        if time.time()>=end_time:
            break
        with print_lock:
            user_picking_countries=input("\nEnter a European capital: ")
            
        if user_picking_countries=="done":
            done=True
        elif user_picking_countries in Europe.europe_capitals.values() and user_picking_countries not in countries_guessed:
            total+=1
            countries_guessed.append(user_picking_countries)
        else:
            total+=0
        print(f'{total}/{len(Europe.europe_capitals)}')
        print(countries_guessed)