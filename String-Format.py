"String Format"
#As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
#Example
age = 36
txt = "My name is John, I am " + age
print(txt)

#But we can combine strings and numbers by using f-strings or the format() method!

"F-Strings"
#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
#To specify a string as an f-string, simply put an f in front of the string literal,
#and add curly brackets {} as placeholders for variables and other operations.
#Example
#Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
#A placeholder can contain variables, operations, functions, and modifiers to format the value.
#Example
#Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)
