# -*- coding: utf-8 -*-
"""LVADSUSR67-Aishwarya-FA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CYB_SYJtx9xCfMiTZneqyMR_-msVdQ5Y
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1
df=pd.read_csv('/content/Walmart_Dataset Python_Final_Assessment.csv')
df

#1
df.info()

#1
df.describe()

#1
df.dtypes

#1
#Finding if there are any null values in the dataframe
nan_count = df.isnull().sum().sum()
print(nan_count)

#2
#Finding if there's any null value in order ID column
nan_orderid = df['Order ID'].isnull().sum().sum()
print(nan_orderid)

"""As there are no null values in the data, there's no requirement of dropping or replacing null values"""

#2
# Replacing null values if any in Category to not given
df['Category'].fillna(value="not given",inplace=True)

#2
#Checkimg for any duplicate entries
duplicate = df[df.duplicated()]
print(duplicate)

#3
#The Measure of sales by category
df.groupby('Category')['Sales'].agg(['mean','median','std','sum','count','min','max','var'])

#3
df.groupby('Category')['Quantity'].agg(['mean','median','std','sum','count','min','max','var'])

#3
df.groupby('Category')['Profit'].agg(['mean','median','std','sum','count','min','max','var'])

#4
df1= df.groupby('Category')['Sales'].sum().reset_index().rename(columns={'sales':'sales'})
plt.figure(figsize= (8,10))
plt.pie(df1['Sales'], labels='Category', autopct='%0.1f%%',data=df1)
plt.show()
#This pie chart represents the percent of total sales amount for each category

#4
df1= df.groupby('Category')['Quantity'].sum().reset_index().rename(columns={'Qunatity':'Quantity'})
plt.figure(figsize= (8,10))
plt.pie(df1['Quantity'], labels='Category', autopct='%0.1f%%',data=df1)
plt.show()

#This chart represents the percent of total sales Quantity for each category

#4
df['Order Date'] = pd.to_datetime(df['Order Date'])
df1=df.groupby(df['Order Date'].dt.year)['Order ID'].count().reset_index().rename(columns={'Order ID':'Count of orders','Order Date':'Year'})
df1.set_index("Year",inplace=True)
print(df1)
sns.lineplot(x="Year",y="Count of orders",marker='o',data=df1)
plt.xlabel("Year")
plt.ylabel("No of Orders")
plt.grid()
plt.title("Plot of orders by year")
plt.show()

#5
df2=df1=df.groupby(df['Order Date'].dt.month)['Sales'].sum().reset_index().rename(columns={'Sales':'Sum of sales','Order Date':'Month'})
df2
sns.lineplot(x="Month",y="Sum of sales",marker='o',data=df2)
plt.figure(figsize= (8,10))
plt.show()

#5
df3=df.groupby('Category')['Profit'].sum().reset_index().rename(columns={'Profit':'Total'})
df3
sns.barplot(x="Category",y="Total",data=df3)
plt.figure(figsize= (20,20))

#5
df4=df.groupby(df['Order Date'].dt.year)['Profit'].mean().reset_index().rename(columns={'Order Date':'Year'})
df4
sns.barplot(x="Year",y="Profit",data=df4)
plt.xlabel("Year")
plt.ylabel("Avg Profit in Millions")
plt.title("Average Profit per year")
plt.show()

#5
df8=df.groupby(df['Order Date'].dt.year)['Sales','Profit'].agg({'Sales':'sum',
                                                   'Profit':'sum'}).reset_index().rename(columns={'Order Date':'Year'})
df8.set_index("Year",inplace=True)
df8

sns.heatmap(df8, annot=True, fmt='f')
plt.show()

#6
df8=df.groupby(df['Category'])['Quantity'].sum().reset_index().rename(columns={'Qunatity':'Category'})
df8
plt.figure(figsize=(10, 6))
sns.boxplot(df8)
plt.title('Count of quantity by Category')
plt.grid(True)
plt.show()

#7
df5=df.groupby(df['Order Date'].dt.year)['Sales'].sum().reset_index().rename(columns={'Order Date':'Year','Sales':'Total Sales'})
df5
sns.lineplot(x="Year",y="Total Sales",marker='o',label='sales',data=df5)
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.title("Sales trend over the years")
plt.show()

#7
df6=df.groupby(df['Order Date'].dt.year)['Profit'].sum().reset_index().rename(columns={'Order Date':'Year','Profit':'Total Profit'})
df6
sns.lineplot(x="Year",y="Total Profit",marker='o',data=df6)
plt.xlabel("Year")
plt.ylabel("Total Profit")
plt.title("Profit trend over the years")
plt.show()

#7
df6=df.groupby([df['Order Date'].dt.year,'Category'])['Sales'].sum().reset_index().rename(columns={'Order Date':'Year','Sales':'Total Sales'})

df6

df7=df6[df6['Total Sales']==df6['Total Sales'].max()]
df7

#7
#customer analysis 1
df8=df.groupby('EmailID')['Order ID','Sales'].agg({'Order ID':'count',
                                                   'Sales':'sum'}).reset_index().rename(columns={'Order ID':'NO of orders','Sales':"Purchase_amount"})
df8.sort_values(by=['NO of orders', 'Purchase_amount']).tail()

#7
# customer analysis 2

df['Order Date'] =df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date']=df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['diff_days'] = (df['Ship Date'] - df['Order Date']) / np.timedelta64(1, 'D')
df9=df.groupby('EmailID')['diff_days'].mean()
df9

#7
# Comprehensive Analysis
1.Streamlining orders
2. The shipping and delivery service
3. Understanding the demand of the products

#7
#Comprehensive Analysis
The underlying factors that contribute to the geographic distribution of sales are:
1. Prices of the products
2. Shipping rates to various countries or cities
3. The time taken for delivery

#7
# Comprehensive Analysis
The high value customers are:
1. Consistent with placing orders
2. Place orders with high Amount
3. Will place orders in regular intervals.