# -*- coding: utf-8 -*-
"""KAGGLE PROJECT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fyzRgZoORsGCCCmNWR6UW7k6ITi7BUOp

MY MINI PROJECT
This is my first personal project on Python. 
WTF2023/DS/B/008
"""

# Code to read csv file into Colaboratory:
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# Commented out IPython magic to ensure Python compatibility.
link= 'https://drive.google.com/file/d/1jmKaQ7hT81zi8xdYr0uwyWc9q58cop-V/view?usp=sharing'
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
# %matplotlib inline

# to get the id part of the file
id = link.split("/")[-2]
 
downloaded = drive.CreateFile({'id':id})
downloaded.GetContentFile('dc-wikia-data.csv') 
 
df= pd.read_csv('dc-wikia-data.csv',index_col='page_id')
df.head(2)

"""CLEANING OF DATA"""

df.info()

#The GSM column only have 64 non-null rows, so because it will not give any reliable descriptive information. i dropped it
df.drop(columns='GSM', inplace=True)

# Filled the NaN in ALIVE column with "Deceased Characters"
values = {"ALIVE": "Deceased Characters"}
df.fillna(value=values,inplace =True)

# Filled the NaN in SEX column with "Genderless Characters"
values = {"SEX": "Genderless Characters"}
df.fillna(value=values,inplace =True)

# Filled the NaN in EYE column with "Unknown"
values = {"EYE": "Unknown"}
df.fillna(value=values,inplace =True)

# Filled the NaN in HAIR column with "Unknown"
values = {"HAIR": "Unknown"}
df.fillna(value=values,inplace =True)

# 2 rows in 'FIRST APPEARANCE' column seem to have unknown datatype, thus resulting to extra complication ...
invalid=df.loc[df['FIRST APPEARANCE'] == '1988, Holiday']
invalid

#.. drop it
df.drop([4728,4935], inplace = True)

# select index of the missing values in the YEAR column
p=df.loc[df['YEAR'].isnull()]
p.index

#drop it
df.drop(p.index, inplace = True)

#convert FIRST APPEARANCE column to a datetime object
time_col = 'FIRST APPEARANCE'
df[time_col] = pd.to_datetime(df[time_col])

df.info()

"""      VISUALIZATION"""

p = sns.barplot(x = 'ALIVE', y= 'APPEARANCES',
               data = df);
p.set(title ='Comparison of the Living Charactrs and the Deceased Characters')

fig = plt.figure(figsize = (25, 5))
 
# creating the bar plot
sns.barplot(x = 'EYE',y = 'APPEARANCES',hue='SEX',data = df)
plt.title=('Eye and Appearance')
plt.show()

fig = plt.figure(figsize = (25, 5))
 
# creating the bar plot
sns.barplot(x = 'HAIR',y = 'APPEARANCES',hue='SEX',data = df)
plt.title=('Hair and Appearances')