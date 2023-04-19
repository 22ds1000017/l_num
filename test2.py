import streamlit as st

st.write("""
# Largest Number App
This app computes the largest of threee numbers.

TDS - Graded Assignment 8
""")

number_list = []
for i in range(0,3,1):
   number_in = st.number_input('Enter the first number')
   number_list.append(number_in)
   st.write('The first number is ', number_list(i))



if (number_list[1] >= number_list[2]) and (number_list[1] >= number_list[3]):
   largest = number_list[1]
elif (number_list[2] >= number_list[1]) and (number_list[2] >= number_list[3]):
   largest = number_list[2]
else:
   largest = number_list[3]



#displaying the largest number

st.write("The largest number is", largest)
