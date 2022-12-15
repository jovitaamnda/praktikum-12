# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 23:56:55 2022

@author: jovita amanda putri
"""


import pandas as pd

data = pd.read_csv("Negara.csv")

df = pd.DataFrame(data)
mean = df.groupby(["Benua"]).mean()
std = df.groupby(["Benua"]).std()

print(data)
print(mean)
print(std)
