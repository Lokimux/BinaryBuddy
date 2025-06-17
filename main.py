import streamlit as st

# Conversion functions
def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(int(decimal))[2:]

def binary_to_hexadecimal(binary):
    return hex(int(binary, 2))[2:]

def hexadecimal_to_binary(hexadecimal):
    return bin(int(hexadecimal, 16))[2:]

def decimal_to_hexadecimal(decimal):
    return hex(int(decimal))[2:]

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def binary_to_octal(binary):
    return oct(int(binary, 2))[2:]

def octal_to_binary(octal):
    return bin(int(octal, 8))[2:]

def decimal_to_octal(decimal):
    return oct(int(decimal))[2:]

def octal_to_decimal(octal):
    return int(octal, 8)

def hexadecimal_to_octal(hexadecimal):
    return oct(int(hexadecimal, 16))[2:]

def octal_to_hexadecimal(octal):
    return hex(int(octal, 8))[2:]

# App title with styling
st.title("🔢 Number Conversion Application")
st.subheader("Convert between Binary, Decimal, Hexadecimal, and Octal systems!")

# Create two columns to organize input and output
col1, col2 = st.columns(2)

# Dropdown to choose conversion type
conversion_type = col1.selectbox("Choose conversion type", [
    "Binary to Decimal", "Decimal to Binary", "Binary to Hexadecimal", 
    "Hexadecimal to Binary", "Decimal to Hexadecimal", "Hexadecimal to Decimal", 
    "Binary to Octal", "Octal to Binary", "Decimal to Octal", "Octal to Decimal", 
    "Hexadecimal to Octal", "Octal to Hexadecimal"
])

# Input box with placeholders based on the selected conversion type
placeholders = {
    "Binary": "Enter a binary number (e.g., 1010)",
    "Decimal": "Enter a decimal number (e.g., 123)",
    "Hexadecimal": "Enter a hexadecimal number (e.g., 1A3)",
    "Octal": "Enter an octal number (e.g., 175)"
}

if "Binary" in conversion_type:
    input_placeholder = placeholders["Binary"]
elif "Decimal" in conversion_type:
    input_placeholder = placeholders["Decimal"]
elif "Hexadecimal" in conversion_type:
    input_placeholder = placeholders["Hexadecimal"]
else:
    input_placeholder = placeholders["Octal"]

# Input field with placeholder guidance
input_value = col1.text_input(f"Enter the number to convert", placeholder=input_placeholder)

# Button for conversion
if col1.button("Convert"):
    # Input validation for empty input
    if not input_value:
        col2.error("Please enter a valid number.")
    else:
        try:
            if conversion_type == "Binary to Decimal":
                result = binary_to_decimal(input_value)
            elif conversion_type == "Decimal to Binary":
                result = decimal_to_binary(input_value)
            elif conversion_type == "Binary to Hexadecimal":
                result = binary_to_hexadecimal(input_value)
            elif conversion_type == "Hexadecimal to Binary":
                result = hexadecimal_to_binary(input_value)
            elif conversion_type == "Decimal to Hexadecimal":
                result = decimal_to_hexadecimal(input_value)
            elif conversion_type == "Hexadecimal to Decimal":
                result = hexadecimal_to_decimal(input_value)
            elif conversion_type == "Binary to Octal":
                result = binary_to_octal(input_value)
            elif conversion_type == "Octal to Binary":
                result = octal_to_binary(input_value)
            elif conversion_type == "Decimal to Octal":
                result = decimal_to_octal(input_value)
            elif conversion_type == "Octal to Decimal":
                result = octal_to_decimal(input_value)
            elif conversion_type == "Hexadecimal to Octal":
                result = hexadecimal_to_octal(input_value)
            elif conversion_type == "Octal to Hexadecimal":
                result = octal_to_hexadecimal(input_value)

            # Display the result in a highlighted format
            col2.success(f"**Conversion Result**: {result}")

        except ValueError:
            col2.error("Invalid input! Please enter a correct number in the selected format.")

# Customize the sidebar with more info
st.sidebar.title("ℹ️ About the App")
st.sidebar.info("This app helps you convert numbers between different bases such as Binary, Decimal, Hexadecimal, and Octal.")
