# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 00:01:03 2021

@author: flama
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 

tm = pd.read_csv('trade_partner_plastic.csv')
waste = pd.read_csv('y_value.csv')

country = pd.read_csv('country_code.csv')
country_dic = dict(zip(country['Economy'],country['Economy Label']))
country_dic[18] = 'Korea'
country_dic[842] = 'United States'
product = pd.read_csv('product_code.csv')
tm = tm[tm['Economy'].isin(country_dic.keys())]
tm['Economy'] = tm['Economy'].map(lambda x: country_dic[x])

tm_import = tm[tm['Flow']==1].groupby(['Year','Economy'])['Metric tons in thousands'].sum()
tm_export = tm[tm['Flow']==2].groupby(['Year','Economy'])['Metric tons in thousands'].sum()

y_value = pd.merge(tm_import, tm_export, on =['Economy','Year'], how='inner').reset_index()
y_value = y_value.rename(columns={'Economy':'Country'}, errors='raise')
y_value.to_csv('import_export.csv')
y_value = pd.merge(y_value, waste, on =['Country','Year'], how='inner').reset_index()


# countries = ['Japan', 'United States of America', 'Thailand', 'Germany', \
#              'Philippines', 'Belgium', 'Australia', 'Indonesia', 'Canada', \
#             'Korea']

# pvc_waste_export = tm[(tm['SitcRev3Product'] == 579) & (tm['Flow'] == 2)]
# pvc_waste_import = tm[(tm['SitcRev3Product'] == 579) & (tm['Flow'] == 1)]

# imports = pvc_waste_import.groupby('Year')['US dollars at current prices in thousands'].sum()
# exports = pvc_waste_export.groupby('Year')['US dollars at current prices in thousands'].sum()

# plt.figure()
# plt.title("Plastic Waste Export")
# plt.legend()
# plt.plot(exports)
# plt.ylabel('US dollars at current prices')
# plt.xticks(rotation=45)
# plt.show()

# plt.figure()
# plt.title("Plastic Waste Import")
# plt.legend()
# plt.plot(imports)
# plt.ylabel('US dollars at current prices')
# plt.xticks(rotation=45)
# plt.show()