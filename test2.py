import streamlit as st

st.write("""
# Largest Number App
This app computes the largest of threee numbers.

TDS - Graded Assignment 8
""")

for i in range(0,3,1):
   number = st.number_input('Enter the first number')
   number+str(i)= number 
   st.write('The first number is ', number+str(i))



if (number2 >= number2) and (number1 >= number3):
   largest = number1
elif (number2 >= number1) and (number2 >= number3):
   largest = number2
else:
   largest = number3


#displaying the largest number

st.write("The largest number is", largest)
