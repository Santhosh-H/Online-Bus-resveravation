def book_bus():
    global booking_details
    from time import sleep
    from tabulate import tabulate
    from random import randint
    from datetime import datetime
    from sql_python_connection import fetch_details_from_table
    all_bus_details = fetch_details_from_table(3)
    from_ = input("Enter the Source Location: ")
    to_ = input("Enter the Destination Location: ")
    available_bus = []
    for each_bus in all_bus_details:
        print(each_bus)
        available_bus.append(each_bus)
    if available_bus == []:
        print("No Bus is Available for either Source Location or Destination Location")
    else:
        dta = []
        for iterate in available_bus:
            dta.append(iterate[:4]+iterate[6:8])
        print(tabulate(dta, headers=["Bus Number","Bus Name","Source Location","Destination Location","Seats Available","Price for one Seat"], tablefmt="grid"))
        bus_no = input("Enter The Bus Number: ")
        booked_bus_details = []
        print(dta)
        for bus in dta:
            if bus_no == bus[0]:
                booked_bus_details.append(bus)
                break
        else:
            print("Enter Bus Number Correctly!")

        from_date = (input("Enter From Date(dd/mm/yyyy): ").split("/"))
        to_date = (input("Enter To Date(dd/mm/yyyy): ").split("/"))
        try:
            f = datetime(int(from_date[2]), int(from_date[1]), int(from_date[0]))
            t = datetime(int(to_date[2]), int(to_date[1]), int(to_date[0]))
        except:
            print("\t\t:DATE FORMATE IS WRONG:")
        seats = input("Enter the No of Seats: ")
        while not(seats.isnumeric()):
            print("Enter Correct Seat Number")
            seats = input("Enter the No of Seats: ")
        seats = int(seats)
        print(booked_bus_details)
        booking_details ={

                "Bus_Number":booked_bus_details[0][0],
                "Bus_Name":booked_bus_details[0][1],
                "Source_Location":booked_bus_details[0][2],
                "Destination_Location":booked_bus_details[0][3],
                "From_date": "-".join(from_date),
                "To_date": "-".join(to_date),
                "Price_for_one_Seats":booked_bus_details[0][-1],
                "Total_Seats_Booked":seats,
                "Total_Price":(int(booked_bus_details[0][-1])*seats)
        }
        t_price = booking_details["Total_Price"]
        print("Your Booking Detials is Below")
        print(tabulate([booking_details.values()], headers=booking_details.keys(), tablefmt="grid"))
        print(f"\n\n Your Total Price for the booking is {t_price}")
        final_choice = input("Want to Proceed to checkout or Dismiss this Booking Process (y/n)")
        if final_choice.lower() in "yes":
            Payment()
        else:
            from main import front_page
            front_page() 
        
def Payment():
    from time import sleep
    from tqdm import tqdm
    from pickle import dump,load
    from random import randint
    from sql_python_connection import fetch_details_from_table,Update_record
    all_customer_details = fetch_details_from_table(1)
    all_bus_details = fetch_details_from_table(3)
    def Transaction():
        global booking_details
        otp_rdm = randint(10000,99999)
        from mailsend import sending_mail
        cust_uname = input("Enter Your Customer Id: ")
        cust_passwd = input("Enter Your Password: ")
        for Customer in all_customer_details:
            if int(cust_uname) == int(Customer[0]):
                if cust_passwd == Customer[-1]:
                    email = Customer[-2]
                    break
        else:
            print("Invalid Entry!")
        sending_mail(to_adress=email, subject="OTP VERIFICATION REQUIRED!",body=f"Your One Time Password for Online Bus Booking is {otp_rdm}")
        otp_prompt = input("Enter The Otp Sent to your Registered Email Address: ")
        print(otp_rdm)
        while not(otp_prompt.isnumeric()) and int(otp_rdm) != int(otp_prompt):
            print("\t\tInvalid OTP")
            otp_rdm = randint(10000,99999)
            sending_mail(to_adress=email, subject="OTP VERIFICATION REQUIRED!",body=f"Your One Time Password for Online Bus Booking is {otp_rdm}")
            otp_prompt = input("Enter The New Otp Sent to your Registered Email Address: ")
        else:
            loop = tqdm(total=10000, position=0, leave=False)
            for k in range(10000):
                loop.set_description("Transaction is being processed".format(k))
                loop.update(1)
            loop.close()
            print("\t\tTransaction has been processed")
            sleep(5)
            print("\t\tPayment is Done\n Have a Great Day")
            for each_bus in all_bus_details:
                if each_bus[0] == booking_details["Bus_Number"]:
                    occu_seats = each_bus[-4]
                    remain_setails = each_bus[-3]
                    break
            occu_seats += booking_details["Total_Seats_Booked"] 
            remain_setails -= booking_details["Total_Seats_Booked"] 
            Update_record([occu_seats,"Occupied_seats",booking_details["Bus_Number"]],3)
            Update_record([remain_setails,"Remaining_Seats",booking_details["Bus_Number"]],3)
            with open("booking_details.dat","rb+") as dat_file:
                try:
                    reciept_details = load(dat_file)
                except:
                    reciept_details = []
            reciept_no = 601+len(reciept_details)
            final_details = [reciept_no] + [cust_uname] + list(booking_details.values())
            with open("booking_details.dat","wb+") as dat_file:
                reciept_details += final_details
                dump(reciept_details, dat_file)
            from main import front_page
            front_page()

    print("\t\tEnter Payment Method\n\t\t   --> 1)Cash\n\t\t   --> 2)Debit Card\n\t\t   --> 3)GPAY\n\t\t   --> 4)UPI")
    choice = input("Enter The Choice: ")
    while not(choice.isnumeric()) and (choice not in ["1","2","3","4"]):
        print("Invalid Choice")
        choice = input("Enter The Choice: ")
    else:
        choice = int(choice)
        if choice == 1:
            Transaction()
        elif choice == 2:
            card_dts = input("Enter The 16 Digit Card Number: ")
            exp = input("Expiry (mm/yyyy): ")
            cvv = input("Enter the CVV Number: ")
            while not(card_dts.isnumeric()) and not(cvv.isnumeric) and (len(card_dts.replace(" ","")) != 16) and (len(exp.replace("/","") != 6)) and (len(cvv) != 3):
                print("Invalid Entry!")
                card_dts = input("Enter The 16 Digit Card Number: ")
                exp = input("Expiry (mm/yyyy): ")
                cvv = input("Enter the CVV Number: ")
            else:
                Transaction()
        elif choice == 3:
            gpay = input("Enter the GPay Number: ")
            while not(gpay.isnumeric()) and len(gpay) != 10:
                print("Invalid Entry!")
                gpay = input("Enter the GPay Number: ")
            else:
                Transaction()
        else:
            upi = input("Enter the UPI ID: ")
            while "@" not in upi:
                print("Invalid Entry!")
                upi = input("Enter the UPI ID: ")
            else:
                Transaction()