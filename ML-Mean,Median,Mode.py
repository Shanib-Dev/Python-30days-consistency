"Mean, Median, and Mode"
#What can we learn from looking at a group of numbers?
#In Machine Learning (and in mathematics) there are often three values that interests us:
"""
Mean - The average value
Median - The mid point value
Mode - The most common value
"""
#Example: We have registered the speed of 13 cars:
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
#What is the average, the middle, or the most common speed value?

"Mean"
#The mean value is the average value.
#To calculate the mean, find the sum of all values, and divide the sum by the number of values:
#(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77

#The NumPy module has a method for this. Learn about the NumPy module in our NumPy Tutorial.
#Example
#Use the NumPy mean() method to find the average speed:
import numpy as np
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
print(x)

"Median"
#The median value is the value in the middle, after you have sorted all the values:
#77, 78, 85, 86, 86, 86, (median)-87, 87, 88, 94, 99, 103, 111
#It is important that the numbers are sorted before you can find the median.

#The NumPy module has a method for this:
#Example
#Use the NumPy median() method to find the middle value:
y = np.median(speed)
print(y)

"Mode"
#The Mode value is the value that appears the most number of times:
#99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

#The SciPy module has a method for this. Learn about the SciPy module in our SciPy Tutorial.
#Example
#Use the SciPy mode() method to find the number that appears the most:
from scipy import stats
z = stats.mode(speed)
print(z)

"Chapter Summary"
#The Mean, Median, and Mode are techniques that are often used in Machine Learning, so it is important to understand the concept behind them.