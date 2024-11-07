# Task 1 Input Length Validator: Write a script that asks for and checks the length of the user's firs name
#and last name. Both should be at least 2 charcters long. if not, print an error message.

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

if len(first_name) >= 2 and len(last_name) >= 2:
    print(f"Thank you {first_name} {last_name} for entering your name.")
else:
    print("Error, both first and last name must be at least 2 characters long, please re-enter your name.")    