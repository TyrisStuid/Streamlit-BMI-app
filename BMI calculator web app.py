import streamlit as st

def calculate_BMI(height,weight):
    height = height/100
    bmi = weight/(height**2)

    return round(bmi,3)

def app():
    # Set the app title
    st.title("BMI Calculator")

    # Get user inputs for weight and height
    weight = st.number_input("Enter your weight in kg", min_value=0.1, step=0.1)
    height = st.number_input("Enter your height in cm", min_value=0.1, step=0.1)

    # Calculate the BMI
    bmi = calculate_BMI(weight, height)

    # Display the result
    st.write("Your BMI is:", bmi)

# Run the Streamlit app
if __name__ == "__main__":
    app()
