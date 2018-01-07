# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:26:05 2017

@author: Paulina
"""

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv(r'C:\Users\Robert\Desktop\Python\gapminder.csv',sep=",",
                index_col=0, header=0, skipinitialspace=True)

sub1 = data[["urbanrate","alcconsumption","employrate"]].dropna()
data_clean=data.dropna()

#first order (linear) scatterplot
scat1 = sns.regplot(x="urbanrate", y="alcconsumption", scatter=True, data=sub1)
plt.xlabel('Urbanization Rate')
plt.ylabel('Alcohol consumption Rate')

# fit second order polynomial
# run the 2 scatterplots together to get both linear and second order fit lines
scat1 = sns.regplot(x="urbanrate", y="alcconsumption", scatter=True, order=2, data=sub1)
plt.xlabel('Urbanization Rate')
plt.ylabel('Alcohol consumption Rate')

# center quantitative IVs for regression analysis
sub1['urbanrate_c'] = (sub1['urbanrate'] - sub1['urbanrate'].mean())
sub1['employrate_c'] = (sub1['employrate'] - sub1['employrate'].mean())
sub1[["urbanrate_c", "employrate_c"]].describe()

# linear regression analysis
reg1 = smf.ols('alcconsumption ~ urbanrate_c', data=sub1).fit()
print (reg1.summary())

# adding employment rate
reg3 = smf.ols('alcconsumption  ~ urbanrate_c + I(urbanrate_c**2) + employrate_c',data=sub1).fit()
print (reg3.summary())

#Q-Q plot for normality
fig4=sm.qqplot(reg3.resid, line='r')

# simple plot of residuals
stdres=pd.DataFrame(reg3.resid_pearson)
plt.plot(stdres, 'o', ls='None')
l = plt.axhline(y=0, color='r')
plt.ylabel('Standardized Residual')
plt.xlabel('Observation Number')


# additional regression diagnostic plots
fig2 = plt.figure(figsize=(12,8))
fig2 = sm.graphics.plot_regress_exog(reg3, "employrate_c", fig=fig2)

# leverage plot
fig3=sm.graphics.influence_plot(reg3, size=8)
print(fig3)