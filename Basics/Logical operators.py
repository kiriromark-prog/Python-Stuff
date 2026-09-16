# Logical operators(and, or, not) are used to check multiple conditions in a single if statement. 
# They allow you to combine multiple boolean expressions and evaluate them together.

temp = int(input("What is the temperature outside? "))

# Example 1: Using the 'and' operator

if not (temp >= 0 and temp <= 30):
    print("The temperature is comfortable.")  # Output: The temperature is comfortable.
    print("You can go outside and enjoy the weather.")

# Example 2: Using the 'or' operator

elif not (temp >= 0 and temp <= 30):
    print("The temperature is not comfortable.")  # Output: The temperature is not comfortable.
    print("You should stay inside and keep warm or cool.")


# Core lessons:
# 1. The 'and' operator returns True if both conditions are True, and False otherwise.
# 2. The 'or' operator returns True if at least one of the conditions is True, and False if both conditions are False.
# 3. The 'not' operator negates the boolean value of a condition, returning True if the condition is False, and False if the condition is True.