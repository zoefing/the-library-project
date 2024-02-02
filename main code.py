import random
import json
from datetime import datetime, timedelta

# read from the JSON file
with open("library_hours.json","r") as json_file:
    library_hours = json.load(json_file)

# set current time
now = datetime.now()
current_time = now.strftime("%H:%M")

# referenced the world wide web to figure out how to set the params for this
def get_user_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input. Please try again.")

# chooses a random place based on the library
def choose_random_place(library_name):
    # if the library chosen is neilson
    if library_name.lower() in ["neilson library","neilson", "n"]:
        random_floor = f"floor {random.randint(0,4)}"
        return random_floor
    
    # if the library chosen is jotsen
    elif library_name.lower() in ["jotsen library", "jotsen", "j"]:
        area = ["a listenting booth","the first floor study area", "the second floor study area"]
        random_area = random.choice(area)
        return random_area
    
    # if the library chosen is hillyer
    elif library_name.lower() in ["hillyer library","hillyer", "h"]:   
        area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
        random_area = random.choice(area)
        return random_area
    
    # if the library chosen is the alumni gym
    elif library_name.lower() in ["the alumni gym","alumni gym", "alumni","gym", "ag"]:   
        random_floor = f"floor {random.randint(1,3)}"
        return random_floor

def options(option):
    library = ["Neilson", "Josten", "Hillyer", "Alumni Gym"]
    
    # if option one is chosen - specific library
    if option.lower() in ["option one", "option 1", "one", "1"]:
        which_library = get_user_input("What library would you like to go to? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ", ["neilson", "n", "josten", "j", "hillyer", "h", "alumni gym", "alumni", "gym", "ag"])
        if which_library in ["neilson", "n"]:
            library_name = "Neilson Library"
        elif which_library in ["josten", "j"]:
            library_name = "Jotsen Library"
        elif which_library in ["hillyer", "h"]:
            library_name = "Hillyer Library"
        elif which_library in ["alumni gym", "ag"]:
            library_name = "the Alumni Gym"
        result = library_name
        return result
    
    # if option two is chosen - closest library
    elif option.lower() in ["option two", "option 2", "two", "2"]:
        closest_library = get_user_input("What is the closest library to you? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ", ["neilson", "n", "josten", "j", "hillyer", "h", "alumni gym", "alumni", "gym", "ag"])
        if closest_library in ["neilson", "n"]:
            library_name = "Neilson Library"
        elif closest_library in ["josten", "j"]:
            library_name = "Jotsen Library"
        elif closest_library in ["hillyer", "h"]:
            library_name = "Hillyer Library"
        elif closest_library in ["alumni gym", "ag"]:
            library_name = "the Alumni Gym"
        result = library_name
        return result
    
    # if option three is chosen - random library
    elif option.lower() in ["option three", "option 3", "three", "3"]:
        library_name = random.choice(library)
        return library_name


def main():
    # define current day
    current_day = now.strftime("%A")
    if now.hour < 5:
        # if it is before 5 AM, consider it part of the night of the previous day
        current_day = (now - timedelta(days=1)).strftime("%A")

    # midnight to 4 AM
    if 0 <= now.hour < 4:
        time = "late at night"
    # 5 AM to 7  AM
    elif 5 <= now.hour < 7:
        time = "early in morning"
    # 7 AM to 12 PM
    elif 7 <= now.hour < 12:
        time = "the morning"
    # 12 PM to 6 PM
    elif 12 <= now.hour < 18:
        time = "the afternoon"
    # 6 PM to 9 PM
    elif 18 <= now.hour < 21:
        time = "the evening"
    # any time between 9 PM and midnight
    else:
        time = "the night"
    
    print(f"It is {time} on {current_day}")

    if current_day in ["Monday", "Tuesday","Wednesday", "Thursday","Friday"]:
        # between 7 and 10 AM
        if 7 <= now.hour < 10:
            
            # asks if user has had breakfast or brunch
            got_breakfast_or_brunch = get_user_input("Did you already get breakfast/brunch? ",
                                                    ["yes", "y",
                                                    "no", "n"])
            
            # if user has not had breakfast or brunch
            if got_breakfast_or_brunch.lower() in ["no","n"]:
                
                # ask if user is planning on getting breakfast or brunch soon
                getting_breakfast_or_brunch = get_user_input("Are you planning on getting breakfast/brunch soon? ",
                                                            ["yes", "y",
                                                            "no", "n"])
                
                # if user is planning on getting breakfast or brunch soon    
                if getting_breakfast_or_brunch.lower() in ["yes","y"]:
                    opinion_on_library = get_user_input("Do you have a specific library in mind after you get breakfast/brunch (Option 1)? "
                                                    "Or do you just want to go to the closest library (Option 2)? "
                                                    "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                    option = opinion_on_library
                    library_name = options(option)
                    print(f"After breakfast/brunch, go to {choose_random_place(library_name)} of {library_name}")
                
                # otherwise
                else:
                    # if user is not planning on getting breakfast or brunch soon
                    if getting_breakfast_or_brunch.lower() in ["no","n"]:
                        opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                    "Or do you just want to go to the closest library (Option 2)? "
                                                    "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
           
            # otherwise            
            else:
                # if user has had breakfast or brunch
                if got_breakfast_or_brunch in ["yes","y"]:
                    opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                        "Or do you just want to go to the closest library (Option 2)? "
                                                        "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                    option = opinion_on_library
                    library_name = options(option)
                    print(f"Go to {choose_random_place(library_name)} of {library_name}")
        
        # between 10 AM and 3 PM
        elif 10 <= now.hour < 15:
            # asks if user has had lunch
            got_lunch = get_user_input("Did you already get lunch? ",
                                        ["yes", "y",
                                        "no", "n"])
            
            
            # if user has not had lunch    
            if got_lunch.lower() in ["no","n"]:
                
                # ask if user is planning on getting lunch soon
                getting_lunch = get_user_input("Are you planning on getting lunch soon? ",
                                                ["yes", "y",
                                                "no", "n"])
                
                # if user is planning on getting lunch soon
                if getting_lunch.lower() in ["yes","y"]:
                    
                    # between 11 AM and 2 PM 
                    if 11 <= now.hour < 14:
                        
                        # asks if user ordered/can order lunch from the neilson cafe
                        neilson_lunch = get_user_input("Can you/did you order lunch from the Neilson cafe? ",
                                                        ["yes", "y",
                                                        "no", "n"])
                        
                        # if user can/did order lunch from the neilson cafe
                        if neilson_lunch.lower() in ["yes","y"]:
                            library_name = "Neilson"
                            print(f"Get your food, and then go to {choose_random_place(library_name)} of {library_name}")
                        
                        # otherwise    
                        else:
                            # if user cannot/did not order lunch from the neilson cafe
                            if neilson_lunch.lower() in ["no","n"]:
                                opinion_on_library = get_user_input("Do you have a specific library in mind after you get lunch (Option 1)? "
                                                                "Or do you just want to go to the closest library (Option 2)? "
                                                                "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                                option = opinion_on_library
                                library_name = options(option)
                                print(f"After lunch, go to {choose_random_place(library_name)} of {library_name}")
                    
                    # otherwise (if neilson lunch not open)
                    else:
                        opinion_on_library = get_user_input("Do you have a specific library in mind after you get lunch (Option 1)? "
                                                                "Or do you just want to go to the closest library (Option 2)? "
                                                                "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                        option = opinion_on_library
                        library_name = options(option)
                        print(f"After lunch, go to {choose_random_place(library_name)} of {library_name}")
                        
            # otherwise        
            else:
                # if user has had lunch
                if got_lunch in ["yes","y"]:
                    opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                        "Or do you just want to go to the closest library (Option 2)? "
                                                        "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])

                    option = opinion_on_library
                    library_name = options(option)
                    print(f"Go to {choose_random_place(library_name)} of {library_name}")
        
        # between 4:30 PM and 10 PM    
        elif 16 <= now.hour < 22 or (now.hour == 22 and now.minute <= 30):
            
            # asks if user has had dinner
            got_dinner = get_user_input("Did you already get dinner? ",
                                        ["yes", "y",
                                        "no", "n"])
            
            # if user has not had dinner        
            if got_dinner.lower() in ["no","n"]:
                
                # ask if user is planning on getting dinner soon
                getting_dinner = get_user_input("Are you planning on getting dinner soon? ",
                                                ["yes", "y",
                                                "no", "n"])

                # if user is planning on getting dinner soon
                if getting_dinner.lower() in ["yes","y"]:
                    opinion_on_library = get_user_input("Do you have a specific library in mind after you get dinner (Option 1)? "
                                                        "Or do you just want to go to the closest library (Option 2)? "
                                                        "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                    option = opinion_on_library
                    library_name = options(option)
                    print(f"After dinner, go to {choose_random_place(library_name)} of {library_name}")     
                 
                # otherwise           
                else:                   
                    # if user is not planning on getting dinner soon
                    if getting_dinner.lower() in ["no", "n"]:
                        opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                            "Or do you just want to go to the closest library (Option 2)? "
                                                            "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])

                        option = opinion_on_library
                        library_name = options(option)
                        print(f"Go to {choose_random_place(library_name)} of {library_name}")
            
            #otherwise                
            else:   
                # if user has had dinner
                if got_dinner in ["yes","y"]:
                    opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                        "Or do you just want to go to the closest library (Option 2)? "
                                                        "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])

                    option = opinion_on_library
                    library_name = options(option)
                    print(f"Go to {choose_random_place(library_name)} of {library_name}")
        
    elif current_day in ["Saturday", "Sunday"]:
        # between 7 AM and 2 PM
        if 7 <= now.hour < 14:
            
            # ask if user has had breakfast or brunch or lunch
            got_breakfast_or_brunch = get_user_input("Did you already get breakfast/brunch/lunch? ",
                                                    ["yes", "y",
                                                    "no", "n"])
            
            # if user has not had breakfast or brunch or lunch
            if got_breakfast_or_brunch.lower() in ["no","n"]:
                if 11 <= now.hour < 14:
                    
                    # ask if user is planning on getting breakfast or brunch or lunch soon
                    getting_weekend_afternoon_meal = get_user_input("Are you planning on getting breakfast/brunch/lunch soon? ",
                                                                    ["yes", "y",
                                                                    "no", "n"])
                    
                    # if user is planning on getting breakfast or brunch or lunch soon
                    if getting_weekend_afternoon_meal in ["yes","y"]:
                        neilson_brunch = get_user_input("Do you want to/did you order brunch from the Neilson cafe? ",
                                                        ["yes", "y",
                                                        "no", "n"])
                    
                        # if user can/did order brunch from the neilson cafe
                        if neilson_brunch.lower() in ["yes","y"]:
                            library_name = "Neilson"
                            print(f"Get your food, and then go to {choose_random_place(library_name)} of {library_name}")

                        # otherwise
                        else:
                            # if user cannot/did not order brunch from the neilson cafe
                            if neilson_brunch.lower() in ["no","n"]:
                                opinion_on_library = get_user_input("Do you have a specific library in mind after you get breakfast/brunch (Option 1)? "
                                                                    "Or do you just want to go to the closest library (Option 2)? "
                                                                    "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                                option = opinion_on_library
                                library_name = options(option)
                                print(f"After breakfast/brunch/lunch, go to {choose_random_place(library_name)} of {library_name}")

                    # otherwise
                    else: 
                        # if user is not planning on getting breakfast or brunch or lunch soon
                        if getting_weekend_afternoon_meal in ["no","n"]:
                            opinion_on_library = get_user_input("Do you have a specific library in mind after you get breakfast/brunch (Option 1)? "
                                                                "Or do you just want to go to the closest library (Option 2)? "
                                                                "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                            option = opinion_on_library
                            library_name = options(option)
                            print(f"After breakfast/brunch/lunch, go to {choose_random_place(library_name)} of {library_name}")
            
            # otherwise
            else:
                # if user has had breakfast or brunch or lunch
                if got_breakfast_or_brunch in ["yes","y"]:
                    opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                        "Or do you just want to go to the closest library (Option 2)? "
                                                        "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])

                    option = opinion_on_library
                    library_name = options(option)
                    print(f"Go to {choose_random_place(library_name)} of {library_name}") 
        
        # between 4:30 PM and 10 PM
        elif 16 <= now.hour < 22 and (now.hour != 22 or now.minute < 30):
            # asks if user has had dinner
            got_dinner = get_user_input("Did you already get dinner? ",
                                        ["yes", "y",
                                        "no", "n"])
            
            # if user has not had dinner
            if got_dinner.lower() in ["no","n"]:
                
                # ask if user is planning on getting dinner soon
                getting_dinner = get_user_input("Are you planning on getting dinner soon? ",
                                                ["yes", "y",
                                                "no", "n"])
                
                # if user is planning on getting dinner soon
                if getting_dinner.lower() in ["yes","y"]:
                    opinion_on_library = get_user_input("Do you have a specific library in mind after you get dinner (Option 1)? "
                                                        "Or do you just want to go to the closest library (Option 2)? "
                                                        "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                    option = opinion_on_library
                    library_name = options(option)
                    print(f"After dinner, go to {choose_random_place(library_name)} of {library_name}")     
                
                # otherwise
                else:
                    # if user is not planning on getting dinner soon
                    if getting_dinner.lower() in ["no","n"]:
                        opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                            "Or do you just want to go to the closest library (Option 2)? "
                                                            "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                            
                        option = opinion_on_library
                        library_name = options(option)
                        print(f"Go to {choose_random_place(library_name)} of {library_name}")          
            
            # otherwise            
            else:
                # if user has had dinner
                if got_dinner.lower() in ["yes","y"]:
                    opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                        "Or do you just want to go to the closest library (Option 2)? "
                                                        "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])

                    option = opinion_on_library
                    library_name = options(option)
                    print(f"Go to {choose_random_place(library_name)} of {library_name}")
        
        # otherwise (does not fit into cases above)            
        else:
            opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                "Or do you just want to go to the closest library (Option 2)? "
                                                "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
            option = opinion_on_library
            library_name = options(option)
            print(f"Go to {choose_random_place(library_name)} of {library_name}") 
                        
if __name__ == "__main__":
    main()