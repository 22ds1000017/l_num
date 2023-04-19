import streamlit as st

st.write("""
# Largest Number App
This app computes the largest of threee numbers.

TDS - Graded Assignment 8
""")

number1 = st.number_input('Enter the first number')
st.write('The first number is ', number1)

number2 = st.slider('Enter the second number', 0, 2000, 1)
st.write("second number", number2)

number3 = st.slider('Enter the third  number', 0,10000, 1)
st.write("third number ", number3)

if (number2 >= number2) and (number1 >= number3):
   largest = number1
elif (number2 >= number1) and (number2 >= number3):
   largest = number2
else:
   largest = number3


#displaying the largest number

st.write("The largest number is", largest)
