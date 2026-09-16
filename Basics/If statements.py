# If Statements
# These are blocks of code that will only run if a certain condition is met. 
# If statements are used to make decisions in your code.

# Example 1
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

# Example 2

age = 12
if age >= 18:
    print("You are an adult.")  # Output: You are an adult.

# Elif statements can be used to check multiple conditions.
# please note that the elif statement is only checked if the previous if statement was not true.

elif age < 0:
    print("Tung tung tung sahur is older than you.")  # Output: Tung tung tung sahur is older than you.

# Else statements can be used to provide an alternative block of code to run if the condition is not met.

else:
    print("You are too young for GTA6 lil bro.")    # Output: You are too young for GTA6 lil bro.


# Useful tips:

# Python, conditional blocks must follow a strict sequential order:          
                # 1. if: Evaluates the first condition.
                # 2. elif: Evaluates the next condition if the previous one was false.
                # 3. else: Executes if none of the above conditions are true.
# They must be used in this order to ensure that the logic flows correctly and that the appropriate block of code is executed based on the conditions provided.                
# Failure to do so may result in a syntax errors or unexpected behavior in your code.