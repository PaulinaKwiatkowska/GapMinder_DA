# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:26:05 2017

@author: Paulina
"""

import pandas as pd
import scipy.stats 
import matplotlib.pyplot as plt

data=pd.read_csv(r'C:\Users\Robert\Desktop\Python\gapminder.csv',sep=",",
                index_col=0, header=0, skipinitialspace=True)

sub1 = data[["hivrate","lifeexpectancy","incomeperperson"]].dropna()
data_clean=data.dropna()

print 'association between incomeperperson and lifeexpectancy'
print (scipy.stats.pearsonr(data_clean['incomeperperson'], data_clean['lifeexpectancy']))

print 'association between lifeexpectancy and hivrate'
print (scipy.stats.pearsonr(data_clean['lifeexpectancy'], data_clean['hivrate']))

plt.figure(1)
x=data['incomeperperson']
y=data['lifeexpectancy']
plt.scatter(x,y,s=1)
plt.xlabel('incomeperperson')
plt.ylabel('lifeexpectancy')

plt.figure(2)
x=data['hivrate']
y=data['lifeexpectancy']
plt.scatter(x,y,s=1)
plt.xlabel('hivrate')
plt.ylabel('lifeexpectancy')