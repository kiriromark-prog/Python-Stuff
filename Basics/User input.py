# In python user input is taken using the input() function. 
# The input() function allows the user to provide input to the program during its execution.

number = input("Enter a number : ") # The input() function takes a string argument that is displayed as a prompt to the user.

# The number variable will store the value entered by the user as a string.

print("You entered:", number) # The input() function returns the user input as a string

# Ok since you know the basics of user input here is an example to apply your basics knowledge of user input.

#Example ///
name = input("Enter your name: ")


# Please note to convert the input to an integer, you can use the int() function.
# Failure to convert the input to an integer will result in a ValueError if the user enters a non-integer value.

age = int(input("Enter your age: "))

# This will print the name and age entered by the user in a formatted string.

# Convert input to float for height
height = float(input("Enter your height in meters: "))  


print("Hello", name, "you are", age, "years old.") 
print("Your height is:", height, "meters.")