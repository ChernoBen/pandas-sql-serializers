# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:41:07 2020

@author: benja
"""

import numpy as np
import pandas as pd

frame1 = pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                       'price':[12.33,11.33,33.21,13.23,33.56]})

frame2 = pd.DataFrame(
    {'id':['pencil','pencil','ball','pen'],
     'color':['white','red','red','black']})


'''
merging dataframes
retorna um dataframe cujo as tabelas possuem id em comum
'''
merged = pd.merge(frame1,frame2)

'''
 ordenado por label
'''
frame3 = pd.DataFrame( {'id':['ball','pencil','pen','mug','ashtray'],
                        'color': ['white','red','red','black','green'],
                        'brand': ['OMG','ABC','ABC','POD','POD']})

frame4 = pd.DataFrame( {'id':['pencil','pencil','ball','pen'],
                        'brand': ['OMG','POD','ABC','POD']})
 

merged2 = pd.merge(frame3,frame4,on = 'id')
