import streamlit as st

st.write("""
# Largest Number App
This app computes the largest of threee numbers.

TDS - Graded Assignment 8
""")

number= []
for i in range(3):
   number[0] = st.number_input('Enter the first number')
   number[1] = st.number_input('Enter the second number')
   number[2] = st.number_input('Enter the third number')
for i in range(3):
   st.write('The first number is ', number[i])



if (number_list[1] >= number_list[2]) and (number_list[1] >= number_list[3]):
   largest = number_list[1]
elif (number_list[2] >= number_list[1]) and (number_list[2] >= number_list[3]):
   largest = number_list[2]
else:
   largest = number_list[3]



#displaying the largest number

st.write("The largest number is", largest)
