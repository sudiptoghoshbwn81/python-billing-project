import mysql.connector
import QR_Code_Scanner

#connecting with mysql_database
conn_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dipannita81",
    database="retail_final_project")
cur_obj=conn_obj.cursor()

#Define function data_entry_sql
def data_entry_cust_details(full_name,address,ph_no_cust):
    sql_query="INSERT INTO cust_details(full_name,address,ph_no)VALUES (%s,%s,%s)"
    data=(full_name,address,ph_no_cust)

    try:
        cur_obj.execute(sql_query,data)
        print("New customer registration success")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error inserting data to MySQL:",e)
        conn_obj.rollback()

#define function data_retrieve_cust
def data_retrieve_cust(ph_no):
    query="select * from cust_details where ph_no=%s"
    result=None

    try:
        cur_obj.execute(query,(ph_no,))
        result=cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:",e)
        conn_obj.rollback()

    return result

#Define function data_retrieve_product_details
def data_retrieve_product_details(p_id):
    query="select * from product_details_table where p_id=%s"
    result=None

    try:
        cur_obj.execute(query,(p_id,))
        result=cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:",e)
        conn_obj.rollback()

    return result

#Define function data_entry_bill_details
def data_entry_BILL_DETAILS_TB(bill_id,c_id,p_id,p_name,quantity):
    sql_query="INSERT INTO BILL_DETAILS_TB(bill_id,C_ID, P_ID, P_NAME, QUANTITY)VALUES (%s,%s,%s,%s,%s)"
    data=(bill_id,c_id,p_id,p_name,quantity)

    try:
        cur_obj.execute(sql_query,data)
        print("Bill Details entry success...")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error inserting data to MySQL:",e)
        conn_obj.rollback()

#Define function data_retrieve_bill_summary
def data_retrieve_bill_summary_table():
    query=f"select max(bill_id) from bill_summary_table"
    result=None

    try:
        cur_obj.execute(query)
        result=cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:",e)
        conn_obj.rollback()

    return result

#Define function billing_operation
def billing_operation(c_id):
    print("Billing can be started now......")
    total_bill_value = 0
    while True:
        #p_id = input("Enter product id: ")
        p_id=QR_Code_Scanner.qr_code_scanner()
        p_details_from_db = data_retrieve_product_details(p_id)
        # print(p_details_from_db)
        product_price = float(p_details_from_db[-2])
        quantity = int(input("Enter quantity of the product:"))
        bill_id=data_retrieve_bill_summary_table()[0]
        data_entry_BILL_DETAILS_TB(int(bill_id+1),c_id, p_details_from_db[0], p_details_from_db[1],quantity)
        bill_value = product_price * quantity
        print("Bill Value:", bill_value)
        total_bill_value = total_bill_value + bill_value
        res = input(
            "Enter any key to continue or press 'q' to stop the billing and generate the final bill: ").strip().lower()
        if res == 'q':
            break
    print("Total Bill value:", total_bill_value)
    return total_bill_value

#Define function data_entry_sql
def data_entry_bill_summary_table(c_id,c_full_name,total_bill_value):
    sql_query="INSERT INTO bill_summary_table(c_id, c_name, total_bill_value)VALUES(%s,%s,%s)"
    data=(c_id,c_full_name,total_bill_value)

    try:
        cur_obj.execute(sql_query,data)
        print("Bill summary entry success")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error inserting data to MySQL:",e)
        conn_obj.rollback()

#Main Logic Starts from here
ph_no_cust=int(input("Please enter customer phone no: "))
cust_details_from_db=data_retrieve_cust(ph_no_cust)
if cust_details_from_db:
    print("existing customer: ",cust_details_from_db)
    total_bill_value=billing_operation(cust_details_from_db[0])
    c_id = cust_details_from_db[0]
    c_full_name = cust_details_from_db[1]
    data_entry_bill_summary_table(c_id,c_full_name,total_bill_value)
else:
    print("new customer....pls register ....")
    full_name = input("Please enter full name: ").strip().upper()
    address = input("Please enter address: ").strip().upper()
    data_entry_cust_details(full_name, address, ph_no_cust)
    cust_details_from_db = data_retrieve_cust(ph_no_cust)
    c_id = cust_details_from_db[0]
    c_full_name = cust_details_from_db[1]
    total_bill_value=billing_operation(c_id)
    data_entry_bill_summary_table(c_id,c_full_name,total_bill_value)
conn_obj.close()
