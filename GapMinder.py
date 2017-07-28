# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:26:05 2017

@author: Paulina
"""

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 

from statsmodels.stats.multicomp import pairwise_tukeyhsd

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
print df1["Income_category"]

sub1 = df1[["internetuserate","Income_category"]].dropna()

print sub1.groupby(df1["Income_category"]).mean()

# using ols function for calculating the F-statistic and associated p value
model1 = smf.ols(formula='internetuserate ~ C(Income_category)', data=sub1)
results1 = model1.fit()
print (results1.summary())

mc1 = multi.MultiComparison(sub1['internetuserate'], sub1['Income_category'])
print mc1
res1 = mc1.tukeyhsd()

print res1.summary()

#print pairwise_tukeyhsd(sub1['internetuserate'], sub1['Income_category'])

