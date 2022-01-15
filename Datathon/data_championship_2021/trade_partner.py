# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 17:47:38 2021

@author: flama
"""

import pandas as pd

countries = ['Japan', 'United States of America',
       'Thailand', 'Germany', 'Philippines', 'Belgium', 'Australia',
       'Indonesia', 'Malaysia', 'Korea, Republic of', 'Canada',
       'Viet Nam', 'Netherlands', 'United Kingdom', 'Mexico',
       'Spain', 'France']

tp = pd.read_csv('trade_partner_p05_no_org.csv')

tp = tp[tp['Economy Label'].isin(countries)]

tp_import = tp[tp['Flow'] == 1]
tp_export = tp[tp['Flow'] == 2]

tp_import = tp_import.groupby(['Year','Economy']).sum()
tp_export = tp_export.groupby(['Year','Economy']).sum()

import_export = pd.merge(tp_import,tp_export,on=['Year','Economy']).reset_index()

import_export = import_export[['Economy','Year','Metric tons in thousands_y', \
                              'Metric tons in thousands_x']]
    
ct_code = pd.read_csv('country_code.csv')
ct_dic = dict(zip(ct_code['Economy'],ct_code['Economy Label']))

import_export['Economy'] = import_export['Economy'].map(lambda x: ct_dic[x])
import_export.rename({'Economy':'Country'},axis=1,inplace=True)
import_export.to_csv('import_export20.csv')