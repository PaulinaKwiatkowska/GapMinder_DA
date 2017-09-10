# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:26:05 2017

@author: Paulina
"""

import pandas as pd
import numpy
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv(r'C:\Users\Robert\Desktop\Python\gapminder.csv',sep=",",
                index_col=0, header=0, skipinitialspace=True)

sub1 = data[["urbanrate","alcconsumption"]].dropna()
data_clean=data.dropna()

print 'OLS regresion model for the association betwen urban rate and alcohol consumption'
reg1=smf.ols('urbanrate ~ alcconsumption', data=data).fit()
print (reg1.summary())

scat1 = sns.regplot(x="urbanrate", y="alcconsumption", data=data)
plt.xlabel('Urban Rate')
plt.ylabel('Alcohol consumption')
plt.title('Scatterplot for the Association Between Urban Rate and Alcohol consumption')