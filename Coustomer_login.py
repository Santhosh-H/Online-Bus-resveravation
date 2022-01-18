#Customer Login Page
def old_Customer_Login():
	#Importing Modules
	from sql_python_connection import fetch_details_from_table
	from table import tableprinting
	#Storing all Customer Details in a Varible
	all_cust_details = fetch_details_from_table(1)
	#Asking User Name Input
	login_input = input("\t\tEnter Your User Name or Customer Id: ")
	#Checking For Username in Total Database
	for record in all_cust_details:
		if login_input.lower() == str(record[0]) or login_input.lower() == record[1]:
				#Prompting For Password
				password = input("\t\tEnter your password: ")
				#Checking For Password
				if password == record[-1]:
					print("_"*157)
					header = ["--> Book a Bus",
							  "--> Cancel a Bus",
							  "--> Remove Your Details"]
					tableprinting(f"Hello {record[1]}",header)
					choice1 = input("\t\tEnter your choice")
					while not(choice1.isnumeric()) and choice1 not in [str(i) for i in range(1,4)]:
						print("Invalid Choice! ")
						choice1 = input("\t\tEnter your choice")
					else:
						choice1 = int(choice1)
						if choice1 == 1:
							from book_bus import book_bus
							book_bus()
						elif choice1 == 2:
							from Cancel_bus import Cancel_Bus
							Cancel_Bus(record[0])
						else:
							from Cancel_bus import delete_cust_details
							delete_cust_details(record[0])
					break
				#Display Aprropriate Error
				else:
					print("\t\tWrong Password")
					old_Customer_Login()
					break
	#Display Aprropriate Error
	else:
		print("\t\tUsername Not Found")
		old_Customer_Login()

#Creating New Costomer Page
def Customer_Sign_up():
	#Importing the Modules
	from sql_python_connection import fetch_details_from_table,add_record_table
	#All Detils in Customer table stored in a variable
	all_customer_details = fetch_details_from_table(1)
	#Headers for Input
	header = ["Name",
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
		Customer_Sign_up()
	elif each_value[2].lower() not in ["male","m","female","f","transgender","t"]: #Checking for gender
		print("\t\tGender Not Valid!!")
		print("_"*157)
		each_value = []
		Customer_Sign_up()
	elif not('@' in each_value[3]): #Checking for Correct Email Address
		print("\t\tEmail Address Not Valid!!")
		print("_"*157)
		each_value = []
		Customer_Sign_up()
	elif not(each_value[-1].isalnum()):#Checking for both alphabet and numeric contain password
		print("\t\tPassword Myst Contain both Alphabet and Numeric")
		print("_"*157)
		each_value = []
		Customer_Sign_up()
	else: #If all The conditions satifies
		#Creating Customer Number
		Customer_No = 401 + len(all_customer_details)
		#Making the corresponding int types form string types
		each_value[1] = int(each_value[1])
		#Final List or adding details into SQL Table
		add_values = [Customer_No] + each_value
		#Adding into The Table
		add_record_table(1, add_values)
		#email verification
		from random import randint
		otp_rdm = randint(100,999)
		from mailsend import sending_mail
		sending_mail(to_adress=each_value[3], subject="Customer Sign Up Verification", body=f"Your One Time Verification Code is {otp_rdm} ")
		otp_prompt = input("Enter The OTP Recived in your Given Email Address: ")
		while not(otp_prompt.isnumeric()) and int(otp_rdm) != int(otp_prompt):
			otp_rdm = randint(100,999)
			sending_mail(to_adress=each_value[3], subject="Customer Sign Up Verification", body=f"Your One Time Verification Code is {otp_rdm} ")
			otp_prompt = input("Enter The New OTP Recived in your Given Email Address: ")
		else:
			#Print Message for Succeful Registration
			print(f"\t\tYour Customer ID is {Customer_No}")
			print("\t\tYour Registration is Successful!")
#Main Login Page
def Custormer_Login():
	#Importing the Modules
	from table import tableprinting
	#Header For the Choice
	header = ["New Login".upper(), 
			  "existing Login".upper(),
			  "back".upper(),
			  "exit".upper()]

	#Printing The Choice
	tableprinting("Customer Login Page",header)
	#Asking Choice
	choice = input("\t\tEnter Choice -->")
	#New Login
	if choice == '1':
		print("_"*157)
		Customer_Sign_up()
	#Existing Login
	elif choice == '2':
		old_Customer_Login()
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
