#%%
# Import packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter  # Import PercentFormatter
import seaborn as sns
from datetime import datetime
from time import time
import warnings
warnings.filterwarnings("ignore")
import os
from scipy import stats

# from ucimlrepo import fetch_ucirepo 


# %%
# Import data: https://archive.ics.uci.edu/dataset/2/adult

# Fetch the dataset
adult = pd.read_csv("adult.csv")
adult

#%%
# Data information
# 3 columns with null values to be treated

print(adult.info())
adult.describe()

#%%
# Null data visualization

# Create a bar plot for null values
plt.figure(figsize=(8, 6))
adult.isna().sum().plot(kind='bar', color='b', edgecolor='black')
plt.title('Null Values in DataFrame')
plt.xlabel('Columns')
plt.ylabel('Null Count')
plt.xticks(rotation=45)


# Create boxplot for numerical data
numerical_df = adult.select_dtypes(include=int)
plt.figure(figsize=(10, 6))
numerical_df.boxplot()
plt.title('Boxplot of Described Statistics')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.show()

#%%
# We can see that the boxplot's visualization is bad due to 
# fnlwgt, with much greater values and more extreme outliers
# NORMALIZAÇÃO [0,1]
for col, max_val in numerical_df.max().items():
    numerical_df[col] /= max_val
plt.figure(figsize=(10, 6))
numerical_df.boxplot()
plt.title('Boxplot of Described Statistics')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.show()

# Conclusions: education and age are far more sparse, whereas capital gain/loss and hours per week are have a clear concentration



#%%
# Age and education distribution analysis

sns.distplot(adult['age'], bins=20)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()

sns.distplot(adult['education-num'], bins=10)
plt.title('Distribution of Education')
plt.xlabel('Education Years')
plt.ylabel('Density')
plt.show()

# Calculate common statistical metrics
data = adult.age
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)
std_dev = np.std(data)
variance = np.var(data)
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

# Display the metrics in a table format
print("===== Statistical Metrics - Age =====")
print("---------------------")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode.mode} (with frequency {mode.count})")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosis}")


#%%
# Age x income relationship
# Define age ranges
bins = [10, 30, 40, 50, 60, 70,1000]  # Adjust as needed
age_ranges = ['<29', '30-39', '40-49', '50-59', '60-69', '70+']

# Create a new column 'age_range' based on age bins
adult['age_range'] = pd.cut(adult['age'], bins=bins, labels=age_ranges)

grouped = adult.groupby(['age_range', 'income']).fnlwgt.agg('sum').unstack().fillna(0)
grouped['Percentage'] = grouped['>50K'] / (grouped['<=50K']+grouped['>50K'])

# Create a stacked bar chart
ax1 = grouped.drop('Percentage', axis=1).plot(kind='bar', stacked=True, color=['y', 'g'], figsize=(10, 6))

# Customize the plot
plt.title('Income Category by Age Range')
plt.xlabel('Age Range')
plt.ylabel('Count')
plt.xticks(rotation=0)
# Add the second y-axis for High income percentage
ax2 = ax1.twinx()
ax2.plot(grouped.index, grouped['Percentage'], marker='X', markersize=10, color='red', linestyle='--', label='High Income %')

# Customize the second y-axis
ax2.set_ylabel('High Income Percentage')
ax2.set_ylim(0, 0.6)  # Set the y-axis limits between 0% and 60%
ax2.yaxis.set_major_formatter(PercentFormatter(1))
ax2.legend(loc='upper right')

# Show the plot
plt.show()

#%%
# Education x income relationship

custom_order = adult.groupby('education')['education-num'].agg('mean').sort_values().index
grouped = adult.groupby(['education', 'income']).fnlwgt.agg('sum').unstack().fillna(0)
grouped['Percentage'] = grouped['>50K'] / (grouped['<=50K']+grouped['>50K'])
grouped = grouped.reindex(custom_order)
# Create a stacked bar chart
ax1 = grouped.drop('Percentage', axis=1).plot(kind='bar', stacked=True, color=['y', 'g'], figsize=(10, 6))

# Customize the plot
plt.title('Income Category by Age Range')
plt.xlabel('Age Range')
plt.ylabel('Count')
plt.xticks(rotation=45)
# Add the second y-axis for High income percentage
ax2 = ax1.twinx()
ax2.plot(grouped.index, grouped['Percentage'], marker='X', markersize=10, color='red', linestyle='--', label='High Income %')

# Customize the second y-axis
ax2.set_ylabel('High Income Percentage')
ax2.set_ylim(0, 1)  # Set the y-axis limits between 0% and 60%
ax2.yaxis.set_major_formatter(PercentFormatter(1))
ax2.legend(loc='upper right')

# Show the plot
plt.show()


#%%

# Assimetria, kurtosys etc.
# scatterplot, heatmap
# outliers: explicar no boxplot acho que já tá bom




#%%
# Heatmap education x 

rich = adult[adult.income=='>50K']
freq_rich = pd.crosstab(rich.education, rich.age_range).fillna(0)
freq_total = pd.crosstab(adult.education, adult.age_range).fillna(0)
freq_percent = freq_rich / freq_total
freq_percent = freq_percent.fillna(0).reindex(custom_order)

plt.figure(figsize=(8, 6))
sns.heatmap(freq_percent, annot=False, cmap='plasma')

# Customize the plot
plt.title('High Income Percentage X Age X Education')
plt.xlabel('Education')
plt.ylabel('Age')

# Show the heatmap
plt.show()



# %%
