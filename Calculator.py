import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def calculate(a, b, operation):
    if operation == "Addition":
        return add(a, b)
    elif operation == "Subtraction":
        return subtract(a, b)
    elif operation == "Multiplication":
        return multiply(a, b)
    elif operation == "Division":
        return divide(a, b)

st.set_page_config(page_title="Smart Arithmetic Tool", page_icon="📐")

st.title("📐 Smart Arithmetic Tool")
st.write("Advanced calculator built using Python & Streamlit")

num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

result = calculate(num1, num2, operation)

st.subheader("Result")

if operation == "Division" and num2 == 0:
    st.error("Error: Division by zero is not allowed.")
else:
    st.success(f"The result is: {result}")
