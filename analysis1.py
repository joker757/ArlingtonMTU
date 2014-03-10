%matplotlib inline
import os
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mp1_style','default') #makes graphs pretty
plt.rcParams('figure.figsize') = (15, 5)
os.chdir('/Users/Josh/Desktop/datascience/Arlington_MTU')

MTU1 = pd.read.csv('2009_Custis_Rosslyn10.15_12.31_15mins.csv')

