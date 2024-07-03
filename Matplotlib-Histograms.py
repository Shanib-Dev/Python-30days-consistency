"Histogram"
#A histogram is a graph showing frequency distributions.
#It is a graph showing the number of observations within each given interval.

"Create Histogram"
#In Matplotlib, we use the hist() function to create histograms.
#The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.
#Example
#A normal data distribution by Numpy
import numpy as np
x = np.random.normal(170, 10, 250)
print(x)

#The hist() function will read the array and produce a histogram:
#Example
#A simple histogram:
import matplotlib.pyplot as plt
x = np.random.normal(180, 30, 250)
plt.hist(x)
plt.show()