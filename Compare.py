# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 21:50:26 2019

@author: Ariadna
"""
import numpy

def Compare(A,B):
    X=numpy.load(A)
    Y=numpy.load(B)
    return X-Y
    