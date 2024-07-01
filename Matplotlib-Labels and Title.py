"Create Labels for a Plot"
#With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
#Example
#Add labels to the x- and y-axis
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie burnae")
plt.show()

"Create a Title for a Plot"
#With Pyplot, you can use the title() function to set a title for the plot.
#Example
#Add a plot title and labels for the x- and y-axis:

plt.plot(x,y)
plt.xlabel("Average pulse")
plt.ylabel("Calorie burnage")
plt.title("Sports Watch Data")
plt.show()

"Set Font Properties for Title and Labels"
#You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.
#Example
#Set font properties for the title and labels:

Font1 = {'color':'blue','size':20}
Font2 = {'family':'serif', 'color':'darkred', 'size':15}

plt.plot(x,y)
plt.xlabel("Average Pulse", fontdict=Font1)
plt.ylabel("Calorie Pulse", fontdict=Font2)
plt.title("Sports Watch Data", fontdict=Font1)
plt.show()

"Position the Title"
#You can use the loc parameter in title() to position the title.
#Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
#Example
#Position the title to the left

plt.plot(x,y)
plt.title("Sports Watch Data", loc="right")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Pulse")
plt.show()