import streamlit as st

st.title("Simple Interest Calculator")

# Replace input() with Streamlit input fields
P=float(st.number_input('Enter the principle: '))
R=float(st.number_input("Enter the rate of Interest: "))
year=int(st.number_input('Enter no of years: ', step=1))
month=int(st.number_input('Enter no of months: ', step=1))

# ---- Backend code (UNCHANGED) ----
T=year+month/12
SI=P*R*T/100

# Replace print() with Streamlit output
st.write(f"Here is the simple interest: {SI:0.2f}")
st.write(f"Here is the Total amount: {P+SI:0.2f}")