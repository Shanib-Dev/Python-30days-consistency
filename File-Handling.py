"Python File Open"
#File handling is an important part of any web application.
#Python has several functions for creating, reading, updating, and deleting files.

"File Handling"
#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
#There are four different methods (modes) for opening a file:
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists
#In addition you can specify if the file should be handled as binary or text mode
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

"Syntax"
#To open a file for reading it is enough to specify the name of the file:
f = open("hey.txt")

#The code above is the same as:
f = open("hey.txt", "rt")

#Because "r" for read, and "t" for text are the default values, you do not need to specify them.

#Open a File on the Server
#Assume we have the following file, located in the same folder as Python:
#"hey.txt"
#To open the file, use the built-in open() function.
#The open() function returns a file object, which has a read() method for reading the content of the file:
#Example
f = open("hey.txt", "rt")
print(f.read())

#If the file is located in a different location, you will have to specify the file path, like this:
#Example
#Open a file on a different location:
try:
 f = open("D:Users\\sanib shaikh\\hey.txt", "r")
 print(f.read())
except:
    print("File Not Found")

"Read Only Parts of the File"
#By default the read() method returns the whole text, but you can also specify how many characters you want to return:
#Example
#Return the 5 first characters of the file:
f = open("hey.txt", "r")
print(f.read(5))

"Read Lines"
#You can return one line by using the readline() method:
#Example
#Read one line of the file:
f = open("hey.txt", "r")
print(f.readline())

#By calling readline() two times, you can read the two first lines:
#Example
#Read two lines of the file:
f = open("hey.txt", "r")
print(f.readline())
print(f.readline())

#By looping through the lines of the file, you can read the whole file, line by line:
#Example
#Loop through the file line by line:
f = open("hey.txt", "r")
for x in f:
  print(x)

"Close Files"
#It is a good practice to always close the file when you are done with it.
#Example
#Close the file when you are finish with it:
f = open("hey.txt", "r")
print(f.readline())
f.close()

"Python file Write"
#Write to an Existing File
#To write to an existing file, you must add a parameter to the open() function:
#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content
#Example
#Open the file "hey.txt" and append content to the file:
f = open("hey.txt", "a")
f.write("\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open("hey.txt", "r")
print(f.read())

#Example
#Open the file "hey1.txt" and overwrite the content:
w = open("hey1.txt", "w", )
w.write("Woops! I have deleted the content!")
w.close()

#open and read the file after the overwriting:
w = open("hey1.txt", "r")
print(w.read())


"Create a New File"
#To create a new file in Python, use the open() method, with one of the following parameters:
#"x" - Create - will create a file, returns an error if the file exist
#"a" - Append - will create a file if the specified file does not exist
#"w" - Write - will create a file if the specified file does not exist
#Example
#Create a file called "myfile.txt":
#f = open("myfile.txt", "x")
#Result: a new empty file is created!
#Example
#Create a new file if it does not exist:
f = open("myfile.txt", "w")


"Python Delete File"
"Delete a File"
#To delete a file, you must import the OS module, and run its os.remove() function:
#Example
#Remove the file "demofile.txt":
import os
os.remove("delete.txt")

"Check if File exist:"
#To avoid getting an error, you might want to check if the file exists before you try to delete it:
#Example
#Check if file exists, then delete it:
import os
if os.path.exists("delete.txt"):
  os.remove("delete.txt")
else:
  print("The file does not exist")

"Delete Folder"
#To delete an entire folder, use the os.rmdir() method:
#Example
#Remove the folder "myfolder":
"""
import os
os.rmdir("myfolder")
"""