# the actual string
greet_message = "Hello gaurav"

# string slicing [start:stop:step]
print(greet_message[0::2]) # Hlogua

# to get length use len() function
print(len(greet_message)) # 12

# below is some of built in methods of python
# they are accessed with varname.method()


# to get count of a specific character
print(greet_message.count('l')) # 2

# check lowercase use -> islower()
print(greet_message.islower()) # True
# check uppercase use -> isupper()
print(greet_message.isupper()) # False

# to remove space b4 and after use .strip()
new_message = " hello "
print(new_message.strip()) # hello

# there are many methods in python strings only few of them are listed above
