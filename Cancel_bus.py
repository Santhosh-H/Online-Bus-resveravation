def Cancel_Bus(CUST_ID):
    from pickle import load,dump 
    from tabulate import tabulate
    with open("booking_details.dat","rb+") as booking_details_dat:
        all_reciept_details = load(booking_details_dat)
    cust_reciepts = []
    for each_reciept in all_reciept_details:
        if int(each_reciept[1]) == int(CUST_ID):
            cust_reciepts.append(each_reciept)
    if len(cust_reciepts) == 0:
        print("\t\tYou Dont Have Any Bookings Go AHEAD AND Book now\n\t\t\tMINIMUM SEATS AVAILABLE")
    else:
        print(tabulate(cust_reciepts, headers=["Recipet Number","Customer ID","BUS Number","Source Location","Destination Location","Source Date","Destination Date","Price(One Seat)","Total Seats Booked","Total Price"], tablefmt="grid"))
        entr_recipet = input("\t\tEnter the Recipet Number: ")
        while not(entr_recipet.isnumeric()):
            entr_recipet = input("\t\tEnter the Recipet Number: ")
        else:
            for each_reciept in all_reciept_details:
                if int(entr_recipet) == each_reciept[0]:
                    print(f"Cancelled bus Reciept Number {each_reciept[0]}")
                    all_reciept_details.remove(each_reciept)
                    from main import front_page
                    front_page()
                    break
def delete_cust_details(Custid):
    from sql_python_connection import Delete_record
    from tqdm import tqdm
    loop = tqdm(total=10000, position=0, leave=False)
    for k in range(10000):
        loop.set_description("Wiping Your Records".format(k))
        loop.update(1)
    loop.close()
    Delete_record(table_number=3,etr_p_key=Custid)
    from main import front_page
    front_page()
