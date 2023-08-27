# -*- coding: utf-8 -*-
"""Amazing mart data project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nkxk2YXOmchExMgDZQqsHPYrc3ePh5SZ

We will be using matplotlib, seaborn for visualization
For mathematical and statisticla functions, we will be using numpy and pandas
"""

import pandas as pd
# pandas is aliased as pd
import numpy as np
# numpy is aliased as np
import matplotlib.pyplot as plt
# pyplot is aliased as plt
import seaborn as sns
# seaborn is aliased as sns

import warnings
warnings.filterwarnings('ignore')

df1 = pd.read_csv('/content/Order .csv',encoding='latin1')
# ,encoding='latin1'
df1.head()# top 5 rows

df1.isnull().sum()

df1.dtypes

"""#### 2) Extract all categorical columns and numerical columns

#### 3) Check duplicates
"""

df1.duplicated().sum()



"""After assessing df1, we've determined that it has a shape of (4117rows, 11 columns), indicating the dataset's size. The type of df1 is a pandas DataFrame, a structured tabular data format commonly used for analysis and manipulation."""

df2 = pd.read_csv('/content/Order_breakdown.csv',encoding='latin1')
# ,encoding='latin1'
df2.head()# top 5 rows

df2.isnull().sum()

df2.dtypes

"""After evaluating df2, we've found its shape to be (A rows, B columns), offering insights into its dimensions. Similar to df1, df2 is also a pandas DataFrame, providing a structured format for effective data handling and analysis.

**# Merging two different datasets into a single combined CSV file offers a more complete and valuable perspective on the subject at hand. By uniting complementary information from both datasets, we gain enhanced analytical capabilities, deeper insights, and a broader context for decision-making. The merged dataset reduces redundancy, improves accuracy, and provides a holistic view that was previously unattainable. This approach not only enhances reporting and visualization but also sets the stage for future expansion and integration. Overall, the merged CSV file unlocks more comprehensive analysis, leading to more informed and effective outcomes.**
"""

# Load the first CSV file
df1 = pd.read_csv('/content/Order .csv')

# Load the second CSV file
df2 = pd.read_csv('/content/Order_breakdown.csv')

# Combine DataFrames horizontally
combined_df = pd.concat([df1, df2], axis=1)

# Export combined data to a new CSV file
combined_df.to_csv('combined.csv', index=False)

df = pd.read_csv('/content/combined.csv')
df.head()# top 5 rows

df.shape
# num of rows = 8047, num of cols = 20

""" I want to merge the contents of two columns named "Order ID" and "Order ID.1" into a single column named "Order ID" and then remove any duplicate rows based on this merged column. Here's how I can achieve this using pandas:



"""

# Merge columns and drop duplicates
df['Order ID'] = df['Order ID'].astype(str) + '_' + df['Order ID.1'].astype(str)
df.drop(['Order ID.1'], axis=1, inplace=True)
df.drop_duplicates(subset=['Order ID'], keep='first', inplace=True)

print(df)

df.dtypes

"""### A) Data Preprocesing

#### 1) Check Null values
"""

df.isnull().sum()

# Columns with null values
columns_with_null = ['Order ID', 'Order Date', 'Customer Name', 'City', 'Country', 'Region', 'Segment', 'Ship Date', 'Ship Mode', 'State', 'Days to Ship']

# Fill categorical columns with 'Unknown'
df[columns_with_null] = df[columns_with_null].fillna('Unknown')

# For numerical columns, you can fill with 0
# df['Days to Ship'] = df['Days to Ship'].fillna(0)

print(df.isnull().sum())

"""Check Data Types"""

df.dtypes

#### 3) Check duplicates
df.duplicated().sum()

"""**Extract all categorical columns and numerical columns**"""

# cat_cols = categorical columns
# num_cols = numerical columns
# select_dtypes = it returns a dataframe
cat_cols = df.select_dtypes(include='object').columns
num_cols = df.select_dtypes(exclude='object').columns
print(cat_cols)
print(num_cols)

"""**##) Uni-variate EDA
Statistical or visual analysis of a single column (one variable)**

#### 1) Find Sub Category wise sum of Sales and depict it on a bar chart and depict highest and lowest shipping cost with different colors.

#### 1) Find Value counts of categroical columns namely Category, Segment, Sub-Category, Region, Ship Mode and Market. Depict the following
a) Catgeory count on a bar chart(matplotlib)<br>
b) Sub-category on a horizontal bar chart(matplotlib)<br>
c) Segment on a Pie Chart(matplotlib)<br>
d) Region on a bar chart(seaborn)<br>
e) Ship Mode on a line chart(matplotlib)<br>
"""

cat_cols

a1 = df['Category'].value_counts()
a1

plt.bar(a1.index,a1.values,color='lightgreen',edgecolor='black',label='Category counts')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Category Count - Vertical Bar Chart')
plt.legend()
plt.show()

a2 = df['Sub-Category'].value_counts()
a2

plt.barh(a2.index,a2.values,color='maroon',label='sub category count')
plt.ylabel('Sub-Category')
plt.xlabel('Count')
plt.title('Sub-Category Count - Horizontal Bar Chart')
plt.legend()
plt.show()

a3 = df['Segment'].value_counts()
a3

plt.pie(a3.values,labels=a3.index,autopct='%.2f%%')
plt.title('Segment Count Percentage distribution')
plt.legend()
plt.show()

a4 = df['Region'].value_counts()
print(type(a4)) # Series
a4

plt.bar(a4.index,a4.values,color='orange',edgecolor='black',label='Region count')
plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Region Count')
plt.legend()
plt.xticks(rotation=90)
plt.show()

sns.countplot(x= df['Region'])
plt.title('Region Count - Vertical Bar Chart')
plt.xticks(rotation=90)
plt.show()

a5 = df['Ship Mode'].value_counts()
a5

plt.plot(a5.index,a5.values,color='green',marker='o',label='Ship Mode count')
plt.xlabel('Ship Mode')
plt.ylabel('Count')
plt.title('Ship Mode Count')
plt.legend()
plt.show()

"""#### 2) Plot  the following
a) Histogram for Discount & Actual Discount<br>
b) Kdeplot/displot for Quantity
"""

plt.hist(df['Discount'])
plt.title('Frequency distribution for Discount')
plt.show()

plt.hist(df['Actual Discount'])
plt.title('Frequency distribution for Actual Discount')
plt.show()

sns.displot(x=df['Quantity'])
plt.title('Displot for Quantity')
plt.show()

sns.kdeplot(x=df['Quantity'])
plt.title('KDEplot for Quantity')
plt.show()

"""###  Bivariate Analysis

Statistical or Visual Analysis of 2 variables

#### 1) Depict the following on a Scatter plot
a)  Sales vs Profit <br>
b)  Profit vs Shpping Cost
"""

plt.scatter(df['Sales'],df['Profit'],color='red')
plt.title('Sales vs Profit - Scatter Chart')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()

"""#### 2) Depict Boxplot for the following
a) Quantity based on Segment<br>
b) Discount based on Ship Mode<br>
"""

sns.boxplot(x=df['Quantity'],y=df['Segment'])
plt.title('Boxplot - Quantity based on Segment')
plt.show()

sns.boxplot(x=df['Discount'],y=df['Ship Mode'])
plt.title('Boxplot - Discount based on Ship Mode')
plt.show()

"""#### 3) Depict the following

Quantity vs Category on a violinplot<br>
"""

sns.violinplot(x=df['Quantity'],y=df['Category'])
plt.title('Boxplot - Quantity based on Category')
plt.show()

"""#### 4) Plot pairplot for the categorical variables  including ['Sales','Profit','Quantity','Discount','Actual Discount']"""

sns.pairplot(df,vars=['Sales','Profit','Quantity','Discount','Actual Discount'])
plt.show()

print(num_cols)
print(cat_cols)

"""#### 5) Depict Correlation on a heatmap"""

corr = df.corr()
corr

sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.show()

"""**The process of preparing the "Amazing Mart Dataset" for machine learning, applying various machine learning techniques, evaluating the models, selecting the best model, and then saving and loading it. Here's a step-by-step approach**

Experiment with using 'Sales' and 'Actual Discount' as features ('Feature1' and 'Feature2') and 'Profit' as the target variable for my machine learning model. This setup suggests that i want to predict the profit based on the sales and actual discount values.

Here's a general outline of how you can proceed:

**Step 1:** Data Preprocessing
Load the dataset using pandas.
Choose the relevant columns: 'Sales', 'Actual Discount', and 'Profit'.
Handle any missing values in these columns.
Split the data into features (X) and the target variable (y).

**Step 2:** Choose a Model
Decide on the type of problem: regression (since i am  predicting a continuous variable, 'Profit').
Choose a regression model to work with, such as Linear Regression, Random Forest Regression, or Gradient Boosting Regression.
Step 3: Train and Evaluate the Model
Split your data into training and testing sets.
Train the selected regression model on the training data.
Use the trained model to predict 'Profit' on the testing data.
Evaluate the model's performance using regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Data Preprocessing
data = pd.read_csv('/content/combined.csv')

features = ['Sales', 'Actual Discount']
target = 'Profit'

X = data[features]
y = data[target]

# Step 2: Choose a Model
model = LinearRegression()  # You can try other regression models as well

# Step 3: Train and Evaluate the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Step 4: Interpret and Visualize Results
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Profit')
plt.ylabel('Predicted Profit')
plt.title('Actual vs. Predicted Profit')
plt.show()

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

"""Step 3: Train and Evaluate Different Models
For each technique, follow the same steps to split the data, train the model, make predictions, and evaluate using appropriate metrics. Here's a template for one technique:
"""

from sklearn.ensemble import RandomForestRegressor, BaggingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Prepare data and split into features (X) and target variable (y)

# Technique 1: Random Forest Regression
model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)
y_pred_rf = model_rf.predict(X_test)

# Evaluate
mae_rf = mean_absolute_error(y_test, y_pred_rf)
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

# Technique 2: Bagging Regression
model_bagging = BaggingRegressor()
model_bagging.fit(X_train, y_train)
y_pred_bagging = model_bagging.predict(X_test)

# Evaluate
mae_bagging = mean_absolute_error(y_test, y_pred_bagging)
mse_bagging = mean_squared_error(y_test, y_pred_bagging)
r2_bagging = r2_score(y_test, y_pred_bagging)

"""Step 4: Choose the Best Model
After evaluating all the models, compare their evaluation metrics (MAE, MSE, R-squared) to determine which model performs best.

Step 5: Save the Best Model
Once I'm  selected the best model, train it on the entire dataset and save it using joblib or another suitable method:
"""

import joblib

best_model = RandomForestRegressor()  # Replace with the best model you selected
best_model.fit(X, y)

# Save the best model
joblib.dump(best_model, 'best_model.pkl')

"""Step 6: Create and Test with New Dataset
Generate a new dataset by randomly selecting 20 data points from the original Amazing Mart dataset. Then, load the saved model and test it on this new dataset:
"""

# Load the saved model
loaded_model = joblib.load('best_model.pkl')

# Load your original dataset (replace with your actual dataset loading code)
original_data = pd.read_csv('/content/combined.csv')

# Create a new dataset (randomly select 20 data points)
new_data = original_data.sample(n=20, random_state=42)  # Modify as needed

# Define your features and target variable
features = ['Sales', 'Actual Discount']  # Modify as needed
target = 'Profit'  # Modify as needed

# Preprocess new_data similarly as before
new_X = new_data[features]
new_y = new_data[target]

# Predict using the loaded model
new_y_pred = loaded_model.predict(new_X)

# Evaluate the model's performance on the new dataset using metrics
new_mae = mean_absolute_error(new_y, new_y_pred)
new_mse = mean_squared_error(new_y, new_y_pred)
new_r2 = r2_score(new_y, new_y_pred)
print("Predicted Profits:")
print(new_y_pred)