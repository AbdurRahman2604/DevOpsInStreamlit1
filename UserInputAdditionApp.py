import streamlit as st
# Input values
a = st.number_input("Enter value for a ")
b = st.number_input("Enter value for b")
c = st.number_input("Enter value for c")

d = st.text_input("Enter value for d (string)")
# Addition
result = a * b + c
# Streamlit app
st.title("Multi + Addition App")
st.write(d)
st.write(f"The sum of {a}, {b} ,{c} is: {result}")