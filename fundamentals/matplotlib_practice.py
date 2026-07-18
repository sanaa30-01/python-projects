from typing import overload
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0, 10, 100)
print(x[:10])


#plotting a line graph 

plt.figure()
plt.plot(x, x**2)
plt.show()

#or can be written as:

fig, ax = plt.subplots()
ax.plot(x, x**2)
plt.show()


#plotting a scatter graph

fig, ax = plt.subplots()
ax.scatter(x, np.exp(x))
plt.show()

fig, ax = plt.subplots()
ax.scatter(x, np.sin(x))
plt.show()


#plotting a bar graph

nut_butter_prices = {"almond butter": 10,
                      "peanut butter": 8,
                      "cashew butter": 12}

fig, ax = plt.subplots()
ax.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax.set(title="Nut Butter Prices", ylabel="Prices ($)")

plt.show()

#or can plot a horizontal bar graph too

fig, ax = plt.subplots()
ax.barh(list(nut_butter_prices.keys()), list(nut_butter_prices.values()))
plt.show() 


#plotting a histogram

x = np.random.randn(1000)   #randn pulls data from a normal distribution and we want that because a histogram is a plot best for distributions

fig, ax = plt.subplots()
ax.hist(x)
plt.show()


x = np.random.random(1000)
fig, ax = plt.subplots()
ax.hist(x)
plt.show()


#plotting multiple subplots

#option 1: creating 4 subplots with each Axis having its own variable 

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))

ax1.plot(x, x/2)
ax2.scatter(np.random.random(10), np.random.random(10))
ax3.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax4.hist(np.random.randn(1000))
plt.show() 

#option 2: creating 4 subplots with the same Axis variable (don't have to create 4 separate variables)

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))

ax[0, 0].plot(x, x/2)
ax[0, 1].scatter(np.random.random(10), np.random.random(10))
ax[1, 0].bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax[1, 1].hist(np.random.randn(1000))
plt.show()


#matplotlib can use pandas to plot directly

student_data = pd.read_csv("/Users/sanaataneja/Downloads/student.csv")
print(student_data)

ts = pd.Series(np.random.randn(1000),
                index=pd.date_range("1/1/2025", periods=1000))

print(ts)

#cumsum() is a method that returns the cumulative sum of a Series
ts.cumsum().plot(kind="line")
plt.show() 

#bar plot from a pandas dataframe

x = np.random.rand(10, 4)   #will create a 10x4 2d array of random numbers 
df = pd.DataFrame(x, columns=["a", "b", "c", "d"])
df.plot.bar()
plt.show() 


student_data.plot(x="name", y="mark", kind="bar")
plt.show()  

#histogram from a pandas dataframe

student_data["mark"].plot.hist(bins=10)
plt.show()


#creating a plot with multiple Axes using a pandas dataframe


heart_disease = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/heart-disease.csv")
print(heart_disease.head())

heart_disease.plot.hist(figsize=(5, 20), subplots=True)
plt.show() 


#creating a more complex plot 
over_50 = heart_disease[heart_disease["age"] > 50]   #this will return a dataframe of all the rows where the age is greater than 50 --> with all other corresponding columns 

over_50.plot(kind="scatter", x="age", y="chol", c="target", figsize=(10, 6))   #will color plot according to the target value (1 for heart disease, 0 for no heart disease)
plt.show()

#or can be plotted using a single axis object
fig, ax = plt.subplots(figsize=(10, 6))

over_50.plot(kind="scatter", x="age", y="chol", c="target", ax=ax)

ax.set_xlim([45, 100])
plt.show()


#or plot using only Axes instances instead of using the dataframe
fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(over_50["age"], over_50["chol"], c=over_50["target"])
ax.set(title="Heart Diseases and Cholesterol Levels", xlabel="Age", ylabel="Cholesterol")
ax.legend(*scatter.legend_elements(), title="Target")

ax.axhline(over_50["chol"].mean(), linestyle="--", color="red")

plt.show()


#plotting multiple plots on the same figure from a dataframe

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(10, 8))

#adding data for ax0 --> heart disease and cholesterol levels

scatter = ax1.scatter(over_50["age"], over_50["chol"], c=over_50["target"])
ax1.set(title="Heart Disease and Cholesterol Levels", ylabel="Cholesterol")
ax1.legend(*scatter.legend_elements(), title="Target")

ax1.axhline(over_50["chol"].mean(), linestyle="--", color="red", label="Average")

#adding data for ax2 --> heart disease and max heart rate levels

scatter = ax2.scatter(over_50["age"], over_50["thalach"], c=over_50["target"])
ax2.set(title="Heart Disease and Max Heart Rate Levels", xlabel="Age", ylabel="Max Heart Rate")
ax2.legend(*scatter.legend_elements(), title="Target")

ax2.axhline(over_50["thalach"].mean(), linestyle="--", color="red", label="Average")

#title for the entire figure (both plots)
fig.suptitle("Heart Disease Analysis", fontsize=16, fontweight="bold")

plt.show() 
