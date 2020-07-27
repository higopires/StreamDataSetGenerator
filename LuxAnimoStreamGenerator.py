# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:30:36 2020

@author: Higo Felipe
"""

import random
import pandas as pd

init = 1595462400

dataset = open("luxanimo2.csv","a")
dataset.write("start_timestamp,end_timestamp\n")

for x in range(72):
    if(random.randint(1,100)<=100):
        dataset.write("%s,%s\n"%(pd.to_datetime(init,unit='s')
                                 , pd.to_datetime(init+300,unit='s')))
    init+=301

for x in range(24):
    if(random.randint(1,100)<=30):
        dataset.write("%s,%s\n"%(pd.to_datetime(init,unit='s')
                                 , pd.to_datetime(init+300,unit='s')))
    init+=301

for x in range(120):
    if(random.randint(1,100)<=3):
        dataset.write("%s,%s\n"%(pd.to_datetime(init,unit='s')
                                 , pd.to_datetime(init+300,unit='s')))
    init+=301

for x in range(24):
    if(random.randint(1,100)<=7):
        dataset.write("%s,%s\n"%(pd.to_datetime(init,unit='s')
                                 , pd.to_datetime(init+300,unit='s')))
    init+=301

for x in range(48):
    if(random.randint(1,100)<=75):
        dataset.write("%s,%s\n"%(pd.to_datetime(init,unit='s')
                                 , pd.to_datetime(init+300,unit='s')))
    init+=301

dataset.close()