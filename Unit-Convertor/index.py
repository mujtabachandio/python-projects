import streamlit as st


st.set_page_config(page_title="Unit Converter", page_icon="🌍", layout="centered")
# Conversion functions
def length_conversion(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_conversion(value, from_unit, to_unit):
    conversion_factors = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

# Streamlit UI
st.title("Unit Converter 🌍")

# Select category
category = st.selectbox("Choose a category", ["Length", "Weight", "Temperature"])

if category == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    if st.button("Convert"):
        result = length_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    value = st.number_input("Enter value", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    if st.button("Convert"):
        result = weight_conversion(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    value = st.number_input("Enter value", format="%.2f")
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    if st.button("Convert"):
        result = temperature_conversion(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")
