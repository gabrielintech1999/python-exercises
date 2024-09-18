# Write a program that reads something from the keyboard and displays its primitive type and all possible information about it.

user_input = input("Enter something: ")

print(f"The primitive type of the input is: {type(user_input)}")


try:
    number_input = float(user_input)
    print(f"the input is a number.")
    print(f"the primitive type after conversion is: {type(number_input)}")
except ValueError:
    print(f"the input is not a number")

print(f"Is the input alphanumeric?  {user_input.isalnum()} ")
print(f"Does the input contain only letters? {user_input.isalpha()} ")
print(f"Does the input contain only digits?  {user_input.isdigit()} ")
print(f"Is the input in uppercase?  {user_input.isupper()} ")
print(f"Is the input in lowercase?  {user_input.islower()} ")
print(f"Is the input a whitespace string ?{user_input.isspace()} ")





