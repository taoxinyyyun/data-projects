# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 00:52:11 2021

@author: flama
"""

from matplotlib import pyplot as plt
from sklearn import tree
import pandas as pd
import numpy as np

Top_imports = ['Japan', 'United States',
       'Thailand', 'Germany', 'Philippines', 'Belgium', 'Australia',
       'Indonesia', 'Malaysia', 'Korea, Republic of', 'Canada',
       'Viet Nam', 'Netherlands', 'United Kingdom', 'Mexico',
       'Spain', 'France']

effect = pd.read_csv('effect_country.csv')

ratio = pd.read_csv('MUNW_21112021064622284.csv')
ratio = ratio[ratio['Country'].isin(Top_imports)]

ratio = ratio.pivot(index=['Country','Year'],columns='Variable')
ratio = ratio.iloc[:,65:72].reset_index()
ratio.rename(dict(zip(ratio.columns,[i[1] for i in ratio.columns])),inplace=True,axis=1)
ratio.columns = ratio.columns.get_level_values(1)
tmp = list(ratio.columns)
tmp[0],tmp[1] = 'Country','Year'
ratio.columns = tmp

ratio = ratio.groupby('Country').mean()
ratio.drop('% Other disposal', inplace=True,axis=1)

final = pd.merge(ratio,effect,on='Country')
final.dropna(inplace=True)

# country = country[country['Country'].isin(Top_imports)]

# country = country.iloc[:,2:-2]
# country = country[['Coastal population2','Inadequately managed plastic waste [kg/day]7']]
# effect = effect[~effect['Country'].isin(['Thailand','Korea, Republic of', 'Viet Nam'])]

# # country = country.dropna(how='all',axis=1,inplace=True)
# # country = (country-country.mean())/country.std()
# # effect.iloc[:,1] = (effect.iloc[:,1]-effect.iloc[:,1].mean())/effect.iloc[:,1].std()

clf = tree.DecisionTreeRegressor(max_depth=3)
clf = clf.fit(final.iloc[:,2:6], final.iloc[:,-1])
plt.figure(figsize=(20,20))
tree.plot_tree(clf)
plt.show()

for idx, val in enumerate(final.iloc[:,2:6].columns):
    print(idx, val)
    print()