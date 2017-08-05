# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:26:05 2017

@author: Paulina
"""

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 
import scipy.stats
        
df1=pd.read_csv(r'C:\Users\Robert\Desktop\Python\gapminder.csv',sep=",",
                index_col=0, header=0, skipinitialspace=True)

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
    
def urban_categories(row):
    '''
    This function divides countries into three categories based on their rate.
    This categorisation is arbitrary and defined by the author.
    '''
    if row["urbanrate"]<=33:
        return "High Rural"
    if row["urbanrate"]<=66:
        return "Mixed"
    else:
        return "Urban"
 
df1["Income_category"]=df1.apply(income_categories, axis=1)      
df1["Urbanisation_category"]=df1.apply(urban_categories, axis=1)
sub1=df1[["lifeexpectancy", "Income_category", "Urbanisation_category"]]
sub1=sub1.dropna(axis=0)
sub1=sub1.sort_values("lifeexpectancy")
print sub1

# contingency table of observed counts
ct1=pd.crosstab(sub1["Income_category"], sub1['Urbanisation_category'])

# chi-square
print 'chi-square value, p value, expected counts'
cs1= scipy.stats.chi2_contingency(ct1)
print (cs1)
print ct1