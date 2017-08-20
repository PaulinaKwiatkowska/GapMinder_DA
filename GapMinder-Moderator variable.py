# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 10:48:03 2017

@author: Paulina
"""

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 
import scipy.stats
import seaborn
import matplotlib.pyplot as plt

def income_categories(row):
    
    '''
    This function divides countries into four income categories defined by the 
    World Bank.
    The current threshold values are valid for 2016.
    '''

    if row ["incomeperperson"]<=1025:
        return "Low"
    elif row["incomeperperson"]<=4035:
        return "Low middle"
    elif row["incomeperperson"]<=12475:
        return "Upper middle"
    else:
        return "High"
    
df1=pd.read_csv(r'C:\Users\Robert\Desktop\Python\gapminder.csv',sep=",",
                index_col=0, header=0, skipinitialspace=True)

#dividing into categories

df1["Income_category"]=df1.apply(income_categories, axis=1)

data_clean = df1[["lifeexpectancy","Income_category","alcconsumption"]].dropna()

sub1=data_clean[(data_clean['Income_category']== "Low")]
sub2=data_clean[(data_clean['Income_category']== "Low middle")]
sub3=data_clean[(data_clean['Income_category']== "Upper middle")]
sub4=data_clean[(data_clean['Income_category']== "High")]

print ('association between lifeexpectancy and alcconsumption for LOW income countries')
print (scipy.stats.pearsonr(sub1['lifeexpectancy'], sub1['alcconsumption']))
print ('       ')
print ('association between lifeexpectancy and alcconsumption for LOW MIDDLE income countries')
print (scipy.stats.pearsonr(sub2['lifeexpectancy'], sub2['alcconsumption']))
print ('       ')
print ('association between lifeexpectancy and alcconsumption for UPPER MIDDLE income countries')
print (scipy.stats.pearsonr(sub3['lifeexpectancy'], sub3['alcconsumption']))
print ('       ')
print ('association between lifeexpectancy and alcconsumption for High income countries')
print (scipy.stats.pearsonr(sub4['lifeexpectancy'], sub4['alcconsumption']))

plt.figure(1)
scat1 = seaborn.regplot(x="alcconsumption", y="lifeexpectancy", data=sub1)
plt.xlabel('Alcohol Consumption')
plt.ylabel('Life Expectancy')
plt.title('Scatterplot for the Association Between Life Expectancy and Alcohol Consumption for LOW income countries')
print (scat1)

plt.figure(2)
scat2 = seaborn.regplot(x="alcconsumption", y="lifeexpectancy", data=sub2)
plt.xlabel('Alcohol Consumption')
plt.ylabel('Life Expectancy')
plt.title('Scatterplot for the Association Between Life Expectancy and Alcohol Consumption for LOW MIDDLE income countries')
print (scat2)

plt.figure(3)
scat3 = seaborn.regplot(x="alcconsumption", y="lifeexpectancy", data=sub3)
plt.xlabel('Alcohol Consumption')
plt.ylabel('Life Expectancy')
plt.title('Scatterplot for the Association Between Life Expectancy and Alcohol Consumption for UPPER MIDDLE income countries')
print (scat3)

plt.figure(4)
scat4 = seaborn.regplot(x="alcconsumption", y="lifeexpectancy", data=sub4)
plt.xlabel('Alcohol Consumption')
plt.ylabel('Life Expectancy')
plt.title('Scatterplot for the Association Between Life Expectancy and Alcohol Consumption for HIGH income countries')
print (scat4)