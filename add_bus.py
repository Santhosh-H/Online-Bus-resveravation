from tabulate import tabulate
#Add Bus In Mysql
Indian_States_and_Union_Teritories = [
										"Andhra Pradesh",
										"Arunachal Pradesh ",
										"Assam","Bihar",
										"Chhattisgarh",
										"Goa",
										"Gujarat",
										"Haryana",
										"Himachal Pradesh",
										"Jammu and Kashmir",
										"Jharkhand",
										"Karnataka",
										"Kerala",
										"Madhya Pradesh",
										"Maharashtra",
										"Manipur",
										"Meghalaya",
										"Mizoram",
										"Nagaland",
										"Odisha",
										"Punjab",
										"Rajasthan",
										"Sikkim",
										"Tamil Nadu",
										"Telangana",
										"Tripura",
										"Uttar Pradesh",
										"Uttarakhand",
										"West Bengal",
										"Andaman and Nicobar Islands",
										"Chandigarh",
										"Dadra and Nagar Haveli",
										"Daman and Diu",
										"Lakshadweep",
										"National Capital Territory of Delhi",
										"Puducherry"
													]

def Add_Bus():
	#Importing Modules
	from sql_python_connection import fetch_details_from_table,add_record_table
	from tabulate import tabulate #Install This in your Computer using command pip install tabulate
	#Details of Bus Stored in a Variable
	all_bus_details = fetch_details_from_table(3)
	#header for the Places (Source/Destination)
	final_list = []
	for i in range(len(Indian_States_and_Union_Teritories)):
		final_list.append([i+1,Indian_States_and_Union_Teritories[i].upper()])
	header = ["Enter","Places (Source/Destination)"]
	#Printing the list in table form
	print(tabulate(headers=header, tabular_data=final_list, tablefmt='grid'))
	#Input Header
	input_header = ['Bus Name','Source','Destination','Total Seats','Price(Per_Seat)','Time Gap']
	#Empty List for add all Inputed Values
	each_value = []
	#Checking the Specific Properties of the header
	for i in range(len(input_header)):
		inp = input(f"\t\tEnter {input_header[i]}: ")
		if inp == "":
			print("\t\tEnter Correctly")
			break
		else:
			each_value.append(inp) 
	#Giving appropreate error message
	if not(each_value[1].isnumeric()) and not(each_value[2].isnumeric()) and not(each_value[3].isnumeric()) and not(each_value[4].isnumeric()) and not(each_value[5].isnumeric()): #Checking for all Error
		print("\t\tInput Not Valid!!")
		print("_"*157)
		each_value = []
		Add_Bus()
	else: #If all The conditions satifies
		occupied_seats = 0   #Occupied Seats
		remaining_seats = each_value[3]             #Remaining Seats
		#Making the corresponding types
		for i in range(len(final_list)):
			if int(final_list[i][0]) == int(each_value[1]):
				each_value[1] = str(final_list[i][1])
				break
		for i in range(len(final_list)):
			if int(final_list[i][0]) == int(each_value[2]):
				each_value[2] = str(final_list[i][1])
				break
		each_value[3] = int(each_value[3])
		each_value[4] = int(each_value[4])
		each_value[5] = int(each_value[5])
		#Creating Bus Number
		if len(all_bus_details) < 10 :
			Bus_No = f'{each_value[2][:2]}'+ '0' + str(len(all_bus_details))
		else:
			Bus_No = f'{each_value[2][:2]}'+ str(len(all_bus_details))
		#Final List or adding details into SQL Table
		add_values = [Bus_No] + each_value[:4] + [occupied_seats,remaining_seats] + each_value[4:]
		#Adding into The Table
		add_record_table(3, add_values)
		#Print Message for Succeful Registration
		print(f"\t\tThe Bus Number is {Bus_No}")
		print("\t\tBus Registered Successful!")

def change_records(tabel_number):
	from sql_python_connection import  fetch_table_header, Update_record,fetch_details_from_table
	bus_details = fetch_details_from_table(3)
	table_headers = fetch_table_header(3)
	bus_no = input("\t\tEnter The bus Number: ")
	for i in bus_details:
		if str(i[0]) == str(bus_no):
			header = ["Enter","What you want to Change"]
			show_list = []
			for l in range(len(table_headers)):
				show_list.append([l+1,table_headers[l]])
			print(tabulate(headers=header, tabular_data=show_list, tablefmt='grid'))
			choice = input("\t\tEnter Your Choice --> ")
			for j in range(len(table_headers)):
				if int(choice)-1 == j:
					if not(j < 4):
						try:
							changed_input = int(input("\t\tEnter to Change: "))
						except:
							print("\t\tEnter Choice Correctly")
					else:
						changed_input = input("\t\tEnter to Change: ")
					update_list = [changed_input,table_headers[j],bus_no]
					print(update_list)
					Update_record(data_list=update_list,table_number=tabel_number)
					break
			else:
				print("\tEnter Choice Correctly")
				change_records(tabel_number)
			break
		else:
			print("\t\tEnter The bus Number Correctly")
			change_records(3)


