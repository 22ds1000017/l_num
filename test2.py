import streamlit as st

st.write("""
# Largest Number App
This app computes the largest of threee numbers.

TDS - Graded Assignment 8
""")


number1 = st.number_input('Enter the first number')
st.write("1st number", number1)
number2 = st.number_input('Enter the second number')
st.write("2nd number", number2)
number3 = st.number_input('Enter the third number')
st.write("3rd number", number3)

if (number1 >= number2) and (number1 >= number3):
   largest = number1
elif (number2 >= number1) and (number2 >= number3):
   largest = number2
else:
   largest = number3



#displaying the largest number

st.write("The largest number is", largest)
