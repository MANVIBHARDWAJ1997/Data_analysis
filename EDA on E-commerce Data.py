# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:47:55 2019

@author: DELL PC
"""

##cleaning data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import missingno as msno
import pandas_profiling
import gc
import datetime
%matplotlib inline 
color = sns.color_palette()
pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns',100)

df = pd.read_csv(r'data.csv',encoding='ISO-8859-1')
df.head()

#changing column names
df.rename(index=str,columns={'InvoiceNo':'invoice_num',
                             'StockCode':'stock_code',
                             'Description':'description',
                             'Quantity':'quantity',
                             'InvoiceDate':'invoice_date',
                             'UnitPrice':'unit_price',
                             'CustomerID':'cust_id',
                             'Country':'country'}, inplace=True)
df.head()
##data cleaning
df.info()
df.isnull().sum().sort_values(ascending=False)
df[df.isnull().any(axis=1)].head() #check out rows with missing values
#changing the invoice_date format 
df['invoice_date']=pd.to_datetime(df.invoice_date, format='%m/%d/%Y %H:%M')
df['description']=df.description.str.lower() #changing data to lower case
df.head()
#removing rows with missing values
df_new = df.dropna()
df_new.isnull().sum().sort_values(ascending=False)
df_new.info()
#changing column type
df_new['cust_id']=df_new['cust_id'].astype('int64')
df_new.head()
df_new.info()




















