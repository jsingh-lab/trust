# Simple Python script to print a color based on user input

# Ask for ID
user_id = input("Enter ID (0 or 1): ")

# Check the value and print the corresponding color
if user_id == '1':
    print("Green")
elif user_id == '0':
    print("Red")
else:
    print("Yellow")
