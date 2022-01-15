# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 18:33:53 2021

@author: flama
"""

import pandas as pd
from statsmodels.api import OLS

pollution = pd.read_csv('y_value_from_percentage.csv')
effect = pd.read_csv('effect_country_year.csv')
year= ['2018','2019']
effect = pd.melt(effect,id_vars='Country',value_vars=year,value_name='effect')
effect.rename({'variable':'Year'},axis=1,inplace=True)
effect['Year'] = effect['Year'].astype(int)
countries = ['Japan', 'United States',
       'Thailand', 'Germany', 'Philippines', 'Belgium', 'Australia',
       'Indonesia', 'Malaysia', 'Korea', 'Canada',
       'Viet Nam', 'Netherlands', 'United Kingdom', 'Mexico',
       'Spain', 'France']

pollution = pollution.loc[pollution['Country'].isin(countries)]
pollution = pollution[pollution['Year'] >= 2018]
pollution = pollution[['Country','Year','plastic pollution per millions of people']]
final = pd.merge(pollution, effect, on=['Year','Country']).reset_index()
final = final.iloc[:,1:]
final['Country'] = final['Country'].astype('category')
final['Year'] = final['Year'].astype('category')

final = pd.get_dummies(final, prefix=['Country','Year'], drop_first = True)

noycol = list(final.columns)
noycol.remove('plastic pollution per millions of people')
final_x = final[noycol]
final_x['effect'] /= 1000

final_y = final['plastic pollution per millions of people']

print(OLS(final_y,final_x).fit().summary())
