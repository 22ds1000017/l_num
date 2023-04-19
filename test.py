

import streamlit as st

number1 = st.number_input('Insert a number')
st.write('The current number is ', number1)

number2 = st.number_input('Insert a number')
st.write('The current number is ', number2)


number3 = st.number_input('Insert a number')
st.write('The current number is ', number3)


if (number1 >= number2) and (number1 >= number3):
   largest = number1
elif (number2 >= number1) and (number2 >= number3):
   largest = number2
else:
   largest = number3


#displaying the largest number

st.write("The largest number is", largest)

