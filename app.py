import streamlit as st

def convert_units(value: float, unit_from: str, unit_to: str):
    # print("value-->", value)
    # print("unit_from-->", unit_from)
    # print("unit_to-->", unit_to)

    # 1 Kilometer = 1000 Meters
    # 1 Meter = 0.001 Kilometer
    # 1 Kilogram = 1000 Grams
    # 1 Gram = 0.001 Kilogram

    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
        return value * 0.001
    else:
        return "Conversion is not supported"
    
# result = convert_units(5, "kilometers", "meters")
# print("The value in meter is", result)

def main():
    st.title("Unit Converter")
    st.write("Welcome to the **Unit Converter!**")
    value = st.number_input("Enter the value you want to convert: ", min_value=0.0)
    unit_from = st.selectbox("Enter the value you want to convert from:", ["meters", "kilometers", "grams", "kilograms"])
    unit_to = st.selectbox("Enter the value you want from conversion:", ["meters", "kilometers", "grams", "kilograms"])

    if st.button("Enter"):
       result = convert_units(value, unit_from, unit_to)
       st.write("Converted Value: ", result)


    # print("Welcome to the Unit Converter")
    # value = float (input("Enter the value you want to convert: "))
    # unit_from = input("Enter the value you want to convert from (e.g. meters, kilometers, grams, kilograms): ")
    # unit_to = input("Enter the value you want from conversion (e.g. meters, kilometers, grams, kilograms): ")

    # print("Value: ", value)
    # print("Unit from: ", unit_from)
    # print("Unit to: ", unit_to)
    # result = convert_units(value, unit_from, unit_to)
    # print("Converted Value: ", result)

main()