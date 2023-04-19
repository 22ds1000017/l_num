import streamlit as st

st.write("""
# Largest Number App
This app computes the largest of threee numbers.

TDS - Graded Assignment 8
""")


for i in range(1,4,1):
   number1 = st.number_input('Enter the first number')
   number2 = st.number_input('Enter the second number')
   number3 = st.number_input('Enter the third number')
for i in range(1,3,1):
   st.write('The first number is ', number+str(i))



if (number_list[1] >= number_list[2]) and (number_list[1] >= number_list[3]):
   largest = number_list[1]
elif (number_list[2] >= number_list[1]) and (number_list[2] >= number_list[3]):
   largest = number_list[2]
else:
   largest = number_list[3]



#displaying the largest number

st.write("The largest number is", largest)
