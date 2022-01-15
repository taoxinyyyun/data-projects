# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 01:11:58 2021

@author: flama
"""

import pandas as pd
import time
iter_csv = pd.read_csv(r'C:\Users\flama\Downloads\US_PlasticsTradebyPartner_ST202110251514_v2.csv',chunksize=500000)

df = pd.concat([chunk[chunk['Product'] == 'P_05'] for chunk in iter_csv])
df.to_csv('trade_partner_plastic.csv')



