
Perform ‘Exploratory Data Analysis’ on the provided dataset ‘SampleSuperstore’ You are the business owner of the retail firm and want to see how your company is performing. You are interested in finding out the weak areas where you can work to make more profit. What all business problems you can derive by looking into the data?

import pandas.util.testing as tm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=pd.read_csv('SampleSuperstore.csv')
data.head(10)

data.info()

data.describe()

data.corr()

col=['Postal Code']
s=data.drop(columns=col,axis=1)
s.corr()

"""DATA VISUALIZATION"""

s.hist(bins=50, figsize=(15,15))
plt.show()

sns.countplot(x=data['Ship Mode'])

sns.countplot(x=data['Region'])

sns.countplot(x=data['Segment'])

sns.countplot(x=data['Category'])

sns.set(style="whitegrid")
plt.figure(2, figsize=(20,10))

sns.barplot(x='Sub-Category', y='Profit', data=data, palette='Spectral')

plt.figure(figsize=(10,10))
data['Sub-Category'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()

sns.countplot(x=data['State'], order=(data['State'].value_counts().head(20)).index)
plt.xticks(rotation=90)

sns.countplot(x=data['State'], order=(data['State'].value_counts().tail(20)).index)
plt.xticks(rotation=90)

states = data.groupby('State')[['Sales','Profit']].sum().sort_values(by='Sales' , ascending=False)
plt.figure(figsize=(30,30))
states[:25].plot(kind='bar', edgecolor="#000000", color=['blue', 'red'])
plt.title("Status of top 25 States")
plt.xlabel('States')
plt.ylabel('Total')
plt.grid(True)
states[25:].plot(kind='bar', edgecolor="#000000", color=['blue', 'red'])
plt.title("Status of bottom 25 States")
plt.xlabel('States')
plt.ylabel('Total')
plt.grid(True)

data.groupby('Sub-Category')['Profit','Sales'].sum().plot.bar(color=['cyan'  , 'black'])
plt.figure(figsize=(30,30))

pd.DataFrame(data.groupby('State').sum())['Profit'].sort_values(ascending=True)
pd.DataFrame(data.groupby('State').sum())['Discount'].sort_values(ascending=True)

plt.figure(figsize = (20,5))
sns.lineplot('Discount', 'Profit', data = data, color ='orange', label= 'Discount')
plt.legend()
