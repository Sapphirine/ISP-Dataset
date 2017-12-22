#Import Libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import fill_between

country = pd.read_csv('c://X/main/Country.csv')
indicators = pd.read_csv('c://X/main/Indicators.csv')

for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)
    
FBS_OM = indicators[(indicators.CountryName=='Oman')&(indicators.IndicatorCode=='IT.NET.BBND')]
FBS_KW = indicators[(indicators.CountryName=='Kuwait')&(indicators.IndicatorCode=='IT.NET.BBND')]
FBS_UA = indicators[(indicators.CountryName=='UAE')&(indicators.IndicatorCode=='IT.NET.BBND')]

fig = plt.figure()

plt.plot(FBS_OM.Year,FBS_OM.Value,'o-',label='OM',color=tableau20[0])
plt.plot(FBS_KW.Year,FBS_KW.Value,'o-',label='KW',color=tableau20[2])
plt.plot(FBS_UA.Year,FBS_UA.Value,'o-',label='UA',color=tableau20[1])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlabel('X',  fontsize=14)
plt.ylabel('Y',  fontsize=14)
plt.title('Script1', fontsize=14)

fig.savefig('Testxxx_var1_var2.pdf',format='pdf', dpi=300)