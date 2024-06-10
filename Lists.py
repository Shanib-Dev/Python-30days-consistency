"List"
#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:
#Example
#Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)

"List Length"
#To determine how many items a list has, use the len() function:
#Example
#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#List Items - Data Types
#List items can be of any data type:
#Example
#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list can contain different data types:
#Example
#A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

"type()"
#From Python's perspective, lists are defined as objects with the data type 'list':
#<class 'list'>
#Example
#What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

"The list() Constructor"
#It is also possible to use the list() constructor when creating a new list.
#Example
#Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

"Python Collections (Arrays)"
#There are four collection data types in the Python programming language:
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""
