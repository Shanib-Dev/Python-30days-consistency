"Add Grid Lines to a Plot"
#With Pyplot, you can use the grid() function to add grid lines to the plot.
#Example
#Add grid lines to the plot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)
plt.title("Sports league")
plt.xlabel("Average pulse")
plt.ylabel("Calorie Burnage")
plt.grid()
plt.show()

"Specify Which Grid Lines to Display"
#you can use the axis parameter in the grid() function to specify which grid lines to display.
#Legal values are: 'x', 'y', and 'both'. Default value is 'both'.
#Example
#Display only grid lines for the x-axis:

plt.plot(x,y)
plt.grid(axis="x")
plt.show()

"Set Line Properties for the Grid"
#You can also set the line properties of the grid, like this: grid(color = 'color', linestyle = 'linestyle', linewidth = number).
#Example
#Set the line properties of the grid:

plt.plot(x,y)
plt.grid(color = 'green', ls = '--', linewidth = 2.5)
plt.show()