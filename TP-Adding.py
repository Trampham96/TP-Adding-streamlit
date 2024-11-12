import streamlit as st

# Set the title of the app
st.title("🎉 Fun Adding App for Toddlers 🎉")
st.subheader("Let's add two numbers together!")

# Create input fields for user to enter numbers
first_number = st.number_input("Enter the first number:", min_value=0, value=0, step=1)
second_number = st.number_input("Enter the second number:", min_value=0, value=0, step=1)

# Calculate the sum when the user interacts with the input fields
if st.button("Calculate Sum"):
    result = first_number + second_number
    st.success(f"The sum is: {result}", icon="🎈")
    st.balloons()
