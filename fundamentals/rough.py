import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

heart_disease = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/heart-disease.csv")
print(heart_disease.head())

heart_disease.plot.hist(figsize=(5, 20), subplots=True)
plt.show() 



over_50 = heart_disease["age"] > 50  
print(over_50.head())
