import streamlit as st
a = 10
b = 20
c=10
result = a * b * c
# Streamlit app
st.title("Multiplication App")
st.text("Welcome")
st.write(f"The sum of {a} ,{b} {c} is: {result}")