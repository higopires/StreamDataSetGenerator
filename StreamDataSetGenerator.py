# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 23:10:53 2020

@author: Higo Felipe
"""

import pandas as pd
import numpy as np
date_rng = pd.date_range(start='7/22/2019', end='7/22/2020', freq='S')

df = pd.DataFrame(date_rng, columns=['start_timestamp'])
df['end_timestamp'] = date_rng
df['start_timestamp'] = np.random.randint(1563753600,1595376000,size=(len(date_rng)))
df['end_timestamp'] = np.random.randint(1563753600,1595376000,size=(len(date_rng)))
df = df[(df.end_timestamp/df.start_timestamp<=1.0000009)&(df.end_timestamp/df.start_timestamp>=1.0000001)]
df = df.to_numpy()
df = df.reshape(df.shape[0]*2,1)
df = np.sort(df,axis=0)
df = df.reshape(int(df.shape[0]/2),2)
df = pd.DataFrame(df,columns=['start_timestamp','end_timestamp'])
df['start_timestamp'] = pd.to_datetime(df['start_timestamp'],unit='s')
df['end_timestamp'] = pd.to_datetime(df['end_timestamp'],unit='s')
df.to_csv('luxanimo_u00.csv',index=False)