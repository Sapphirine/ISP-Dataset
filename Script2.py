%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
plt.style.use('ggplot')

chosen_indicators = ['IE.PPI.TELE.CD', 'IT.CEL.SETS', 'SIT.CEL.SETS.p2', 'IT.NET.USER.ZS', \
                     'IT.NET.BBND', 'IT.NET.BBND.p2' ]

df_s = df[df['IndicatorCode'].isin(chosen_indicators)]

df_om = df_subset[df['CountryName']=="Oman"]

def plot_indicator(indicator,delta=10):
    ds_f = df_s[['IndicatorName','Year','Value']][df_s['IndicatorCode']==indicator]
    try:
        title = df_s['IndicatorName'].iloc[0]
    except:
        title = "None"

    x1 = df_s['Year'].values
  
    plt.figure(figsize=(20,5))
