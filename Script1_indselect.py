import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re
df = pd.read_csv('c://X/main/Indicators.csv')
Indicator_array =  df[['IndicatorName','IndicatorCode']].drop_duplicates().values
modified_indicators = []
unique_indicator_codes = []
for ele in Indicator_array:
    indicator = ele[0]
    indicator_code = ele[1].strip()
    if indicator_code not in unique_indicator_codes:
        new_indicator = re.sub('[,()]',"",indicator).lower()
        new_indicator = re.sub('-'," to ",new_indicator).lower()
        modified_indicators.append([new_indicator,indicator_code])
        unique_indicator_codes.append(indicator_code)

Indicators = pd.DataFrame(modified_indicators,columns=['IndicatorName','IndicatorCode'])
Indicators = Indicators.drop_duplicates()
print(Indicators.shape)

key_word_dict = {}
key_word_dict['Demography'] = ['population']
key_word_dict['Trade'] = ['trade','import','export','good','shipping','shipment']
key_word_dict['Economy'] = ['income','gdp','gni','infrastructure']
key_word_dict['Energy'] = ['fuel','energy','power']
key_word_dict['Employment'] =['employed','employment','umemployed','unemployment']

feature = 'Trade'
for indicator_ele in Indicators.values:
    for ele in key_word_dict[feature]:
        word_list = indicator_ele[0].split()
        if ele in word_list or ele+'s' in word_list:
            print(indicator_ele)
            break