"Decision Tree"
#In this chapter we will show you how to make a "Decision Tree". A Decision Tree is a Flow Chart, and can help you make decisions based on previous experience.
#In the example, a person will try to decide if he/she should go to a comedy show or not.
#Luckily our example person has registered every time there was a comedy show in town, and registered some information about the comedian, and also registered if he/she went or not.
#Now, based on this data set, Python can create a decision tree that can be used to decide if any new shows are worth attending to.

"How Does it Work?"
#First, read the dataset with pandas:
#Example
import pandas as pd
df = pd.read_csv("data1.csv")
print(df)

#To make a decision tree, all data has to be numerical.
#We have to convert the non numerical columns 'Nationality' and 'Go' into numerical values.
#Pandas has a map() method that takes a dictionary with information on how to convert the values.
#{'UK': 0, 'USA': 1, 'N': 2}
#Means convert the values 'UK' to 0, 'USA' to 1, and 'N' to 2.
#Example
#Change string values into numerical values:
d = {'UK' : 0,'USA' : 1, 'N' : 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES' : 1, 'NO' : 0}
df['Go'] = df['Go'].map(d)
print("\n")
print(df)

#Then we have to separate the feature columns from the target column.
#The feature columns are the columns that we try to predict from, and the target column is the column with the values we try to predict.
#Example
#X is the feature columns, y is the target column:
features = ['Age', 'Experience','Rank', 'Nationality']
x = df[features]
y = df['Go']

print(x)
print(y)

#Now we can create the actual decision tree, fit it with our details. Start by importing the modules we need:
#Example
#Create and display a Decision Tree:
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv("data1.csv")
d = {'US' : 0, 'USA' : 1, 'N' : 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES' : 1, 'NO' :  0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']
x = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x,y)

tree.plot_tree(dtree, feature_names=features)

"Result Explained"
#The decision tree uses your earlier decisions to calculate the odds for you to wanting to go see a comedian or not.

"Predict Values"
#We can use the Decision Tree to predict new values.
#Example: Should I go see a show starring a 40 years old American comedian, with 10 years of experience, and a comedy ranking of 7?
#Example
#Use predict() method to predict new values:
print(dtree.predict([[40, 10, 7, 1]]))

#Example
#What would the answer be if the comedy rank was 6?
print(dtree.predict([[40, 10, 6, 1]]))

