# customer's menu
def customer_final():


    # schedule list
    def default_schedule():
        f = open("schedule.txt", "w")
        f.write("")
        f.close()

        schedule_list = [
            ["AMG100", "Kuala Lumpur", "Jakarta", "17 November 2021", "17:00 UTC+8", "17 November 2021", "19:15 UTC+8", "25 November 2021", "18:00 UTC+8", "25 November 2021", "20:00 UTC+8"],
            ["AMG111", "Kuala Lumpur", "Singapore", "20 November 2021", "19:00 UTC+8", "20 November 2021", "20:00 UTC+8", "26 November 2021", "19:00 UTC+8", "26 November 2021", "20:00 UTC+8"],
            ["AMG123", "Riyadh", "Kuala Lumpur", "23 November 2021", "19:00 UTC+8", "24 November 2021", "05:30 UTC+8", "27 November 2021", "18:00 UTC+8", "28 November 2021", "04:00 UTC+8"],
            ["AMG222", "Singapore", "Kuala Lumpur", "23 November 2021", "12:45 UTC+8", "23 November 2021", "14:00 UTC+8", "28 November 2021", "19:00 UTC+8", "28 November 2021", "20:00 UTC+8"],
            ["AMG234", "Singapore", "Beijing", "23 November 2021", "10:00 UTC+8", "23 November 2021", "20:10 UTC+8", "29 November 2021", "10:00 UTC+8", "29 November 2021", "20:00 UTC+8"],
            ["AMG333", "Kuala Lumpur", "Tokyo", "25 November 2021", "20:00 UTC+8", "26 November 2021", "02:15 UTC+8", "30 November 2021", "10:00 UTC+8", "30 November 2021", "16:00 UTC+8"],
            ["AMG345", "Tokyo", "Monaco", "25 November 2021", "02:00 UTC+8", "25 November 2021", "17:15 UTC+8", "1 December 2021", "10:00 UTC+8", "2 December 2021", "01:00 UTC+8"],
            ["AMG444", "Jakarta", "Singapore", "26 November 2021", "12:00 UTC+8", "26 November 2021", "13:55 UTC+8", "2 December 2021", "06:00 UTC+8", "2 December 2021", "08:00 UTC+8"],
            ["AMG456", "Jakarta", "Washington DC", "26 November 2021", "12:00 UTC+8", "27 November 2021", "09:30 UTC+8", "3 December 2021", "12:00 UTC+8", "4 December 2021", "09:30 UTC+8"],
            ["AMG555", "New Delhi", "Kuala Lumpur", "28 November 2021", "06:00 UTC+8", "28 November 2021", "11:30 UTC+8", "5 December 2021", "07:30 UTC+8", "5 December 2021", "14:00 UTC+8"],
        ]

        f = open("schedule.txt", "a")
        for row in schedule_list:
            for element in row:
                f.write(element + ";")
            f.write("\n")
        f.close()



    # display schedule list
    def display_schedule():
        f = open("schedule.txt", "r")
        content = f.read()
        content_listbyline = content.splitlines()
        f.close()

        print("---------------------------------------")

        for flight_element in content_listbyline:
            detail = flight_element.split(";")
            print("Airline No        :", detail[0])
            print("Flight From       :", detail[1])
            print("Flight To         :", detail[2])
            print("Departure Date    :", detail[3])
            print("Departure Time    :", detail[4])
            print("Arrival Date      :", detail[5])
            print("Arrival Time      :", detail[6])
            print("Return Departure Date     :", detail[7])
            print("Return Departure Time     :", detail[8])
            print("Return Arrival Date       :", detail[9])
            print("Return Arrival Time       :", detail[10])
            print("---------------------------------------")



    # search flights    
    def search_flights():
        search_number = int(input(
            "1. Search by Departure City\n"
            "2. Search by Departure Date\n"
            "3. Search by City Destination\n"
            "4. Search by Return Date\n"
            "5. Search by all\n"
            "6. Go back to main menu\n"
            "---------------------------------------\n"
            "Select number: "
        ))
        print("---------------------------------------")

        #reading the schedule first
        f = open('schedule.txt', 'r')
        content = f.read()
        content_listbyline = content.splitlines()
        f.close()
        print("---------------------------------------")

        # defining the choices
        def departure_city():
            search = input("Enter Departure City to search:")
            print("---------------------------------------")
            for flight_element in content_listbyline:
                detail = flight_element.split(";")
                if search in detail[1]:
                    print("Airline No        : ", detail[0])
                    print("Flight From       : ", detail[1])
                    print("Flight To         : ", detail[2])
                    print("Departure Date    : ", detail[3])
                    print("Departure Time    : ", detail[4])
                    print("Arrival Date      : ", detail[5])
                    print("Arrival Time      : ", detail[6])
                    print("Return Departure Date     : ", detail[7])
                    print("Return Departure Time     : ", detail[8])
                    print("Return Arrival Date       : ", detail[9])
                    print("Return Arrival Time       : ", detail[10])
                    print("---------------------------------------")
                    
        def departure_date():
            search = input("Enter Departure Date to search:")
            print("---------------------------------------")
            for flight_element in content_listbyline:
                detail = flight_element.split(";")
                if search in detail[3]:
                    print("Airline No        : ", detail[0])
                    print("Flight From       : ", detail[1])
                    print("Flight To         : ", detail[2])
                    print("Departure Date    : ", detail[3])
                    print("Departure Time    : ", detail[4])
                    print("Arrival Date      : ", detail[5])
                    print("Arrival Time      : ", detail[6])
                    print("Return Departure Date     : ", detail[7])
                    print("Return Departure Time     : ", detail[8])
                    print("Return Arrival Date       : ", detail[9])
                    print("Return Arrival Time       : ", detail[10])
                    print("---------------------------------------")

        def city_destination():
            search = input("Enter City Destination to search:")
            print("---------------------------------------")
            for flight_element in content_listbyline:
                detail = flight_element.split(";")
                if search in detail[2]:
                    print("Airline No        : ", detail[0])
                    print("Flight From       : ", detail[1])
                    print("Flight To         : ", detail[2])
                    print("Departure Date    : ", detail[3])
                    print("Departure Time    : ", detail[4])
                    print("Arrival Date      : ", detail[5])
                    print("Arrival Time      : ", detail[6])
                    print("Return Departure Date     : ", detail[7])
                    print("Return Departure Time     : ", detail[8])
                    print("Return Arrival Date       : ", detail[9])
                    print("Return Arrival Time       : ", detail[10])
                    print("---------------------------------------")
                else:
                    print("NOT FOUND!!")
                    print("---------------------------------------")

        def return_date():
            search = input("Enter Return Date to search:")
            print("---------------------------------------")
            for flight_element in content_listbyline:
                detail = flight_element.split(";")
                if search in detail[7]:
                    print("Airline No        : ", detail[0])
                    print("Flight From       : ", detail[1])
                    print("Flight To         : ", detail[2])
                    print("Departure Date    : ", detail[3])
                    print("Departure Time    : ", detail[4])
                    print("Arrival Date      : ", detail[5])
                    print("Arrival Time      : ", detail[6])
                    print("Return Departure Date     : ", detail[7])
                    print("Return Departure Time     : ", detail[8])
                    print("Return Arrival Date       : ", detail[9])
                    print("Return Arrival Time       : ", detail[10])
                    print("---------------------------------------")          

        def search_all():
            departure = input("Enter Departure City     : ")
            date = input("Enter Departure Date          : ")
            destination = input("Enter City Destination : ")
            returndate = input("Enter Return Date       : ")
            print("---------------------------------------")
            for flight_element in content_listbyline:
                detail = flight_element.split(";")
                if (departure in detail[1] and date in detail[3] and destination in detail[2] and returndate in detail[7]):
                    print("Airline No        :", detail[0])
                    print("Flight From       :", detail[1])
                    print("Flight To         :", detail[2])
                    print("Departure Date    :", detail[3])
                    print("Departure Time    :", detail[4])
                    print("Arrival Date      :", detail[5])
                    print("Arrival Time      :", detail[6])
                    print("Return Departure Date     :", detail[7])
                    print("Return Departure Time     :", detail[8])
                    print("Return Arrival Date       :", detail[9])
                    print("Return Arrival Time       :", detail[10])
                    print("---------------------------------------")
                                        

        # choosing the choices
        if search_number == 1:
            departure_city()
            print("---------------------------------------")
            menu()
        elif search_number == 2:
            departure_date()
            print("---------------------------------------")
            menu()
        elif search_number == 3:
            city_destination()
            print("---------------------------------------")
            menu()
        elif search_number == 4:
            return_date()
            print("---------------------------------------")
            menu()
        elif search_number == 5:
            search_all()
            print("---------------------------------------")
            menu()
        elif search_number == 6:
            print("Going back to main menu...")
            print("---------------------------------------")
            menu()
        else:
            print("The choice isn't available, please try again")
            menu()



    # register
    def registermenu():

        # registering
        def register():
            members_info = []

            print("##----Sign Up Page----##")

            username = input("Username  : ")
            password = input("Password  : ")
            confirm_password = input("Confirm Password: ")
            name = input("Full Name  : ")
            birthday = input("Date of Birth   : ")
            nationality = input("Nationality  : ")
            telp_number = input("Telephone No : ")
            emergency = input("Emergency Contact No: ")
            card = input("Credit/Debit Card Number : ")

            if password != confirm_password:
                print("==============================")
                print("Password doesn't match, please try again")
                print("==============================")
                register()
            else:
                if len(password)<=4:
                    print("==============================")
                    print("Password is too short, please make the password more than 4 characters")
                    print("==============================")
                    register()  
                else:
                    members_info.append(username)
                    members_info.append(password)
                    members_info.append(name)
                    members_info.append(birthday)
                    members_info.append(telp_number)
                    members_info.append(nationality)
                    members_info.append(emergency)
                    members_info.append(card)

                    print("==============================")
                    print("Here's you're details!")
                    print("Details: ", members_info)
                    print("==============================")

                    f = open('members.txt', 'a')
                    for info in members_info:
                        f.write(info + ";")
                    f.write("\n")
                    f.close


        # options choices
        continue_confirm = int(input(
            "=====Let's register=====!\n"
            "1. Continue\n"
            "2. Back to main menu\n"
            "---------------------------------------\n"
            "Select number: "
            ))

        print("---------------------------------------")

        if continue_confirm == 1:
            register()
            print("---------------------------------------")
        elif continue_confirm == 2:
            menu()
            print("---------------------------------------")
        else:
            print("Wrong input! let's try that again")
            print("---------------------------------------")
            registermenu()



    # exit
    def exit():
        pass



    # main menu 
    def menu():
        print("+++++++++++++++++++++++++++++++++++++++")
        insert_number = int(input(
        "1. Display Flight Schedule\n"
        "2. Search for Flight Schedule\n"
        "3. Register as a member\n"
        "4. Exit\n"
        "---------------------------------------\n"
        "Select number: "
        ))

        if insert_number == 1:
            print("---------------------------------------")
            display_schedule()
            menu()
        elif insert_number == 2:
            print("---------------------------------------")
            search_flights()
            menu()
        elif insert_number == 3:
            print("---------------------------------------")
            registermenu()
            menu()
        elif insert_number == 4:
            print("exiting....")
            print("---------------------------------------")
            exit()
        else:
            print("---------------------------------------")
            print("The choice isn't available, please try again")
            menu()

    # start up the program
    menu()

        

# member's menu
def members_final():
  
   def check_credentials(username,password):
      f = open('members.txt','r')
      for member in f:
         user =  member.split(';')
         if(user[0] == username and user[1] == password):
            return user[:8]
      return None

   def modify_file(user):
      f = open('members.txt','r')
      users = f.read().split('\n')
      f.close()
      f = open('members.txt','w')
      for i in users:
         if i.split(';')[0] ==user[0]:
            for info in user:
               f.write(info + ";")
            f.write('\n')
         else:
            f.write(i)
            f.write('\n')
      f.close()
      print('---------------------Successfully Modified Profile------------\n')
      
   def modify_details(user):
      print("1. Password")
      print("2. Fullname")
      print("3. Emergency Contact Number")
      print("4. Credit/Debit Card Number")
      print("5. Go back to main menu")
      print("--------------------------------")
      choice = int(input("Select what do you want to Modify : "))

      if choice ==1:
         print("---------------------------------------")
         user[1]= input("Enter New Password: ")
         modify_file(user)
      elif choice == 2:
         print("---------------------------------------")
         user[2] = input("Enter New Name: ")
         modify_file(user)
      elif choice == 3:
         print("---------------------------------------")
         user[6] = input("Enter New  Emergency Contact Number: ")
         modify_file(user)
      elif choice == 4:
         print("---------------------------------------")
         user[7] = input("Enter New Debit/Credit Number: ")
         modify_file(user)
      elif choice == 5:
         print(
         "---------------------------------------\n"
         "Going Back to Main Menu...\n"
         "---------------------------------------"
         )
         menu(user)
      else:
         print("---------------------------------------")
         print("The choice isn't available!")
         menu(user)

   # display schedule list
   def display_schedule():
      f = open("schedule.txt", "r")
      content = f.read()
      content_listbyline = content.splitlines()
      f.close()

      print("---------------------------------------")
      i=1
      for flight_element in content_listbyline:
         detail = flight_element.split(";")
         print(f'--------------------{i}----------------------')
         print("Airline No        :", detail[0])
         print("Flight From       :", detail[1])
         print("Flight To         :", detail[2])
         print("Departure Date    :", detail[3])
         print("Departure Time    :", detail[4])
         print("Arrival Date      :", detail[5])
         print("Arrival Time      :", detail[6])
         print("Return Departure Date     :", detail[7])
         print("Return Departure Time     :", detail[8])
         print("Return Arrival Date       :", detail[9])
         print("Return Arrival Time       :", detail[10])
         print("---------------------------------------")
         i+=1

   def add_bookings(user):
      display_schedule()
      schedule = int(input("Enter Schedule Number in Which you want a Booking: "))

      while 1:
         way = int(input('One Way or Return Ticket(1-2) : '))
         if way != 1 and way!=2:
            print("-------------Invalid Input--------------")
         else:
            break
      
      clss = input("Class Economy/ First Class/ Business : ")
      includeInsurance = input("Include Travel Insurance(y/n) : ")
      seating = input("Enter Seating (random, window, aisle, extra legroom) : ")

      print('------------------------------------------')
      confirm = input("Do you want to confirm the booking(y/n) : ")

      print('---------------------------')
      if confirm != 'y':
         print("Booking Cancelled!")
      else :   
         booking_num = 0
         f = open('bookings.txt','r')
         for i in f:
            booking_num+=1
         f.close()
         f = open("bookings.txt",'a')
         f.write(f"{booking_num};{user[0]};{schedule};{way};{clss};{includeInsurance};{seating}")
         f.write('\n')
         f.close()
         print("Booking Confirmed!")

   def display_bookings(user):
      f = open('bookings.txt')
      for booking in f:
         b = booking.split(';')
         if b[1] ==  user[0]:
            print('============Booking Details============')
            print('Booking Number : ',b[0])
            print("One Way / Return : ",b[3])
            print("Class : ",b[4])
            print("Insurance Included : ",b[5])
            print("Seat Type : ",b[6])
            print('============Flight Details============')
            schedule_number = int(b[2])
            n=1
            f = open("schedule.txt", "r")
            content = f.read()
            content_listbyline = content.splitlines()
            f.close()

            detail = content_listbyline[schedule_number-1].split(';')
            
            print("Airline No        :", detail[0])
            print("Flight From       :", detail[1])
            print("Flight To         :", detail[2])
            print("Departure Date    :", detail[3])
            print("Departure Time    :", detail[4])
            print("Arrival Date      :", detail[5])
            print("Arrival Time      :", detail[6])
            print("Return Departure Date     :", detail[7])
            print("Return Departure Time     :", detail[8])
            print("Return Arrival Date       :", detail[9])
            print("Return Arrival Time       :", detail[10])
            print("---------------------------------------")
      f.close()

   def display_profile(user):
      print(f"Username : {user[0]}")
      print(f"Password : {user[1]}")
      print(f"Fullname : {user[2]}")
      print(f"Date Of Birth : {user[3]}")
      print(f"Nationality : {user[5]}")
      print(f"Telephone Number : {user[4]}")
      print(f"Emergency Contact Number : {user[6]}")
      print(f"Credit/Debit Card Number : {user[7]}")

   # main menu 
   def menu(current_user):
      print("+++++++++++++++++++++++++++++++++++++++")
      insert_number = int(input(
      "1. Display Profile\n"
      "2. Display Bookings\n"
      "3. Add Bookings\n"
      "4. Modify Profile\n"
      "5. Exit Program\n"
      "---------------------------------------\n"
      "Select number: "
      ))

      if insert_number == 1:
         print("---------------------------------------")
         display_profile(current_user)
         menu(current_user)
      elif insert_number == 2:
         print("---------------------------------------")
         display_bookings(current_user)
         menu(current_user)
      elif insert_number == 3:
         print("---------------------------------------")
         add_bookings(current_user)
         menu(current_user)
      elif insert_number == 4:
         print("---------------------------------------")
         modify_details(current_user)
         menu(current_user)
      elif insert_number == 5:
         print("exiting....")
         print("---------------------------------------")
         exit()
      else:
         print("---------------------------------------")
         print("The choice isn't available, please try again")
         menu()

   # start up the program
   def startup():
      print("------------------Login to access System----------------")
      username = input("Username : ")
      password = input("Password : ")

      current_user = check_credentials(username,password)
      if(current_user!=None):
         print("--------------Login Succesfull-----------------------")
         menu(current_user)
      else:
         print("--------------------------------------------")
         print("Wrong Credentials !")

   startup()



#admin's menu
def admin_final():
    # login operation
    granted = False
    def grant():
        global granted
        granted = True
        
    def login(name,password):
        success = False
        file = open("login_address.txt","r")
        for i in file:
            a,b = i.split(",")
            b = b.strip()
            if(a==name and b==password):
                success = True
                print("----------------------")
        file.close()
        if (success):
            print("Login Successful!")
            grant()
        else:
            print("wrong username or password")
            access(option)
        
    def register(name,password):
        file = open("login_address.txt","a")
        file.write("\n"+name+","+password)
        file.close()
        grant()
        
    def access(option):
        global name
        if(option=="login"):
            name = input("Enter your username: ")
            password = input("Enter your password: ")
            login(name,password)
        else:
            print("Enter your username and password to be registered")
            name = input("Enter your username: ")
            password = input("Enter your passwords: ")
            register(name,password)

    # Login Page
    def begin():
        global option
        print("Welcome to Portal")
        option = input("Login or Register (login,reg): ")
        if(option!="login" and option!="reg"):
            begin()
    
    begin()
    access(option)
    if(granted):
        print("Welcome Back Administrator")
        print("### User Details ###")
        print("Username: ",name)
        
    # Question 1.a  
    def Flight_details():
        f = open("schedule_vigy.txt", "a")
        flight_number = input("Enter flight number: ")
        flight_from = input("Enter departure: ")
        flight_to = input("Enter destination: ")
        departure_date =  input("Enter date of departure: ")
        departure_time = input("Enter time of departure: ")
        arrival_date = input("Enter date of arrival: ")
        arrival_time = input("Enter time of arrival: ")
        return_departure_date = input("Enter return departure date: ")
        return_departure_time = input("Enter return departure time: ")
        return_arrival_date = input("Enter return arrival date: ")
        return_arrival_time = input("Enter return arrival time: ")
        price = input("Enter the price: ")
        classification = input("Enter your class: ")
        f.write("\n"+flight_number+";"+flight_from+";"+flight_to+";"+departure_date+";"+departure_time+";"+arrival_date+";"+arrival_time+";"+return_departure_date+";"+return_departure_time+";"+return_arrival_date+";"+return_arrival_time+";"+price+";"+classification)
        f.close()
        print("Flight details successfully added!")

    # Question 1.b
    def Ticket_details():
        f = open("Ticket.txt", "a") 
        todays_date = input("Enter the date: ")
        ticket_sold = input("Enter the number of ticket sold today: ")
        profit_made = input("What is the profit made for today: ")
        f.write("\n"+todays_date+";"+ticket_sold+";"+profit_made)
        f.close()
        print("Ticket details successfully added!")
        
    # Question 1
    def add_flight_details():
        while True:
            print("Please choose from the provided question"
            "\n 1.Flight details"
            "\n 2.Tickets details"
            "\n 3.Exit (logout)")
            option = int(input("Choose your choice: "))
            if option == 1:
                Flight_details()
                print("----------------------")
                break
            elif option == 2:
                Ticket_details() 
                print("----------------------")
                break
            elif option == 3:
                exit()
                break
            else:
                print("Invalid Choice")
    

    # Question 2
    def modifying_flight_details():
        f = open("schedule.txt","r")
        content = f.read()
        content_listbyline = content.splitlines()
        f.close()

        print("---------------------------------------")
        for flight_element in content_listbyline:
            detail = flight_element.split(";")
            print("Airline No        :", detail[0])
            print("Flight From       :", detail[1])
            print("Flight To         :", detail[2])
            print("Departure Date    :", detail[3])
            print("Departure Time    :", detail[4])
            print("Arrival Date      :", detail[5])
            print("Arrival Time      :", detail[6])
            print("Return Departure Date   :", detail[7])
            print("Return Departure Time   :", detail[8])
            print("Return Arrival Date     :", detail[9])
            print("Return Arrival Time     :", detail[10])
            print("---------------------------------------")

            f = open("schedule_vigy.txt", "a")
        flight_number = input("Enter flight number: ")
        flight_from = input("Enter departure: ")
        flight_to = input("Enter destination: ")
        departure_date =  input("Enter date of departure: ")
        departure_time = input("Enter time of departure: ")
        arrival_date = input("Enter date of arrival: ")
        arrival_time = input("Enter time of arrival: ")
        return_departure_date = input("Enter return departure date: ")
        return_departure_time = input("Enter return departure time: ")
        return_arrival_date = input("Enter return arrival date: ")
        return_arrival_time = input("Enter return arrival time: ")
        price = input("Enter the price: ")
        classification = input("Enter your class: ")
        f.write("\n"+flight_number+";"+flight_from+";"+flight_to+";"+departure_date+";"+departure_time+";"+arrival_date+";"+arrival_time+";"+return_departure_date+";"+return_departure_time+";"+return_arrival_date+";"+return_arrival_time+";"+price+";"+classification)
        f.close()
        print("Flight details successfully added!")

    # Question 3.a
    def Display_schedules():

        f = open("schedule.txt", "r")
        content = f.read()
        content_listbyline = content.splitlines()
        f.close()

        print("---------------------------------------")
        for flight_element in content_listbyline:
            detail = flight_element.split(";")
            print("Airline No        :", detail[0])
            print("Flight From       :", detail[1])
            print("Flight To         :", detail[2])
            print("Departure Date    :", detail[3])
            print("Departure Time    :", detail[4])
            print("Arrival Date      :", detail[5])
            print("Arrival Time      :", detail[6])
            print("Return Departure Date   :", detail[7])
            print("Return Departure Time   :", detail[8])
            print("Return Arrival Date     :", detail[9])
            print("Return Arrival Time     :", detail[10])
            print("---------------------------------------")

    # Question 3.b
    def Booked_flights():
        f = open("bookings.txt", "r")
        content = f.read()
        content_listbyline = content.splitlines()

        print("---------------------------------------")
        for bookings_element in content_listbyline:
            detail = bookings_element.split(";")
            print("Booking Number        :", detail[0])
            print("User                  :", detail[1])
            print("Schedule              :", detail[2])
            print("Way                   :", detail[3])
            print("class                 :", detail[4])
            print("IncludeInsurance     :", detail[5])
            print("Seatings             :", detail[6])
            print("---------------------------------------")

    # Question 3.c
    def Total_ticket_sold():
        f = open("ticket.txt", "r")
        content = f.read()
        content_listbyline = content.splitlines()

        print("---------------------------------------")
        for bookings_element in content_listbyline:
            detail = bookings_element.split(";")
            print("Date                  :", detail[0])
            print("Ticket sold           :", detail[1])
            print("Profit earned         :", detail[2])
            print("---------------------------------------")

    # Question 3
    def Displaying_all_records():
        while True:
            print("Please choose from the provided question"
            "\n 1.Display schedules"
            "\n 2.Booked flights"
            "\n 3.Total ticket sold"
            "\n 4.Exit (logout)")
            option = int(input("Choose your choice: "))
            if option == 1:
                Display_schedules()
                print("----------------------")
                break
            elif option == 2:
                Booked_flights()
                print("----------------------")
                break
            elif option == 3:
                Total_ticket_sold()
                print("----------------------")
                break
            elif option == 4:
                exit()
                break
            else:
                print("Invalid Choice")
            
    # Choices         
    def main_menu():
        while True:
            print("Please choose from the provided question"
            "\n 1.Add flight details"
            "\n 2.Modify flight schedules"
            "\n 3.Displaying all records"
            "\n 4.Exit (logout)")
            option = int(input("Choose your choice: "))
            if option == 1:
                add_flight_details()
                print("----------------------")
                break
            elif option == 2:
                modifying_flight_details()
                print("----------------------")
                break
            elif option == 3:
                Displaying_all_records()
                print("----------------------")
                break
            elif option == 4:
                exit()
            else:
                print("Invalid Choice")

    # Activate program           
    main_menu()
    pass



# ultimate main menu
def ultimate_menu():
    
    print("==============================")
    print("Welcome to the Main Menu")
    print("==============================")
    choose_input_final = int(input("1. Customers Menu\n"
                       "2. Members Menu\n"
                       "3. Admins Menu\n"
                       "4. Exit\n"
                       "==============================\n"
                       "Please choose a number:" ))
    print("==============================")

    if choose_input_final == 1:
        print("=========== ## Customer's Menu ## ============")
        customer_final()
    elif choose_input_final == 2:
        print("=========== ## Member's Menu ## ============")
        members_final()
    elif choose_input_final == 3:
        print("=========== ## Admin's Menu ## ============")
        admin_final()
    elif choose_input_final == 4:
        print("=========== ## Exiting... ## ============")
        pass
    else:
        print("==============================")
        print("Wrong Input please try again")
        print("==============================")
        ultimate_menu()

#startup
ultimate_menu()