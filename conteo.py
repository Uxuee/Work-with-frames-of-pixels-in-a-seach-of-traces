# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:45:53 2019

@author: Ariadna
"""
import numpy as np

def Conteo(U):
    #m=5038848
    unique, counts = np.unique(U, return_counts=True)
    X=dict(zip(unique, counts))
    return X
