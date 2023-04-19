
    import streamlit as st

    number1 = st.number_input('Enter the first number')
    st.write('The first number is ', number1)

    number2 = st.slider('Enter the second number', 0, 2000, 1)
    st.write("second number", number2)

    @st.cache(allow_output_mutation=True)
    def Nums():
        return []

    nums = Nums()
    num = st.sidebar.number_input("Input Number")
    if st.sidebar.button("Add number"):
        nums.append(num)

    try:
        inputs = nums
        st.table(inputs)
        st.write("Sum: ", sum(inputs))
    except:
        st.title("Enter some numbers")
