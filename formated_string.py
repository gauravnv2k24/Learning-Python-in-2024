# formatted strings 
# instead of converting and merging the types into string 
# you can use formatted strings
 
name = "John"
age  = 20

# makes any type used directly without int type conversion
print(f"Hello, {name} you are {age} years old") # Hello, John you are 20 years old
# or
print("Hello, {} you are {} years old".format(name,age)) # Hello, John you are 20 years old
# or
print("Hello, {1} you are {0} years old".format(age,name)) # Hello, John you are 20 years old
# or you can also create new variables
print("Hello, {new_name} you are {age} years old".format(new_name="ram",age=50)) # Hello, ram you are 50 years old