import random

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
    
    # if option one is chosen
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
    
    # if option two is chosen
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
    
    # if option three is chosen
    elif option.lower() in ["option three", "option 3", "three", "3"]:
        library_name = random.choice(library)
        return library_name


def main():
    library = ["Neilson Library", "Josten Library", "Hillyer Library", "the Alumni Gym"]

    user_input = get_user_input("What day of the week is it? ", ["monday", "m", "mon",
                                                                "tuesday", "tu", "tues",
                                                                "wednesday", "w", "weds",
                                                                "thursday", "th", "thurs", "t",
                                                                "friday", "fri", "f", "saturday",
                                                                "sa", "sat", "sunday",
                                                                "su", "sun", "s"])

    is_it_a_mealtime = get_user_input("Is it currently a mealtime? ",
                                               ["yes", "y",
                                                "no", "n"])
    
    if is_it_a_mealtime.lower() in ["yes","y"]:

    
    
      is_it_breakfast_or_brunch_time = get_user_input("Is it breakfast/brunch time? ",
                                                ["yes", "y",
                                                  "no", "n"])

      if is_it_breakfast_or_brunch_time.lower() in ["yes","y"]:
          got_breakfast_or_brunch = get_user_input("Did you already get breakfast/brunch? ",
                                                ["yes", "y",
                                                  "no", "n"])
          
          if got_breakfast_or_brunch.lower() in ["no","n"]:
              neilson_brunch = get_user_input("Can you/did you order brunch from the Neilson cafe? ",
                                          ["yes", "y",
                                          "no", "n"])

              if neilson_brunch.lower() in ["yes","y"]:
                  library_name = "Neilson"
                  print(f"Get your food, and then go to {choose_random_place(library_name)} of {library_name}")
              
              else:
                  opinion_on_library = get_user_input("Do you have a specific library in mind after you get breakfast/brunch (Option 1)? "
                                                  "Or do you just want to go to the closest library (Option 2)? "
                                                  "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                  option = opinion_on_library
                  library_name = options(option)
                  print(f"After breakfast/brunch, go to {choose_random_place(library_name)} of {library_name}")
          
          else:
              if got_breakfast_or_brunch in ["yes","y"]:
                  opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                  "Or do you just want to go to the closest library (Option 2)? "
                                                  "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])

                  option = opinion_on_library
                  library_name = options(option)
                  print(f"Go to {choose_random_place(library_name)} of {library_name}")

      elif is_it_breakfast_or_brunch_time.lower() in ["no","n"]:
          is_it_lunch_time = get_user_input("Is it lunch time? ",
                                                ["yes", "y",
                                                  "no", "n"])
          
          if is_it_lunch_time.lower() in ["yes","y"]:
              got_lunch = get_user_input("Did you already get lunch? ",
                                                  ["yes", "y",
                                                      "no", "n"])
              
              if got_lunch.lower() in ["no","n"]:
                  neilson_lunch = get_user_input("Can you/did you order lunch from the Neilson cafe? ",
                                              ["yes", "y",
                                              "no", "n"])

                  if neilson_lunch.lower() in ["yes","y"]:
                      library_name = "Neilson"
                      print(f"Get your food, and then go to {choose_random_place(library_name)} of {library_name}")
                  
                  else:
                      opinion_on_library = get_user_input("Do you have a specific library in mind after you get lunch (Option 1)? "
                                                      "Or do you just want to go to the closest library (Option 2)? "
                                                      "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                      option = opinion_on_library
                      library_name = options(option)
                      print(f"After lunch, go to {choose_random_place(library_name)} of {library_name}")
              
              else:
                  if got_lunch in ["yes","y"]:
                      opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                      "Or do you just want to go to the closest library (Option 2)? "
                                                      "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])

                      option = opinion_on_library
                      library_name = options(option)
                      print(f"Go to {choose_random_place(library_name)} of {library_name}")
          
          elif is_it_lunch_time.lower() in ["no","n"]:
              is_it_dinner_time = get_user_input("Is it dinner time? ",
                                                  ["yes", "y",
                                                      "no", "n"])
              
              if is_it_dinner_time.lower() in ["yes","y"]:
                  got_dinner = get_user_input("Did you already get dinner? ",
                                                      ["yes", "y",
                                                          "no", "n"])
                  
                  if got_dinner.lower() in ["no","n"]:
                      cc_dinner = get_user_input("Can you/did you order lunch from the cc? ",
                                                  ["yes", "y",
                                                  "no", "n"])

                      if cc_dinner.lower() in ["yes","y"]:
                          opinion_on_library = get_user_input("Do you have a specific library in mind after you get dinner (Option 1)? "
                                                          "Or do you just want to go to the closest library (Option 2)? "
                                                          "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                          option = opinion_on_library
                          library_name = options(option)
                          print(f"After dinner, go to {choose_random_place(library_name)} of {library_name}")     
                      
                      else:
                          opinion_on_library = get_user_input("Do you have a specific library in mind after you get dinner (Option 1)? "
                                                          "Or do you just want to go to the closest library (Option 2)? "
                                                          "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])
                          option = opinion_on_library
                          library_name = options(option)
                          print(f"After dinner, go to {choose_random_place(library_name)} of {library_name}")
                
                  else:
                      if got_dinner in ["yes","y"]:
                          opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                                          "Or do you just want to go to the closest library (Option 2)? "
                                                          "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])

                          option = opinion_on_library
                          library_name = options(option)
                          print(f"Go to {choose_random_place(library_name)} of {library_name}")
        
    if is_it_a_mealtime.lower() in ["no","n"]:
      is_it_night_time = get_user_input("Is it after 11 pm? ",
                                      ["yes", "y",
                                      "no", "n"])
                
      if is_it_night_time.lower() in ["yes","y"]:
        library_name = "the Alumni Gym"
        print(f"Go to {choose_random_place(library_name)} of {library_name}")     
                
      if is_it_night_time.lower() in ["no","n"]:
        opinion_on_library = get_user_input("Do you have a specific library in mind (Option 1)? "
                                          "Or do you just want to go to the closest library (Option 2)? "
                                          "Or a random one (Option 3)? ", ["option 1", "1", "one", "option 2", "2", "two", "option 3", "3", "three"])

        option = opinion_on_library
        library_name = options(option)
        print(f"Go to {choose_random_place(library_name)} of {library_name}")
                        
if __name__ == "__main__":
    main()