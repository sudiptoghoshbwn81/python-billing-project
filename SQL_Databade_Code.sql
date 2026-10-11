--- Retail_Billing _Final_Projrct

-- Creating Database
create database retail_final_project ;
use retail_final_project;

-- Creating Customer details table and inserting records
CREATE TABLE cust_details (
    cust_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(100) NOT NULL,
    address VARCHAR(255),
    ph_no bigint not null,
    registration_date_time DATETIME not null DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO cust_details
(full_name, address, ph_no, registration_date_time)
VALUES
('Rahul Sharma', 'Mumbai', '9876543210', '2026-07-22 09:30:00');

-- Creating product details table and inserting records
CREATE TABLE product_details_table (
    p_id INT PRIMARY KEY AUTO_INCREMENT,
    p_names VARCHAR(100) NOT NULL,
    p_price DECIMAL(10,2) NOT NULL,
    stock_on_hand INT NOT NULL DEFAULT 0
);

INSERT INTO product_details_table (p_names, p_price, stock_on_hand)
VALUES
('Basmati Rice 5kg', 650.00, 50),
('Sona Masoori Rice 5kg', 480.00, 40),
('Wheat Flour (Atta) 10kg', 520.00, 60),
('Maida 1kg', 65.00, 100),
('Suji (Semolina) 1kg', 55.00, 80),
('Besan 1kg', 95.00, 75),
('Toor Dal 1kg', 180.00, 90),
('Moong Dal 1kg', 145.00, 85),
('Masoor Dal 1kg', 130.00, 70),
('Chana Dal 1kg', 110.00, 65),
('Urad Dal 1kg', 155.00, 60),
('Rajma 1kg', 175.00, 55),
('Kabuli Chana 1kg', 165.00, 70),
('Black Chana 1kg', 120.00, 75),
('Poha 1kg', 70.00, 90),
('Flattened Rice Premium', 85.00, 60),
('Sugar 1kg', 48.00, 150),
('Jaggery 1kg', 70.00, 80),
('Salt 1kg', 25.00, 200),
('Rock Salt 1kg', 55.00, 90),
('Sunflower Oil 1L', 165.00, 120),
('Mustard Oil 1L', 190.00, 100),
('Groundnut Oil 1L', 210.00, 80),
('Ghee 1L', 620.00, 45),
('Butter 500g', 295.00, 50),
('Milk Powder 500g', 340.00, 40),
('Tea Powder 1kg', 540.00, 70),
('Instant Coffee 200g', 420.00, 55),
('Turmeric Powder 200g', 45.00, 120),
('Red Chilli Powder 200g', 80.00, 100),
('Coriander Powder 200g', 60.00, 90),
('Cumin Seeds 200g', 95.00, 75),
('Mustard Seeds 200g', 40.00, 85),
('Black Pepper 100g', 120.00, 60),
('Garam Masala 100g', 95.00, 70),
('Cinnamon 100g', 75.00, 50),
('Cloves 100g', 130.00, 40),
('Cardamom 100g', 280.00, 35),
('Bay Leaf 100g', 45.00, 50),
('Tamarind 500g', 90.00, 60),
('Cashew Nuts 500g', 520.00, 30),
('Almonds 500g', 480.00, 35),
('Raisins 500g', 260.00, 40),
('Peanuts 1kg', 140.00, 80),
('Coconut Oil 1L', 340.00, 50),
('Soy Chunks 1kg', 220.00, 60),
('Papad 500g', 110.00, 70),
('Pickle Mango 500g', 150.00, 45),
('Tomato Ketchup 1kg', 140.00, 55),
('Vermicelli 500g', 65.00, 75);

-- -- Creating bill summary table and inserting records
CREATE TABLE bill_summary_table (
    bill_id INT PRIMARY KEY AUTO_INCREMENT,
    c_id INT NOT NULL,
    c_name VARCHAR(100) NOT NULL,
    total_bill_value DECIMAL(10,2) NOT NULL,
    bill_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO bill_summary_table
(c_id, c_name, total_bill_value, bill_timestamp)
VALUES
(1, 'Rahul Sharma', 1250.50, '2026-07-23 10:15:30');

INSERT INTO bill_summary_table
(c_id, c_name, total_bill_value, bill_timestamp)
VALUES
(2, 'Priya Singh', 890.75, '2026-07-23 10:45:15');

INSERT INTO bill_summary_table
(c_id, c_name, total_bill_value, bill_timestamp)
VALUES
(3, 'Amit Das', 2150.00, '2026-07-23 11:20:40');

INSERT INTO bill_summary_table values
(c_id, c_name, total_bill_value, bill_timestamp);

INSERT INTO bill_summary_table
(c_id, c_name, total_bill_value, bill_timestamp)
VALUES
(4, 'Neha Verma', 540.25, '2026-07-23 12:10:55');

INSERT INTO bill_summary_table
(c_id, c_name, total_bill_value, bill_timestamp)
VALUES
(5, 'Rohan Gupta', 3675.90, '2026-07-23 13:05:20');

-- Creating bill details table and inserting reords
CREATE TABLE BILL_DETAILS_TB (
    SL_NO INT AUTO_INCREMENT PRIMARY KEY,
    bill_id int not null,
    C_ID INT NOT NULL,
    P_ID INT NOT NULL,
    P_NAME VARCHAR(500) NOT NULL,
    QUANTITY INT NOT NULL,
    `TIMESTAMP` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO BILL_DETAILS_TB (bill_id,C_ID, P_ID, P_NAME, QUANTITY)
VALUES (10, 1001, 501, 'Basmati Rice', 2);

-- Finding latest bill id
select max(bill_id) from bill_summary_table;

select * from cust_details;
select * from product_details_table;
select * from bill_summary_table;
select * from BILL_DETAILS_TB;

-- checking total bill by bill id 
with CTE1 as
(select pd.p_id,pd.p_names, bt.bill_id,pd.p_price* bt.QUANTITY as Total_cost_br from product_details_table pd
inner join BILL_DETAILS_TB bt
on pd.p_id=bt.p_id),
CTE2 as (select bill_id,sum(Total_cost_br) as Total_cost from CTE1
group by bill_id order by Total_cost desc)
select * from CTE2



