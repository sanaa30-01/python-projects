import pandas as pd

#1-d column of data is known as a series

cars = pd.Series(["BMW", "Toyota", "Honda"])
print(cars)

colors = pd.Series(["Blue", "Red", "White"])
print(colors)

#2-d table of data with rows and columns is known as a dataframe --> can be called by passing in a python dictionary 

#key of the dictionary is the column name and the value is the data in that column
#in this case we used the two series we initialized above to create hte data for the dataframe
car_data = pd.DataFrame({"Car Name": cars, 
                        "Color": colors,})
print(car_data)


#second dataframe example
foods = pd.Series(["Ice cream", "Salad", "French fries", "Chicken", "Pizza"])

prices = pd.Series([3, 5, 2, 9, 10])

food_data = pd.DataFrame({"Food Name": foods,
                          "Price": prices})

print(food_data)

#reading a csv file

#paste in the absolute path of the csv file 
student_data = pd.read_csv("/Users/sanaataneja/Downloads/student.csv")

print(student_data)

#exporting a dataframe to a csv file

#use the absolute path of the location you want to export the file to
student_data.to_csv("/Users/sanaataneja/Downloads/student_data.csv")

#printing the data types of each of the columns in the dataframe
print(student_data.dtypes)


#describe function gives a statistical summary of the numerical columns in the dataframe including count, mean, std, min, quartiles, and max
print(student_data.describe())

#info function gives a summary of the dataframe 
#including the number of entries, the number of non-null entries in each column (if non null entries are less than total entires, there are missing values), and data types of each column
print(student_data.info())

#statistical functions

print(student_data.mean(numeric_only=True))  #will output the mean of the nuemrical columns only, specifcying this is important

print(student_data.sum(numeric_only=True))  #specificying numeric only is important since default is false and it will output the sum of the textual columns too

#using columns 
print(student_data.columns)
#making a list to store the names of the columns
student_data_columns = student_data.columns
print(student_data_columns[0])

#using index
#will output the index (values of the left most column) of the dataframe
print(student_data.index)


#viewing and selecting data

#viewing the first few rows of the datafram
print(student_data.head())

print(student_data.head(8)) 

#viewing the last few rows of the dataframe
print(student_data.tail())

print(student_data.tail(7)) 


#selcting data from a dataframe

#will output the row at index 4
print(student_data.loc[4]) 

#slicing using loc method 
#will output rows from index 0 to 6 (inclusive) 
print(student_data.loc[:6])  

#will output the values in the "class" column for all rows
print(student_data.loc[:, "class"]) 

#will output the values in the "mark" column for all rows 
print(student_data["mark"]) 

#using boelan indexing to output the rows where the value in the "mark" column is greater than 80 
print(student_data[student_data["mark"] > 80]) 

#comparing two columns in the dataframe
#will output the column specified first as the rows and the column specified second as the columns  
#pd.crosstab not student_data.crosstab because pd.crosstab is a function in pandas and student_data.crosstab is a method in the dataframe class
print(pd.crosstab(student_data["name"], student_data["class"])) 

#grouping data 
#will group the data by the column specified, all unique values in the column will be the groups, then it will output the mean of the numerical columns for each group
#will be useful for analyzing data by different categories
print(student_data.groupby("class").mean(numeric_only=True)) 


#manipulating data
#.str gives access to string methods for hte column specified 

#will not change the original dataframe, it will only return a new series with the lowercase values 
print(student_data["name"].str.lower())

#to change the original dataframe, we need to set the column to the new series

student_data["name"] = student_data["name"].str.lower()
print(student_data.head())

#.fillna() method can be used to fill missing values in the dataframe
#example: 
#will fill the missing values in the "Odometer" column with the mean of the "Odometer" column
#car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean(), inplace=False)

#.dropna() method can be used to drop missing values from the dataframe
#like .fillna(), .dropna() also has the inplace parameter set to false by default, so the original dataframe will not be changed 


#creating a new column in the dataframe
#three ways to do this:
#1. using pd.Series()
#2. using a python list
#3. using existing columns to create a new column

#1. using pd.Series()
#example: 
#student_data["grade"] = pd.Series(["A", "B", "C", .... "F", "A", "D"])

#2. using a python list
#grades = ["A", "B", "C", .... "F", "A", "D"]
#student_data["grade"] = grades

#3. using existing columns to create a new column
#example: 
#student_data["percentage"] = (student_data["mark"] / 100) * 100   

#to delete a column from the dataframe, we can use the drop() method

#to split into train, validation, and test sets, we randomize the order of the samples 
#do so using the sample() method
#frac=1 means 100% of the samples will be selected and they will be outputted in a random order 
student_data_sampled = student_data.sample(frac=1) 
print(student_data_sampled)

#to reset index to the default index, we can use the reset_index() method
#resets the index but also adds a new column with the old index values 
student_data_sampled.reset_index(inplace=True) 
print(student_data_sampled) 


#to apply a function to a column, we can use the apply() method
#example: 
#student_data_sampled["percentage"] = student_data_sampled["mark"].apply(lambda x: (x / 100) * 100)
#uses a lambda function because we are applying a function to a column and we are not passing in a function name  