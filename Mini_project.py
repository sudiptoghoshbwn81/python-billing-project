#Database connection details
import mysql.connector

conn_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dipannita81",
    database="feb_2026_login_auth_mini_proj")
cur_obj=conn_obj.cursor()

#Define function data_entry_sql
def data_entry_sql(full_name,address,ph_no,user_id,password):
    sql = "INSERT INTO CUST_DETAILS (full_name,address,ph_no,user_id,password) VALUES (%s, %s, %s, %s, %s)"
    data = (full_name,address,ph_no,user_id,password)

    try:
        cur_obj.execute(sql, data)
        print("CUSTOMER ENTRY SUCCESSFUL.")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error inserting data to MySQL:", e)
        conn_obj.rollback()

#Define function data_retrieve
def data_retrieve(cus_user_id):
    query = f"select * from CUST_DETAILS WHERE USER_ID='{cus_user_id}'"

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()
    return result

def login():
    cus_user_id = input("Enter your user id: ")
    data_retrieve(cus_user_id)
    cus_details_from_db = data_retrieve(cus_user_id)
    if cus_details_from_db:
        password_db = cus_details_from_db[-1]
        cus_password = input("Enter your password: ")
        if password_db == cus_password:
            print("Access Granted")
        else:
            print("Wrong userid password try again...")
    else:
        print("Userid not present in database,try again......")


#main codes starts here.......
print("Welcome to demo app......")
res=input("New user registration\n1. New user login\n2. Existing user login\nselect from here: ")
if res=='1':
    print("New user registration")
    full_name=input("Enter your full name: ")
    address=input("Enter your address: ")
    ph_no=(input("Enter your phone no: ")).strip()
    while True:
        user_id=input("Set your user id: ")
        user_details=data_retrieve(user_id)
        if not user_details:
            password = input("Set your password: ")
            data_entry_sql(full_name, address, ph_no, user_id, password)
            login()
            break
        else:
            print("User id present try again...")
elif res=='2':
    print("New user login")
    login()

else:
    print("Invalid entry. Please select from above menu...")
conn_obj.close()