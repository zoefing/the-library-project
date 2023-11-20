import random

while True:
    # see what the day of the week is
    user_input = input("What day of the week is it? ")
    # establish library
    library = ["Neilson", "Josten", "Hillyer", "Alumni Gym"]
    
    # this is only applicable in the code catered to my schedule (which varries by day)... but i'm keeping it
    if user_input in ["monday", "m", "mon", "tuesday", "tu", "tues", "wednesday","w", "weds", "thursday", "th", "thurs", "t", "friday", "fri", "f", "saturday", "sa", "sat", "sunday", "su", "sun", "s"]:
        # check if it is breakfast or brunch time
        is_it_breakfast_or_brunch = input("Is it breakfast/brunch time? ")
        
        # if it is breakfast or brunch time
        if is_it_breakfast_or_brunch.lower() in ["yes", "y"]:
            got_breakfast_or_brunch = input("Did you already get breakfast/brunch? ")
            
            # if the user did not yet get breakfast or brunch
            if got_breakfast_or_brunch.lower() in ["no","n"]:
                # see if neilson is a viable option
                neilson_brunch = input("Can you/did you order brunch from the Neislon cafe? ")
                            
                # if the cc is a viable option
                if neilson_brunch.lower() in ["yes", "y"]:
                    random_floor = random.randint(0,2)
                    print(f"Get your food, and then go to floor {random_floor} of {library[0]} Library")
                    break   
            
                # otherwise, if neilson is not a viable option
                else:
                    opinion_on_library = input("Do you have a specific library in mind after you get breakfast/brunch (Option 1)? Or do you just want to go to the closest library (Option 2)? Or a random one (Option 3)? ")
                    
                    # if user selects option 1
                    if opinion_on_library.lower() in ["option 1", "1", "one"]:
                        which_library = input("What library would you like to go to? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                        
                        # if neilson is slected
                        if which_library.lower() in ["neilson", "n"]:
                            random_floor = random.randint(0,4)
                            print(f"After breakfast/brunch, go to floor {random_floor} of {library[0]} Library")
                            break
                    
                        # otherwise, if jotsen is selected
                        elif which_library.lower() in ["jotsen", "j"]:
                            area = ["a listenting booth","the first floor study area", "the second floor study area"]
                            random_area = random.choice(area)
                            print(f"After breakfast/brunch, go to {random_area} in {library[1]} Library")
                            break
                        
                        # otherwise, if hillyer is selected
                        elif which_library.lower() in ["hillyer", "h"]:   
                            area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                            random_area = random.choice(area)
                            print(f"After breakfast/brunch, go to {random_area} in {library[2]} Library")
                            break              
                        
                        # otherwise, if alumni gym is selected
                        elif which_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                            random_floor = random.randint(1,3)
                            print(f"After breakfast/brunch, go to floor {random_floor} of {library[3]}")
                            break            
                        
                        
                    # otherwise, if user selects option 2
                    elif opinion_on_library.lower() in ["option 2", "2", "two"]:
                        closest_library = input("What is the closest library to your desired dining hall? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                        
                        # if neilson is selected
                        if closest_library.lower() in ["neilson", "n"]:
                            random_floor = random.randint(0,4)
                            print(f"After breakfast/brunch, go to floor {random_floor} of {library[0]} Library")
                            break
                    
                        # otherwise, if jotsen is selected
                        elif closest_library.lower() in ["jotsen", "j"]:
                            area = ["a listenting booth","the first floor study area", "the second floor study area"]
                            random_area = random.choice(area)
                            print(f"After breakfast/brunch, go to {random_area} in {library[1]} Library")
                            break
                        
                        # otherwise, if hillyer is selected
                        elif closest_library.lower() in ["hillyer", "h"]:   
                            area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                            random_area = random.choice(area)
                            print(f"After breakfast/brunch, go to {random_area} in {library[2]} Library")
                            break
    
                        # otherwise, if alumni gym is selected
                        elif closest_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                            random_floor = random.randint(1,3)
                            print(f"After breakfast/brunch, go to floor {random_floor} of {library[3]}")
                            break          
    
    
                    # otherwise, if user selects option 3            
                    elif opinion_on_library.lower() in ["option 3", "3", "three"]:
                        
                        # randomly choose a library
                        library_list = ["Neilson", "Josten", "Hillyer", "Alumni Gym"]
                        library = random.choice(library_list)
                        
                        # neilson
                        if library == "Neilson":
                            random_floor = random.randint(0,4)
                            print(f"Your random library is {library_list[0]}! After breakfast/brunch, go to floor {random_floor} of {library_list[0]} Library")
                            break
                    
                        # jotsen
                        elif library == "Josten":
                            area = ["a listenting booth","the first floor study area", "the second floor study area"]
                            random_area = random.choice(area)
                            print(f"Your random library is {library_list[1]}! After breakfast/brunch, go to {random_area} in {library_list[1]} Library")
                            break
                        
                        # hillyer
                        elif library == "Hillyer":   
                            area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                            random_area = random.choice(area)
                            print(f"Your random library is {library_list[2]}! After breakfast/brunch, go to {random_area} in {library_list[2]} Library")
                            break
            
                        # alumni gym
                        elif library == "Alumni Gym":   
                            random_floor = random.randint(1,3)
                            print(f"AYour random library is {library_list[3]}! After breakfast/brunch, go to floor {random_floor} of {library[3]}")
                            break          
            
            
            # otherwise, if the user already got breakfast/brunch
            elif got_breakfast_or_brunch == "yes":
                # see if they have a speicfic library in mind
                opinion_on_library = input("Do you have a specific library in mind (Option 1)? Or do you just want to go to the closest library (Option 2)? Or a random one (Option 3)? ")
                    
                # if user selects option 1
                if opinion_on_library.lower() in ["option 1", "1", "one"]:
                    which_library = input("What library would you like to go to? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                        
                    # if neilson is slected
                    if which_library.lower() in ["neilson", "n"]:
                        random_floor = random.randint(0,4)
                        print(f"Go to floor {random_floor} of {library[0]} Library")
                        break
                    
                    # otherwise, if jotsen is selected
                    elif which_library.lower() in ["jotsen", "j"]:
                        area = ["a listenting booth","the first floor study area", "the second floor study area"]
                        random_area = random.choice(area)
                        print(f"Go to {random_area} in {library[1]} Library")
                        break
                        
                    # otherwise, if hillyer is selected
                    elif which_library.lower() in ["hillyer", "h"]:   
                        area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                        random_area = random.choice(area)
                        print(f"Go to {random_area} in {library[2]} Library")
                        break                    
                        
                    # otherwise, if alumni gym is selected
                    elif which_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                        random_floor = random.randint(1,3)
                        print(f"Go to floor {random_floor} of {library[3]}")
                        break           
                        
                # otherwise, if user selects option 2
                elif opinion_on_library.lower() in ["option 2", "2", "two"]:
                    closest_library = input("What is the closest library to you? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                        
                    # if neilson is selected
                    if closest_library.lower() in ["neilson", "n"]:
                        random_floor = random.randint(0,4)
                        print(f"Go to floor {random_floor} of {library[0]} Library")
                        break
                    
                    # otherwise, if jotsen is selected
                    elif closest_library.lower() in ["jotsen", "j"]:
                        area = ["a listenting booth","the first floor study area", "the second floor study area"]
                        random_area = random.choice(area)
                        print(f"Go to {random_area} in {library[1]} Library")
                        break
                        
                    # otherwise, if hillyer is selected
                    elif closest_library.lower() in ["hillyer", "h"]:   
                        area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                        random_area = random.choice(area)
                        print(f"Go to {random_area} in {library[2]} Library")
                        break
                    
                    # otherwise, if alumni gym is selected
                    elif closest_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                        random_floor = random.randint(1,3)
                        print(f"Go to floor {random_floor} of {library[3]}")
                        break  
    
    
                # otherwise, if user selects option 3            
                elif opinion_on_library.lower() in ["option 3", "3", "three"]:
                        
                    # randomly choose a library
                    library_list = ["Neilson", "Josten", "Hillyer", "Alumni Gym"]
                    library = random.choice(library_list)
                        
                    # neilson
                    if library == "Neilson":
                        random_floor = random.randint(0,4)
                        print(f"Your random library is {library_list[0]}! Go to floor {random_floor} of {library_list[0]} Library")
                        break
                    
                    # jotsen
                    elif library == "Josten":
                        area = ["a listenting booth","the first floor study area", "the second floor study area"]
                        random_area = random.choice(area)
                        print(f"Your random library is {library_list[1]}! Go to {random_area} in {library_list[1]} Library")
                        break
                        
                    # hillyer
                    elif library == "Hillyer":   
                        area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                        random_area = random.choice(area)
                        print(f"Your random library is {library_list[2]}! Go to {random_area} in {library_list[2]} Library")
                        break
                    
                    # alumni gym
                    elif library == "Alumni Gym":   
                        random_floor = random.randint(1,3)
                        print(f"AYour random library is {library_list[3]}! Go to floor {random_floor} of {library[3]}")
                        break  
        
        # if it is not breakfast or brunch time
        if is_it_breakfast_or_brunch.lower() in ["no", "n"]:
            # check if it is lunchtime
            is_it_lunchtime = input("Ok... is it lunchtime? ")
            
            # if it is lunchtime
            if is_it_lunchtime.lower() in ["yes", "y"]:
                got_lunch = input("Did you already get lunch? ")
            
                # if the user did not yet get lunch
                if got_lunch.lower() in ["no","n"]:
                    # see if neilson is a viable option
                    got_lunch = input("Can you/did you order lunch from the Neislon cafe? ")
                        
                    # if neilson is a viable option
                    if got_lunch.lower() in ["yes", "y"]:
                        random_floor = random.randint(0,4)
                        print(f"Get your food, and then go to floor {random_floor} of {library[0]} Library")
                        break    

                    # otherwise, if neilson is not a viable option
                    else:
                        opinion_on_library = input("Do you have a specific library in mind after you get lunch (Option 1)? Or do you just want to go to the closest library (Option 2)? Or a random one (Option 3)? ")
                            
                        # if user selects option 1
                        if opinion_on_library.lower() in ["option 1", "1", "one"]:
                            which_library = input("What library would you like to go to? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                                
                            # if neilson is slected
                            if which_library.lower() in ["neilson", "n"]:
                                random_floor = random.randint(0,4)
                                print(f"After lunch, go to floor {random_floor} of {library[0]} Library")
                                break
                            
                            # otherwise, if jotsen is selected
                            elif which_library.lower() in ["jotsen", "j"]:
                                area = ["a listenting booth","the first floor study area", "the second floor study area"]
                                random_area = random.choice(area)
                                print(f"After lunch, go to {random_area} in {library[1]} Library")
                                break
                                
                            # otherwise, if hillyer is selected
                            elif which_library.lower() in ["hillyer", "h"]:   
                                area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                                random_area = random.choice(area)
                                print(f"After lunch, go to {random_area} in {library[2]} Library")
                                break   
                            
                            # otherwise, if alumni gym is selected
                            elif which_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                                random_floor = random.randint(1,3)
                                print(f"After lunch, go to floor {random_floor} of {library[3]}")
                                break                   
                                
                                
                        # otherwise, if user selects option 2
                        elif opinion_on_library.lower() in ["option 2", "2", "two"]:
                            closest_library = input("What is the closest library to your desired dining hall? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                                
                            # if neilson is selected
                            if closest_library.lower() in ["neilson", "n"]:
                                random_floor = random.randint(0,4)
                                print(f"After lunch, go to floor {random_floor} of {library[0]} Library")
                                break
                            
                            # otherwise, if jotsen is selected
                            elif closest_library.lower() in ["jotsen", "j"]:
                                area = ["a listenting booth","the first floor study area", "the second floor study area"]
                                random_area = random.choice(area)
                                print(f"After lunch, go to {random_area} in {library[1]} Library")
                                break
                                
                            # otherwise, if hillyer is selected
                            elif closest_library.lower() in ["hillyer", "h"]:   
                                area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                                random_area = random.choice(area)
                                print(f"After lunch, go to {random_area} in {library[2]} Library")
                                break
                            
                            # otherwise, if alumni gym is selected
                            elif which_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                                random_floor = random.randint(1,3)
                                print(f"After lunch, go to floor {random_floor} of {library[3]}")
                                break      
            
            
                        # otherwise, if user selects option 3            
                        elif opinion_on_library.lower() in ["option 3", "3", "three"]:
                                
                            # randomly choose a library
                            library_list = ["Neilson", "Josten", "Hillyer", "Alumni Gym"]
                            library = random.choice(library_list)
                                
                            # neilson
                            if library == "Neilson":
                                random_floor = random.randint(0,4)
                                print(f"Your random library is {library_list[0]}! After lunch, go to floor {random_floor} of {library_list[0]} Library")
                                break
                            
                            # jotsen
                            elif library == "Josten":
                                area = ["a listenting booth","the first floor study area", "the second floor study area"]
                                random_area = random.choice(area)
                                print(f"Your random library is {library_list[1]}! After lunch, go to {random_area} in {library_list[1]} Library")
                                break
                                
                            # hillyer
                            elif library == "Hillyer":   
                                area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                                random_area = random.choice(area)
                                print(f"Your random library is {library_list[2]}! After lunch, go to {random_area} in {library_list[2]} Library")
                                break
                            
                            # alumni gym
                            elif library == "Alumni Gym":   
                                random_floor = random.randint(1,3)
                                print(f"Your random library is {library_list[3]}! After lunch, go to floor {random_floor} of {library[3]}")
                                break  
                    
                # otherwise, if the user already got lunch
                elif got_lunch == "yes":
                    # see if they have a speicfic library in mind
                    opinion_on_library = input("Do you have a specific library in mind (Option 1)? Or do you just want to go to the closest library (Option 2)? Or a random one (Option 3)? ")
                            
                    # if user selects option 1
                    if opinion_on_library.lower() in ["option 1", "1", "one"]:
                        which_library = input("What library would you like to go to? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                                
                        # if neilson is slected
                        if which_library.lower() in ["neilson", "n"]:
                            random_floor = random.randint(0,4)
                            print(f"Go to floor {random_floor} of {library[0]} Library")
                            break
                            
                        # otherwise, if jotsen is selected
                        elif which_library.lower() in ["jotsen", "j"]:
                            area = ["a listenting booth","the first floor study area", "the second floor study area"]
                            random_area = random.choice(area)
                            print(f"Go to {random_area} in {library[1]} Library")
                            break
                                
                        # otherwise, if hillyer is selected
                        elif which_library.lower() in ["hillyer", "h"]:   
                            area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                            random_area = random.choice(area)
                            print(f"Go to {random_area} in {library[2]} Library")
                            break      
                        
                        # otherwise, if hillyer is selected
                        elif which_library.lower() in ["hillyer", "h"]:   
                            area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                            random_area = random.choice(area)
                            print(f"Go to {random_area} in {library[2]} Library")
                            break              
                        
                        # otherwise, if the alumni gym is selected
                        elif which_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                            random_floor = random.randint(1,3)
                            print(f"Go to floor {random_floor} of {library[3]}")
                            break              
                         
                                
                    # otherwise, if user selects option 2
                    elif opinion_on_library.lower() in ["option 2", "2", "two"]:
                        closest_library = input("What is the closest library to you? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                                
                        # if neilson is selected
                        if closest_library.lower() in ["neilson", "n"]:
                            random_floor = random.randint(0,4)
                            print(f"Go to floor {random_floor} of {library[0]} Library")
                            break
                            
                        # otherwise, if jotsen is selected
                        elif closest_library.lower() in ["jotsen", "j"]:
                            area = ["a listenting booth","the first floor study area", "the second floor study area"]
                            random_area = random.choice(area)
                            print(f"Go to {random_area} in {library[1]} Library")
                            break
                                
                        # otherwise, if hillyer is selected
                        elif closest_library.lower() in ["hillyer", "h"]:   
                            area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                            random_area = random.choice(area)
                            print(f"Go to {random_area} in {library[2]} Library")
                            break
                        
                        # otherwise, if the alumni gym is selected
                        elif closest_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                            random_floor = random.randint(1,3)
                            print(f"Go to floor {random_floor} of {library[3]}")
                            break      
            
            
                    # otherwise, if user selects option 3            
                    elif opinion_on_library.lower() in ["option 3", "3", "three"]:
                                
                        # randomly choose a library
                        library_list = ["Neilson", "Josten", "Hillyer", "Alumni Gym"]
                        library = random.choice(library_list)
                                
                        # neilson
                        if library == "Neilson":
                            random_floor = random.randint(0,4)
                            print(f"Your random library is {library_list[0]}! Go to floor {random_floor} of {library_list[0]} Library")
                            break
                            
                        # jotsen
                        elif library == "Josten":
                            area = ["a listenting booth","the first floor study area", "the second floor study area"]
                            random_area = random.choice(area)
                            print(f"Your random library is {library_list[1]}! Go to {random_area} in {library_list[1]} Library")
                            break
                                
                        # hillyer
                        elif library == "Hillyer":   
                            area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                            random_area = random.choice(area)
                            print(f"Your random library is {library_list[2]}! Go to {random_area} in {library_list[2]} Library")
                            break
                        
                         # alumni gym
                        elif library == "Alumni Gym":   
                            random_floor = random.randint(1,3)
                            print(f"Your random library is {library_list[3]}! Go to floor {random_floor} of {library[3]}")
                            break  
                
            # if it is not lunchtime
            elif is_it_lunchtime.lower() in ["no", "n"]:
                is_it_dinnertime = input("Ok... is it dinnertime? ")
                    
                # check if it is dinnertime
                if is_it_dinnertime.lower() in ["yes", "y"]:
                    got_dinner = input("Did you already get dinner? ")
                        
                    # if the user did not yet get dinner
                    if got_dinner.lower() in ["no","n"]:
                        # see if the cc is a viable option
                        cc_dinner = input("Can you/did you order dinner from the Campus Center cafe? ")
                            
                        # if the cc is a viable option
                        if cc_dinner.lower() in ["yes", "y"]:
                            random_floor = random.randint(0,2)
                            print(f"Get your food, and then go to floor {random_floor} of the Campus Center")
                            break    

                        # otherwise, if the cc is not a viable option
                        else:
                            opinion_on_library = input("Do you have a specific library in mind after you get dinner (Option 1)? Or do you just want to go to the closest library (Option 2)? Or a random one (Option 3)? ")
                                
                            # if user selects option 1
                            if opinion_on_library.lower() in ["option 1", "1", "one"]:
                                which_library = input("What library would you like to go to? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                                    
                                # if neilson is slected
                                if which_library.lower() in ["neilson", "n"]:
                                    random_floor = random.randint(0,4)
                                    print(f"After dinner, go to floor {random_floor} of {library[0]} Library")
                                    break
                                
                                # otherwise, if jotsen is selected
                                elif which_library.lower() in ["jotsen", "j"]:
                                    area = ["a listenting booth","the first floor study area", "the second floor study area"]
                                    random_area = random.choice(area)
                                    print(f"After dinner, go to {random_area} in {library[1]} Library")
                                    break
                                    
                                # otherwise, if hillyer is selected
                                elif which_library.lower() in ["hillyer", "h"]:   
                                    area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                                    random_area = random.choice(area)
                                    print(f"After dinner, go to {random_area} in {library[2]} Library")
                                    break     
                                
                                # otherwise, if the alumni gym is selected
                                elif which_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                                    random_floor = random.randint(1,3)
                                    print(f"After dinner, go to floor {random_floor} of {library[3]}")
                                    break             
                                    
                                    
                            # otherwise, if user selects option 2
                            elif opinion_on_library.lower() in ["option 2", "2", "two"]:
                                closest_library = input("What is the closest library to your desired dining hall? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                                    
                                # if neilson is selected
                                if closest_library.lower() in ["neilson", "n"]:
                                    random_floor = random.randint(0,4)
                                    print(f"After dinner, go to floor {random_floor} of {library[0]} Library")
                                    break
                                
                                # otherwise, if jotsen is selected
                                elif closest_library.lower() in ["jotsen", "j"]:
                                    area = ["a listenting booth","the first floor study area", "the second floor study area"]
                                    random_area = random.choice(area)
                                    print(f"After dinner, go to {random_area} in {library[1]} Library")
                                    break
                                    
                                # otherwise, if hillyer is selected
                                elif closest_library.lower() in ["hillyer", "h"]:   
                                    area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                                    random_area = random.choice(area)
                                    print(f"After lunch, go to {random_area} in {library[2]} Library")
                                    break
                                
                                # otherwise, if the alumni gym is selected
                                elif closest_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                                    random_floor = random.randint(1,3)
                                    print(f"After dinner, go to floor {random_floor} of {library[3]}")
                                    break 
                
                
                            # otherwise, if user selects option 3            
                            elif opinion_on_library.lower() in ["option 3", "3", "three"]:
                                    
                                # randomly choose a library
                                library_list = ["Neilson", "Josten", "Hillyer", "Alumni Gym"]
                                library = random.choice(library_list)
                                    
                                # neilson
                                if library == "Neilson":
                                    random_floor = random.randint(0,4)
                                    print(f"Your random library is {library_list[0]}! After dinner, go to floor {random_floor} of {library_list[0]} Library")
                                    break
                                
                                # josten
                                elif library == "Josten":
                                    area = ["a listenting booth","the first floor study area", "the second floor study area"]
                                    random_area = random.choice(area)
                                    print(f"Your random library is {library_list[1]}! After dinner, go to {random_area} in {library_list[1]} Library")
                                    break
                                    
                                # hillyer
                                elif library == "Hillyer":   
                                    area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                                    random_area = random.choice(area)
                                    print(f"Your random library is {library_list[2]}! After dinner, go to {random_area} in {library_list[2]} Library")
                                    break
                                
                                # alumni gym
                                elif library == "Alumni Gym":   
                                    random_floor = random.randint(1,3)
                                    print(f"Your random library is {library_list[3]}! After dinner, go to floor {random_floor} of {library[3]}")
                                    break  
                        
                        
                    # otherwise, if the user already got dinner
                    elif got_dinner.lower() == "yes":
                        # see if they have a speicfic library in mind
                        opinion_on_library = input("Do you have a specific library in mind (Option 1)? Or do you just want to go to the closest library (Option 2)? Or a random one (Option 3)? ")
                                
                        # if user selects option 1
                        if opinion_on_library.lower() in ["option 1", "1", "one"]:
                            which_library = input("What library would you like to go to? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                                    
                            # if neilson is slected
                            if which_library.lower() in ["neilson", "n"]:
                                random_floor = random.randint(0,4)
                                print(f"Go to floor {random_floor} of {library[0]} Library")
                                break
                                
                            # otherwise, if josten is selected
                            elif which_library.lower() in ["josten", "j"]:
                                area = ["a listenting booth","the first floor study area", "the second floor study area"]
                                random_area = random.choice(area)
                                print(f"Go to {random_area} in {library[1]} Library")
                                break
                                    
                            # otherwise, if hillyer is selected
                            elif which_library.lower() in ["hillyer", "h"]:   
                                area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                                random_area = random.choice(area)
                                print(f"Go to {random_area} in {library[2]} Library")
                                break       
                            
                            # otherwise, if the alumni gym is selected
                            elif which_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                                random_floor = random.randint(1,3)
                                print(f"Go to floor {random_floor} of {library[3]}")
                                break              
                                    
                                    
                        # otherwise, if user selects option 2
                        elif opinion_on_library.lower() in ["option 2", "2", "two"]:
                            closest_library = input("What is the closest library to you? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                                    
                            # if neilson is selected
                            if closest_library.lower() in ["neilson", "n"]:
                                random_floor = random.randint(0,4)
                                print(f"Go to floor {random_floor} of {library[0]} Library")
                                break
                                
                            # otherwise, if josten is selected
                            elif closest_library.lower() in ["jotsen", "j"]:
                                area = ["a listenting booth","the first floor study area", "the second floor study area"]
                                random_area = random.choice(area)
                                print(f"Go to {random_area} in {library[1]} Library")
                                break
                                    
                            # otherwise, if hillyer is selected
                            elif closest_library.lower() in ["hillyer", "h"]:   
                                area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                                random_area = random.choice(area)
                                print(f"Go to {random_area} in {library[2]} Library")
                                break
                            
                            # otherwise, if the alumni gym is selected
                            elif closest_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                                random_floor = random.randint(1,3)
                                print(f"Go to floor {random_floor} of {library[3]}")
                                break 
                
                
                        # otherwise, if user selects option 3            
                        elif opinion_on_library.lower() in ["option 3", "3", "three"]:
                                    
                            # randomly choose a library
                            library_list = ["Neilson", "Josten", "Hillyer", "Alumni Gym"]
                            library = random.choice(library_list)
                                    
                            # neilson
                            if library == "Neilson":
                                random_floor = random.randint(0,4)
                                print(f"Your random library is {library_list[0]}! Go to floor {random_floor} of {library_list[0]} Library")
                                break
                                
                            # jotsen
                            elif library == "Josten":
                                area = ["a listenting booth","the first floor study area", "the second floor study area"]
                                random_area = random.choice(area)
                                print(f"Your random library is {library_list[1]}! Go to {random_area} in {library_list[1]} Library")
                                break
                                    
                            # hillyer
                            elif library == "Hillyer":   
                                area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                                random_area = random.choice(area)
                                print(f"Your random library is {library_list[2]}! Go to {random_area} in {library_list[2]} Library")
                                break
                            
                            # alumni gym
                            elif library == "Alumni Gym":   
                                random_floor = random.randint(1,3)
                                print(f"Your random library is {library_list[3]}! Go to floor {random_floor} of {library[3]}")
                                break  
                    
                    
                elif is_it_dinnertime.lower() in ["no", "n"]:
                    opinion_on_library = input("Do you have a specific library in mind (Option 1)? Or do you just want to go to the closest library (Option 2)? Or a random one (Option 3)? ")
                        
                    # if user selects option 1
                    if opinion_on_library.lower() in ["option 1", "1", "one"]:
                        which_library = input("What library would you like to go to? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                                    
                        # if neilson is slected
                        if which_library.lower() in ["neilson", "n"]:
                            random_floor = random.randint(0,4)
                            print(f"Go to floor {random_floor} of {library[0]} Library")
                            break
                                
                        # otherwise, if jotsen is selected
                        elif which_library.lower() in ["jotsen", "j"]:
                            area = ["a listenting booth","the first floor study area", "the second floor study area"]
                            random_area = random.choice(area)
                            print(f"Go to {random_area} in {library[1]} Library")
                            break
                                    
                        # otherwise, if hillyer is selected
                        elif which_library.lower() in ["hillyer", "h"]:   
                            area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                            random_area = random.choice(area)
                            print(f"Go to {random_area} in {library[2]} Library")
                            break      
                        
                        # otherwise, if the alumni gym is selected
                        elif which_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                            random_floor = random.randint(1,3)
                            print(f"Go to floor {random_floor} of {library[3]}")
                            break               
                                    
                                    
                     # otherwise, if user selects option 2
                    elif opinion_on_library.lower() in ["option 2", "2", "two"]:
                        closest_library = input("What is the closest library to you? Neilson (N), Josten (J), Hillyer (H), or the Alumni Gym (AG)? ")
                                    
                        # if neilson is selected
                        if closest_library.lower() in ["neilson", "n"]:
                            random_floor = random.randint(0,4)
                            print(f"Go to floor {random_floor} of {library[0]} Library")
                            break
                                
                        # otherwise, if jotsen is selected
                        elif closest_library.lower() in ["jotsen", "j"]:
                            area = ["a listenting booth","the first floor study area", "the second floor study area"]
                            random_area = random.choice(area)
                            print(f"Go to {random_area} in {library[1]} Library")
                            break
                                    
                        # otherwise, if hillyer is selected
                        elif closest_library.lower() in ["hillyer", "h"]:   
                            area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                            random_area = random.choice(area)
                            print(f"Go to {random_area} in {library[2]} Library")
                            break
                        
                        # otherwise, if the alumni gym is selected
                        elif closest_library.lower() in ["alumni gym", "alumni","gym", "ag"]:   
                            random_floor = random.randint(1,3)
                            print(f"Go to floor {random_floor} of {library[3]}")
                            break 
                
                
                    # otherwise, if user selects option 3            
                    elif opinion_on_library.lower() in ["option 3", "3", "three"]:
                                    
                        # randomly choose a library
                        library_list = ["Neilson", "Josten", "Hillyer", "Alumni Gym"]
                        library = random.choice(library_list)
                                    
                        # neilson
                        if library == "Neilson":
                            random_floor = random.randint(0,4)
                            print(f"Your random library is {library_list[0]}! Go to floor {random_floor} of {library_list[0]} Library")
                            break
                                
                        # jotsen
                        elif library == "Josten":
                            area = ["a listenting booth","the first floor study area", "the second floor study area"]
                            random_area = random.choice(area)
                            print(f"Your random library is {library_list[1]}! Go to {random_area} in {library_list[1]} Library")
                            break
                                    
                        # hillyer
                        elif library == "Hillyer":   
                            area = ["the auditorium", "the atrium", "the first floor study area", "a study carrel on the first floor", "the second floor study area", "a study carrel on the second floor"]
                            random_area = random.choice(area)
                            print(f"Your random library is {library_list[2]}! Go to {random_area} in {library_list[2]} Library")
                            break
                        
                        # alumni gym
                        elif library == "Alumni Gym":   
                            random_floor = random.randint(1,3)
                            print(f"Your random library is {library_list[3]}! Go to floor {random_floor} of {library[3]}")
                            break  
