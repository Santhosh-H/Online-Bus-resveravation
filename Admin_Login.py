#Admin Login Page
from tabulate import tabulate
from table import tableprinting
def Admin_Sign_up():
	#Importing the Modules
	from sql_python_connection import fetch_details_from_table,add_record_table,fetch_table_header,Update_record
	#All Detils in Admin table stored in a variable
	all_admin_details = fetch_details_from_table(2)
	#Headers for Input
	header = ["Admin Name",
			  "Age",
			  "Gender",
			  "Email Address",
			  "Password"]
	#Empty List for add all Inputed Values
	each_value = []
	#Checking the Specific Properties of the header
	for i in range(len(header)):
		inp = input(f"\t\tEnter {header[i]}: ")
		if inp == "":
			print("\t\tEnter Correctly")
			break
		else:
			each_value.append(inp) 
	#Giving appropreate error message
	if not(each_value[1].isnumeric()): #Checking for age
		print("\t\tAge Not Valid!!")
		print("_"*157)
		each_value = []
		Admin_Sign_up()
	elif each_value[2].lower() not in ["male","m","female","f","transgender","t"]: #Checking for gender
		print("\t\tGender Not Valid!!")
		print("_"*157)
		each_value = []
		Admin_Sign_up()
	elif not('@' in each_value[3]): #Checking for Correct Email Address
		print("\t\tEmail Address Not Valid!!")
		print("_"*157)
		each_value = []
		Admin_Sign_up()
	elif not(each_value[-1].isalnum()):#Checking for both alphabet and numeric contain password
		print("\t\tPassword Myst Contain both Alphabet and Numeric")
		print("_"*157)
		each_value = []
		Admin_Sign_up()
	else: #If all The conditions satifies
		#Creating Admin Number
		Admin_No = 5001 + len(all_admin_details)
		#Making the corresponding int types form string types
		each_value[1] = int(each_value[1])
		#Final List or adding details into SQL Table
		add_values = [Admin_No] + each_value
		#Adding into The Table
		add_record_table(2, add_values)
		#Print Message for Succeful Registration
		print(f"\t\tYour Admin ID is {Admin_No}")
		print("\t\tYour Registration is Successful!")
def Old_Admin():
	#Importing the Modules
	from sql_python_connection import fetch_details_from_table,Delete_record,Update_record,fetch_table_header
	from add_bus import change_records
	#All Detils in Admin table stored in a variable
	all_admin_details = fetch_details_from_table(2)
	user_inp = input("Enter Admin UserName or Admin Number: ")
	for records in all_admin_details:
		if str(records[0]) == str(user_inp) or str(records[1]).lower() == str(user_inp).lower():
			passwd = input("Enter your password: ")
			if records[-1] == passwd:
				print("_"*157)
				header = ["--> Add a Bus",
						  "--> Delete a Bus",
						  "--> Change Bus Details",
						  "--> View All Bus Details"]
				tableprinting(f"Hello {records[1]}",header)
				choice = input("\t\tEnter Your Choice --> ")
				if choice == '1':
					from add_bus import Add_Bus
					Add_Bus()
				elif choice == '2':
					all_bus_details = fetch_details_from_table(3)
					bus_no = input("Enter The bus_no to delete The bus")
					for record in all_bus_details:
						if record[0] == bus_no:
							Delete_record(bus_no,3)
							break
					else:
						print("\t\tBus No Invalid!")
				elif choice == '3':
					change_records(3)
					break
				elif choice == '4':
					header = fetch_table_header(3)
					data = fetch_details_from_table(3)
					print(tabulate(tabular_data=data, headers=header, tablefmt='grid'))
					break
				else:
					print("\t\t\tEnter The choice Correctly")
					Old_Admin()
			else:
				print("\t\tIncorrect Password")
				Old_Admin()
	else:
		print("\t\tUsername Not Found")
		Old_Admin()
def Admin_Login():
	#Importing the Modules
	from table import tableprinting
	#Header For the Choice
	header = ["NEW ADMIN",
			  "EXISTING ADMIN",
			  "BACK",
			  "EXIT"]
	#Printing The Choice
	tableprinting("Admin Login",header)
	#Asking Choice
	choice = input("\t\tEnter Choice -->")
	#New Admin
	if choice == '1':
		Admin_Sign_up()
	#Existing Admin
	elif choice == '2':
		Old_Admin()
	#Back Button
	elif choice == '3':
		from main import front_page
		print("_"*157)
		front_page()
	#Exit Button
	elif choice == '4':
		print("\t\tThank Your visiting or page")
		quit()
	#Error Message
	else:
		print("\t\tEnter Choice Correctly")
