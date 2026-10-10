
import streamlit as st
import mysql.connector
import QR_Code_Scanner

# Page configuration
st.set_page_config(
    page_title="Retail Billing System",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Retail Billing System")
st.write("Customer Registration and Product Billing")

# Connecting with MySQL database
@st.cache_resource
def get_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dipannita81",
        database="retail_final_project"
    )

conn_obj = get_database_connection()


# Define function data_entry_sql
def data_entry_cust_details(full_name, address, ph_no_cust):
    sql_query = (
        "INSERT INTO cust_details(full_name,address,ph_no) "
        "VALUES (%s,%s,%s)"
    )
    data = (full_name, address, ph_no_cust)

    try:
        cur_obj = conn_obj.cursor()
        cur_obj.execute(sql_query, data)
        conn_obj.commit()
        cur_obj.close()
        return True

    except mysql.connector.Error as e:
        conn_obj.rollback()
        st.error(f"Error inserting data to MySQL: {e}")
        return False


# Define function data_retrieve_cust
def data_retrieve_cust(ph_no):
    query = "SELECT * FROM cust_details WHERE ph_no=%s"
    result = None

    try:
        cur_obj = conn_obj.cursor()
        cur_obj.execute(query, (ph_no,))
        result = cur_obj.fetchone()
        cur_obj.close()

    except mysql.connector.Error as e:
        conn_obj.rollback()
        st.error(f"Error retrieving customer data: {e}")

    return result


# Define function data_retrieve_product_details
def data_retrieve_product_details(p_id):
    query = "SELECT * FROM product_details_table WHERE p_id=%s"
    result = None

    try:
        cur_obj = conn_obj.cursor()
        cur_obj.execute(query, (p_id,))
        result = cur_obj.fetchone()
        cur_obj.close()

    except mysql.connector.Error as e:
        conn_obj.rollback()
        st.error(f"Error retrieving product data: {e}")

    return result


# Define function data_entry_BILL_DETAILS_TB
def data_entry_BILL_DETAILS_TB(
    bill_id, c_id, p_id, p_name, quantity
):
    sql_query = (
        "INSERT INTO BILL_DETAILS_TB"
        "(bill_id,C_ID,P_ID,P_NAME,QUANTITY) "
        "VALUES (%s,%s,%s,%s,%s)"
    )
    data = (bill_id, c_id, p_id, p_name, quantity)

    try:
        cur_obj = conn_obj.cursor()
        cur_obj.execute(sql_query, data)
        conn_obj.commit()
        cur_obj.close()
        return True

    except mysql.connector.Error as e:
        conn_obj.rollback()
        st.error(f"Error inserting bill details: {e}")
        return False


# Define function data_retrieve_bill_summary
def data_retrieve_bill_summary_table():
    query = "SELECT MAX(bill_id) FROM bill_summary_table"
    result = None

    try:
        cur_obj = conn_obj.cursor()
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        cur_obj.close()

    except mysql.connector.Error as e:
        conn_obj.rollback()
        st.error(f"Error retrieving bill summary: {e}")

    return result


# Define function data_entry_bill_summary_table
def data_entry_bill_summary_table(
    c_id, c_full_name, total_bill_value
):
    sql_query = (
        "INSERT INTO bill_summary_table"
        "(c_id,c_name,total_bill_value) VALUES (%s,%s,%s)"
    )
    data = (c_id, c_full_name, total_bill_value)

    try:
        cur_obj = conn_obj.cursor()
        cur_obj.execute(sql_query, data)
        conn_obj.commit()
        cur_obj.close()
        return True

    except mysql.connector.Error as e:
        conn_obj.rollback()
        st.error(f"Error inserting bill summary: {e}")
        return False


# Initialize Streamlit session state
if "customer" not in st.session_state:
    st.session_state.customer = None

if "bill_id" not in st.session_state:
    st.session_state.bill_id = None

if "total_bill_value" not in st.session_state:
    st.session_state.total_bill_value = 0.0

if "bill_items" not in st.session_state:
    st.session_state.bill_items = []

if "bill_completed" not in st.session_state:
    st.session_state.bill_completed = False


# Main Logic Starts from here
st.header("1. Customer Details")

with st.form("customer_form"):
    ph_no_cust = st.number_input(
        "Please enter customer phone number",
        min_value=1,
        step=1
    )

    customer_submitted = st.form_submit_button(
        "Find Customer"
    )

if customer_submitted:
    cust_details_from_db = data_retrieve_cust(
        int(ph_no_cust)
    )

    if cust_details_from_db:
        st.session_state.customer = cust_details_from_db
        st.session_state.bill_id = None
        st.session_state.total_bill_value = 0.0
        st.session_state.bill_items = []
        st.session_state.bill_completed = False

        st.success("Existing customer found.")

    else:
        st.session_state.customer = None
        st.session_state.registration_phone = int(ph_no_cust)
        st.info("New customer. Please register.")


# New customer registration
if (
    "registration_phone" in st.session_state
    and st.session_state.customer is None
):
    with st.form("registration_form"):
        full_name = st.text_input("Full Name")
        address = st.text_area("Address")

        register_submitted = st.form_submit_button(
            "Register Customer"
        )

    if register_submitted:
        if not full_name.strip() or not address.strip():
            st.warning("Please enter the full name and address.")

        else:
            success = data_entry_cust_details(
                full_name.strip().upper(),
                address.strip().upper(),
                st.session_state.registration_phone
            )

            if success:
                cust_details_from_db = data_retrieve_cust(
                    st.session_state.registration_phone
                )

                if cust_details_from_db:
                    st.session_state.customer = cust_details_from_db
                    st.session_state.bill_id = None
                    st.session_state.total_bill_value = 0.0
                    st.session_state.bill_items = []
                    st.session_state.bill_completed = False

                    del st.session_state.registration_phone

                    st.success("New customer registration successful!")
                    st.rerun()


# Billing operation
if st.session_state.customer:
    cust_details_from_db = st.session_state.customer

    c_id = cust_details_from_db[0]
    c_full_name = cust_details_from_db[1]

    st.divider()
    st.header("2. Billing")

    st.write(f"**Customer ID:** {c_id}")
    st.write(f"**Customer Name:** {c_full_name}")

    if not st.session_state.bill_completed:

        # Generate the bill ID once per billing session
        if st.session_state.bill_id is None:
            bill_summary = data_retrieve_bill_summary_table()

            if bill_summary is None or bill_summary[0] is None:
                st.session_state.bill_id = 1
            else:
                st.session_state.bill_id = int(
                    bill_summary[0] + 1
                )

        st.write(
            f"**Bill ID:** {st.session_state.bill_id}"
        )

        st.info(
            "Keep the camera ready. Click Scan Product "
            "to activate your existing QR code scanner."
        )

        quantity = st.number_input(
            "Enter quantity of the product",
            min_value=1,
            value=1,
            step=1,
            key="product_quantity"
        )

        if st.button("📷 Scan Product", type="primary"):
            try:
                # Existing QR scanner function
                p_id = QR_Code_Scanner.qr_code_scanner()

                if p_id is None:
                    st.warning("No product QR code was scanned.")

                else:
                    p_details_from_db = (
                        data_retrieve_product_details(p_id)
                    )

                    if p_details_from_db:
                        product_price = float(
                            p_details_from_db[-2]
                        )

                        product_id = p_details_from_db[0]
                        product_name = p_details_from_db[1]

                        bill_value = product_price * int(quantity)

                        success = data_entry_BILL_DETAILS_TB(
                            int(st.session_state.bill_id),
                            c_id,
                            product_id,
                            product_name,
                            int(quantity)
                        )

                        if success:
                            st.session_state.total_bill_value += (
                                bill_value
                            )

                            st.session_state.bill_items.append({
                                "Product ID": product_id,
                                "Product Name": product_name,
                                "Price": product_price,
                                "Quantity": int(quantity),
                                "Bill Value": bill_value
                            })

                            st.success(
                                f"Product scanned: {product_name}"
                            )

                            st.write(
                                f"Product price: {product_price:.2f}"
                            )
                            st.write(
                                f"Quantity: {int(quantity)}"
                            )
                            st.write(
                                f"Bill value: {bill_value:.2f}"
                            )

                            st.rerun()

                    else:
                        st.error(
                            "Product not found in the database."
                        )

            except Exception as e:
                st.error(f"QR scanner error: {e}")

        # Display current bill items
        if st.session_state.bill_items:
            st.subheader("Current Bill Items")
            st.dataframe(
                st.session_state.bill_items,
                use_container_width=True,
                hide_index=True
            )

            st.subheader(
                f"Total Bill Value: "
                f"{st.session_state.total_bill_value:.2f}"
            )

        if st.button("Finish Billing and Generate Bill"):
            success = data_entry_bill_summary_table(
                c_id,
                c_full_name,
                st.session_state.total_bill_value
            )

            if success:
                st.session_state.bill_completed = True
                st.rerun()

    else:
        st.success("Billing completed successfully!")

        st.subheader("Final Bill")
        st.write(f"**Bill ID:** {st.session_state.bill_id}")
        st.write(f"**Customer ID:** {c_id}")
        st.write(f"**Customer Name:** {c_full_name}")

        if st.session_state.bill_items:
            st.dataframe(
                st.session_state.bill_items,
                use_container_width=True,
                hide_index=True
            )

        st.subheader(
            f"Total Bill Value: "
            f"{st.session_state.total_bill_value:.2f}"
        )

        if st.button("Start New Bill"):
            st.session_state.customer = None
            st.session_state.bill_id = None
            st.session_state.total_bill_value = 0.0
            st.session_state.bill_items = []
            st.session_state.bill_completed = False
            st.rerun()
