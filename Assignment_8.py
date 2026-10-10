import streamlit as st

st.title("Shopping Cart Calculator")

# Replace input() with Streamlit inputs
p1=float(st.number_input("please enter the rate of first product: "))
q1=int(st.number_input("please enter the quantity of first product: ", step=1))

p2=float(st.number_input("please enter the rate of second product: "))
q2=int(st.number_input("please enter the quantity of second product: ", step=1))

p3=float(st.number_input("please enter the rate of third product: "))
q3=int(st.number_input("please enter the quantity of third product: ", step=1))

# ---- Backend code (UNCHANGED) ----
total_price=p1*q1+p2*q2+p3*q3

# Replace print() with Streamlit output
st.write(f"The total bill is {total_price:0.2f}")
