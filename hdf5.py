# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:08:01 2020

@author: benja
"""
import pandas as pd
import numpy as np
import pickle
from pandas.io.pytables import HDFStore

'''
store df data within h5 file
'''

frame = pd.DataFrame(np.arange(16).reshape(4,4),
                     index = ['white','black','red','blue'],
                     columns = ['up','down','right','left'])

'''
creating hdf5 file
each dataframe is stored using a label in hdf5 file
'''
store = HDFStore('mydata.h5')
store['obj1'] = frame
store['obj2'] = frame

'''
serializando objetos python
'''
data = {'color':['white','red'],'value':[5,7]}
pickled_data = pickle.dumps(data)
print(pickled_data)

'''
deserializando dados
'''
nframe = pickle.loads(pickled_data)
print(nframe)

'''
serializando df e criando arquivo.pkl
'''
dframe = pd.DataFrame(np.arange(16).reshape(4,4),index = ['up','down','left','right'])
frame.to_pickle('frame.pkl')

