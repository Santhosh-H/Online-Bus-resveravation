#Creating a Front Page for Online Bus booking
def front_page():
	#Importing the Modules
	from table import tableprinting
	from Admin_Login import Admin_Login
	from Coustomer_login import Custormer_Login
	#Header For the Choice
	heading1 = ["Customer Login",
				"Administration Login",
				"Exit"]
	#Printing The Choice
	tableprinting("Welcome to Online Bus Booking",heading1)
	#Asking Choice
	choice = input("\tEnter Choice --> ")
	#Customer Login
	if choice == '1':
		print("_"*157)
		Custormer_Login()
	#Admin Login
	elif choice == '2':
		Admin_Login()
	#Exit Button
	elif choice == '3' :
		print("_"*157)
		print("\t\tThank Your visiting or page")
		quit()
	else:
		print("\t\tEnter Choice Correctly")


front_page()
