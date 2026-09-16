# String Slicing is a method to extract a portion of a string by specifying the start and end index. 
# The syntax for string slicing is: string[start:end:step]

string = "Python is fun"

# (1) Indexing

# Indexing starts from 0, so the first character of the string is at index 0, the second character is at index 1, and so on.
first_word = string[0]# Output: P

# The end index is exclusive, meaning that the character at the end index is not included in the slice.
first_word = string[0:6]  # Output: Python

# This is ashortcut for slicing from the start of the string to the end of the string.
full_string = string[:]  # Output: Python is fun

# But if you prefer, you can also specify the start and end index to slice a portion of the string.
full_string = string[0:13]  # Output: Python is fun


# (2) Stepping

# Stepping allows you to skip characters in the string. The step value specifies how many characters to skip.
# For example, if you want to extract every second character from the string, you can use a step value of 2.

every_second_character = string[::2]  # Output: Pto sn


# (3) Bonus - Reverse
# You can also reverse a string using slicing by specifying a negative step value.

reversed_string = string[::-1]  # Output: nuf si nohtyP

#(4) Slicing 

# Take a different scenario where you have a web handle
# In this case i want to remove a substring from the web handle, specifically the "http://" part of the web handle.

web1= "http://google.com"
web2= "http://wikipedia.com"

# To remove the "http://" part of the web handle, you can use string slicing to extract the portion of the string starting from index 7 
                                                         # (the index of the first character after "http://") to the end of the string.
slice = slice(7,-4)  

print(web1[slice])  # Output: google
print(web2[slice])  # Output: wikipedia