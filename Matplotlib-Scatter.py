"Creating Scatter Plots"
#With Pyplot, you can use the scatter() function to draw a scatter plot.
#The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()

#The observation in the example above is the result of 13 cars passing by.
#The X-axis shows how old the car is.
#The Y-axis shows the speed of the car when it passes.
#Are there any relationships between the observations?
#It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.

"Compare Plots"
#In the example above, there seems to be a relationship between speed and age, but what if we plot the observations from another day as well? Will the scatter plot tell us something else?
#Example
#Draw two plots on the same figure:
#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)
plt.show()

#By comparing the two plots, I think it is safe to say that they both gives us the same conclusion: the newer the car, the faster it drives.

"Colors"
#You can set your own color for each scatter plot with the color or the c argument:
#Example
#Set your own color of the markers:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color="#0000FF")

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = "hotpink")
plt.show()

"Color Each Dot"
#You can even set a specific color for each dot by using an array of colors as value for the c argument:
#Note: You cannot use the color argument for this, only the c argument.
#Example
#Set your own color of the markers:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
color = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x,y, c=  color)
plt.show()

"ColorMap"
#The Matplotlib module has a number of available colormaps.
#A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.
#This colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, up to 100, which is a yellow color.

"How to Use the ColorMap"
#You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.
#In addition you have to create an array with values (from 0 to 100), one value for each point in the scatter plot:
#Example
#Create a color array, and specify a colormap in the scatter plot:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
color = np.array([0,10,20,25,30,40,45,50,60,70,80,90,100])

plt.scatter(x,y, c= color, cmap="viridis")
plt.show()

#You can include the colormap in the drawing by including the plt.colorbar() statement:
#Example
#Include the actual colormap:

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.show()

"Size"
#You can change the size of the dots with the s argument.
#Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:
#Example
#Set your own size for the markers:

size = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x, y, s=size)
#plt.show()

"Alpha"
#You can adjust the transparency of the dots with the alpha argument.
#Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:
#Example
#Set your own size for the markers:

plt.scatter(x, y, s=size, alpha=0.5)
#plt.show()

#Combine Color Size and Alpha
#You can combine a colormap with different sizes of the dots. This is best visualized if the dots are transparent:
#Example
#Create random arrays with 100 values for x-points, y-points, colors and sizes:

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = np.random.randint(100, size=(100))

plt.scatter(x, y, s=sizes, c=colors, alpha=0.5 , cmap='nipy_spectral')
plt.show()
