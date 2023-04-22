# Take input from the user
text = input("Enter text: ")

# Initialize an empty string to store the transformed text
transformed_text = ""

# Loop through each character in the input text
for i in range(len(text)):
    # Get the next character in the string (wrapping around to the beginning if at the end)
    next_char = text[(i+1) % len(text)]
    # Append the next character to the transformed text
    transformed_text += next_char

# Print the transformed text
print(transformed_text)
