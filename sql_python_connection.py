#Connecting Mysql with Python
import mysql.connector
#Specify the Mysql Password 
sql_password = "Give Your Mysql Password"
#Getting Details From Table
def Create_Required_Tables():
	#Connecting to Mysql
	conn = mysql.connector.connect(host="localhost",
						  user="root",
						  passwd=sql_password)  

	mycur = conn.cursor()
	#Creating a Database if does not exit
	mycur.execute("CREATE DATABASE IF NOT EXISTS Online_Bus_Booking;")
	#Using Database
	mycur.execute("USE Online_Bus_Booking;")
	#Creating a Customer details Table
	mycur.execute("""CREATE TABLE IF NOT EXISTS Customer_details(
					 				Customer_No int PRIMARY KEY,
									Customer_Name varchar(40),
									Age int,
									Gender varchar(12),
									Email_address varchar(50),
									Password varchar(50)
									);""")
	#Comiting The Changes
	conn.commit()
	#Creating a Admin details Table
	mycur.execute("""CREATE TABLE IF NOT EXISTS Admin_details(
					 				Admin_No int PRIMARY KEY,
									Admin_Name varchar(40),
									Age int,
									Gender varchar(12),
									Email_address varchar(50),
									Password varchar(50)
									);""")
	#Comiting The Changes
	conn.commit()
	#Creating a Bus details Table
	mycur.execute("""CREATE TABLE IF NOT EXISTS Bus_details(
					 				Bus_No varchar(5) PRIMARY KEY,
									Bus_Name varchar(40),
									Source varchar(35),
									Destination varchar(35),
									Total_Seats int,
									Occupied_seats int,
									Remaining_Seats int,
									Price_Per_Seat bigint,
									Time_Gap int
									);""")
	#Comiting The Changes
	conn.commit()
	conn.close()
def fetch_details_from_table(table_number):
	Create_Required_Tables()
	#Connecting to Mysql
	conn = mysql.connector.connect(host="localhost",
						  user="root",
						  passwd=sql_password,
						  database="Online_Bus_Booking")  

	mycur = conn.cursor()
	# 1 --> Customer_details 
	# 2 --> Admin_detail
	# 3 --> Bus_details
	if table_number == 1:
		table_name = "Customer_details"
	elif table_number == 2:
		table_name = "Admin_details"
	elif table_number == 3:
		table_name = "Bus_details"
	try:
		mycur.execute(f"SELECT * FROM {table_name};")
		records = mycur.fetchall()
		conn.close() #Closing the Sql Server
		#Converting the records from Tuple to List
		list_record = []
		for i in records:
			list_record.append(list(i))
		#Retuning the Value
		return list_record
	except:
		#If the Table is Empty
		return []
def add_record_table(table_number,list_details):
	Create_Required_Tables()
	#Connecting to Mysql
	conn = mysql.connector.connect(host="localhost",
						  user="root",
						  passwd=sql_password,database='Online_bus_booking')  

	mycur = conn.cursor()
	# 1 --> Customer_details 
	# 2 --> Admin_details
	if table_number == 1:
		table_name = "Customer_details"
		tabel_len = 6
	elif table_number == 2:
		table_name = "Admin_details"
		tabel_len = 6
	elif table_number == 3:
		table_name = "Bus_details"
		tabel_len = 9
	#Inserting into Table
	command = f"INSERT INTO {table_name} VALUES ("
	#Making the Insert Command More Efficiently
	for i in range(tabel_len):
		if not(type(list_details[i]) == str):
			if not(i == (tabel_len - 1)):
				command += f"{list_details[i]},"
			else:		
				command += f"{list_details[i]});"
		else:
			if not(i == (tabel_len - 1)):
				command += f"'{list_details[i]}',"
			else:		
				command += f"'{list_details[i]}');"
	mycur.execute(command)
	#Commiting the Changes
	conn.commit()
	#Closing the Sql Server
	conn.close() 
def Delete_record(etr_p_key,table_number):
	Create_Required_Tables()
	#Connecting to Mysql
	conn = mysql.connector.connect(host="localhost",
						  user="root",
						  passwd=sql_password,database='Online_bus_booking')  

	mycur = conn.cursor()
	# 1 --> Customer_details 
	# 2 --> Admin_detail
	# 3 --> Bus_details
	if table_number == 1:
		table_name = "Customer_details"
		primary_key = "Customer_No"
	elif table_number == 2:
		table_name = "Admin_details"
		primary_key = "Admin_No"
	elif table_number == 3:
		table_name = "Bus_details"
		primary_key = "Bus_No"
	
	mycur.execute(f"DELETE FROM {table_name} WHERE {primary_key} = {etr_p_key};")
	conn.commit()
	print(f"\t\tDeleted {table_name} OF {primary_key}: {etr_p_key}")
	conn.close() #Closing the Sql Server
def Update_record(data_list,table_number):
	Create_Required_Tables()
	#Connecting to Mysql
	conn = mysql.connector.connect(host="localhost",
						  user="root",
						  passwd=sql_password,database='Online_bus_booking')  

	mycur = conn.cursor()
	# 1 --> Customer_details 
	# 2 --> Admin_detail
	# 3 --> Bus_details
	if table_number == 1:
		table_name = "Customer_details"
	elif table_number == 2:
		table_name = "Admin_details"
	elif table_number == 3:
		table_name = "Bus_details"
	
	command = f"UPDATE {table_name} SET {data_list[-2]} = "
	for i in range(len(data_list)-2):
		if type(data_list[i]) == int:
			command += "{}".format(data_list[i])
			command += '= '
		else:
			command += "'{}'".format(data_list[i])
			command += '= '
	command = command[:-2] + f" WHERE bus_no = '{data_list[-1]}';"
	mycur.execute(command)
	conn.commit()
	print(f"\t\tChanged details Of Bus No: {data_list[-1]} (Changed:{data_list[i]})")
	conn.close() #Closing the Sql Server
def fetch_table_header(table_number):
	Create_Required_Tables()
	#Connecting to Mysql
	conn = mysql.connector.connect(host="localhost",
						  user="root",
						  passwd=sql_password,database='Online_bus_booking')  

	mycur = conn.cursor()
	# 1 --> Customer_details 
	# 2 --> Admin_detail
	# 3 --> Bus_details
	if table_number == 1:
		table_name = "Customer_details"
	elif table_number == 2:
		table_name = "Admin_details"
	elif table_number == 3:
		table_name = "Bus_details"
	mycur.execute(f"DESCRIBE {table_name}")
	fetched_data = mycur.fetchall()
	data = []
	for i in fetched_data:
		data.append(i[0])
	return data
