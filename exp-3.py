# Define the input string
input_string = "Welcome to Python world"

# 1. Count the number of alphabets in the given string          (can also do like this ----> alphabet_count = sum(char.isalpha() for char in input_string))
alphabet_count = 0
for char in input_string:
    if char.isalpha():
        alphabet_count = alphabet_count + 1


# 2. Extract characters in the given range from the given string (indices 7 to 13)
start = int(input("Give starting index : "))
end = int(input("Give ending index : "))
extracted_characters = input_string[start:end]

# 3. Check if the string is alphanumeric or not
is_alphanumeric = input_string.isalnum()

# Print the results
print("Number of alphabets:", alphabet_count)
print("Extracted characters:", extracted_characters)
if is_alphanumeric:
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")
