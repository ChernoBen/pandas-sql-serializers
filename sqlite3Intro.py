# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 12:04:30 2020

@author: benja
"""


import sqlite3
import pandas as pd
import numpy as np


'''
criando conexão e executando querys
'''
query = """ CREATE TABLE test(a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);"""
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()

'''
primeira inserção
'''
data = [
        ('white','up',1,3),
        ('black','down',2,8),
        ('green','up',4,4),
        ('red','down',5,5)]

stmt = "INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt,data)
con.commit()

'''
criando select
'''
cursor = con.execute('select * from test')
rows = cursor.fetchall()#fatia as linhas da tabela e insere em uma lista
print(rows)
'''
obter os nomes das colunas
'''
cursor.description

'''
criando um dataframe com dados do banco
'''
dfsql = pd.DataFrame(rows, columns =['a','b','c','d'])