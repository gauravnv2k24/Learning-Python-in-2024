# string are enclose with doubt and single quotation (single lines or simple strings) or triple single quotation(multiple lines or long strings)

message = "hi hello there"

print(type(message)) # <class 'str'>

password='12345'
print(type(password)) # <class 'str'>

story = '''
string are enclose with doubt and single quotation (single lines or simple strings) or triple single quotation(multiple lines or long strings)
'''

print(type(story)) # <class 'str'>

# string concatination
first_name = "John"
last_name = "Doe"

print(first_name + " " + last_name) # John Doe