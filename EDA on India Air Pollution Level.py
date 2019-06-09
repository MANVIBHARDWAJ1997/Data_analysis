# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:53:34 2019

@author: DELL PC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv('data.csv',encoding='ISO-8859-1')
df.describe()
df.count() #it results in a number of non null values
df.shape #no. of rows and columns
df.isnull().sum() #it gives out the number of null values in each column
df.info() #it returns range,column,number of non-null objects of each column,datatype and memory usage
df.head(5)

##cleaning the dataset
df.drop(['stn_code','agency','sampling_date','location_monitoring_station'],axis=1,inplace=True)
data = df.dropna(subset=['date']) #dropping rows where no date is available
data.columns
#type column include several names and most of which are same so remove this type of stuff and make it uniform
types = {
        'Residential':'R',
        'Residental and others': 'RO',
        'Residental,Rural and other Areas':'RRO',
        'Industrial Area':'I',
        'Industrail Areas':'I',
        'Industrail':'I',
        'Sensitive Area':'S',
        'Sensitive Areas':'S',
        'Sensitive':'S',
        np.nan:'RRO'
        }
data.type = data.type.replace(types)
data.head()
#to get the new column of year we have to first convert the date column to datetime format
data['date'] = pd.to_datetime(data['date'],errors='coerce')
data.head(5)
data['year'] = data.date.dt.year
data.head(5)

##handling missing values
#here we use imputer from sklearn to fill missing values of column with the mean
COLS = ['so2','no2','rspm','spm','pm2_5']
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values=np.nan, strategy='mean')
data[COLS] = imputer.fit_transform(data[COLS])
data.head(5)
data.info()
data.isnull().sum() #now no null values are there

#so2 status
statewise_so2=data[['so2','state']].groupby('state',as_index=False).median().sort_values(by='so2')
statewise_so2.head(10)
statewise_so2.plot(kind='bar',x='state',y='so2')
#no2 status
statewise_so2=data[['so2','state']].groupby('state',as_index=False).median().sort_values(by='so2')
statewise_so2.head(10)
statewise_so2.plot(kind='bar',x='state',y='so2')
#rspm status
statewise_rspm=data[['rspm','state']].groupby('state',as_index=False).median().sort_values(by='rspm')
statewise_rspm.head(10)
statewise_rspm.plot(kind='bar',x='state',y='rspm')
#spm status
statewise_spm=data[['spm','state']].groupby('state',as_index=False).median().sort_values(by='spm')
statewise_spm.head(10)
statewise_spm.plot(kind='bar',x='state',y='spm')

#now with the AP state only
andhra = data[data['state']=='Andhra Pradesh']
year_wise_AP = andhra[['so2','no2','rspm','spm','year']].groupby('year').median()
year_wise_AP.head()
plt.plot(year_wise_AP['so2'],'-sc',markersize = 3)
plt.plot(year_wise_AP['no2'],'-or',markersize = 3)
plt.legend()

plt.plot(year_wise_AP['rspm'],'-ob',markersize = 3)
plt.plot(year_wise_AP['spm'],'-om',markersize = 3)
plt.legend()
#shows that the value of spm increases in AP from 2010 to 2015
#spm meaans suspended particulate matter
#spm,rspm,no2 and so2 are the main parameters used to measure the quality of air.

















