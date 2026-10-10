import streamlit as st

st.title("Temperature Conversion")

# Frontend input instead of input()
Fahrenheit_Temp = st.number_input("Enter the temperature in Fahrenheit")

# --- Backend code (kept same) ---
Celsius_Temp=(Fahrenheit_Temp-32)*5/9

# Frontend output instead of print()
st.write(f"Temperature in celsius is {Celsius_Temp:.3f}°C")
