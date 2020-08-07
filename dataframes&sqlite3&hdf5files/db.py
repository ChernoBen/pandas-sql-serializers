# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:50:04 2020

@author: benja
"""


'''
dataframes end databases
'''
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

frame = pd.DataFrame(np.arange(20).reshape(4,5),
                     columns=['white','red','blue','black','green'])

'''
implementando conexão com sqlite3
'''
engine = create_engine('sqlite:///foo.db')

'''
convetendo dataframe para uma tabela no db
'''
frame.to_sql('colors',engine)

'''
lendo tabela do db
'''
pd.read_sql('colors',engine)