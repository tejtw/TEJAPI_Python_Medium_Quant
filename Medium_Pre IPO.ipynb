# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:36:14 2022

@author: Mark
"""

import numpy as np
import pandas as pd
from scipy.stats.mstats import gmean
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
import tejapi
import time
tejapi.ApiConfig.api_key="EyUSGsEJr8ouhg7nDjtVrPcPlexvSI"
tejapi.ApiConfig.api_base="http://10.10.10.66"
tejapi.ApiConfig.ignoretz = True

#%%資料撈取整理計算報酬

df = pd.read_excel('C:/Users/Mark/Desktop/Python/PreIPO Python/TEST2.xlsx')
A1 = df[['代號','名稱','上市日收盤價(元)','上市日後一天收盤價(元)','上市日後二天收盤價(元)','上市日後三天收盤價(元)','上市日後四天收盤價(元)','上市日後五天收盤價(元)']]
# A1 = A1.rename(columns={"代號" : "公司簡稱"}, inplace = False)
A2 = A1[['上市日收盤價(元)','上市日後一天收盤價(元)','上市日後二天收盤價(元)','上市日後三天收盤價(元)','上市日後四天收盤價(元)','上市日後五天收盤價(元)']]
A3 = A2.copy()
for i in range(1, len(A2.columns)):
    A3.iloc[:,i:i+1] = ((A2.iloc[:,i:i+1].values)/(A2.iloc[:,0:1].values))-1
# 此段非單日日報酬計算，屬於累積報酬

# A3 = A2.T
# A3 = A3.pct_change(1)*100 
# A3 = A3.T
# 單日日報酬計算，需先將Dataframe矩陣轉置

# def culmulative(df,p):
#     df =df.copy()
#     df["後二日累積報酬率"]=df.rolling(p).gmean()    
#     return df
# CR = culmulative(A3 , 3)
# 無意義的一段

A3 = A3.rename(columns={'上市日後一天收盤價(元)' : '後一日累積報酬率%',
                        '上市日後二天收盤價(元)' : '後二日累積報酬率%', 
                        '上市日後三天收盤價(元)' : '後三日累積報酬率%', 
                        '上市日後四天收盤價(元)' : '後四日累積報酬率%', 
                        '上市日後五天收盤價(元)' : '後五日累積報酬率%'}, inplace = False)
data = A3.drop('上市日收盤價(元)',axis=1)
data1 = A1.join(data, how = "left")

Company = A1['代號'].to_list()
Detail = tejapi.get('TWN/AIND', chinese_column_name = True , paginate = True, coid = Company,
                    opts={'columns':['coid','ind1']}) # 舊產業名
Detail = Detail.rename(columns={"公司簡稱" : "代號"}, inplace = False)
#Detail['TSE 產業別'] = Detail['TSE 產業別'].map(lambda x : int(x))
qq = Detail[Detail['TSE 產業別'] != "17" ]
qq = qq[qq['TSE 產業別'] != "14" ]
qq = qq[qq['TSE 產業別'] != "19" ]
qq = qq[qq['TSE 產業別'] != "20" ]
qq = qq[qq['TSE 產業別'] != "80" ]
qq = qq[qq['TSE 產業別'] != "32" ]
qq = qq[qq['TSE 產業別'] != "33" ]
qq = qq[qq['TSE 產業別'] != "34" ]
qq = qq[qq['TSE 產業別'] != "91" ]
PreIPO = data1.merge(qq, on='代號')

#%%依照產業計算勝率繪製圖表

PreIPO = PreIPO.dropna(axis=0,how='any') # 清空NA
industry_name = np.unique(PreIPO[['TSE 產業別']])
payoff = np.array(['後一日累積報酬率%','後二日累積報酬率%','後三日累積報酬率%','後四日累積報酬率%','後五日累積報酬率%'])
industry_number = len(PreIPO.groupby('TSE 產業別').count())
save_IPO = list()
for i in range(industry_number):
    for j in range(len(payoff)):        
        positive_payoff = len(PreIPO[(PreIPO['TSE 產業別'] == industry_name[i]) & (PreIPO[payoff[j]] > 0)])
        total_number = len(PreIPO[(PreIPO['TSE 產業別'] == industry_name[i])])
        save_IPO.append(f'{round(positive_payoff/total_number*100,2)}')
x = np.array(save_IPO)
x = x.reshape([27,5])
make_form= pd.DataFrame(x)
make_form.columns = ['上市/櫃後一日勝率%','上市/櫃後二日勝率%','上市/櫃後三日勝率%','上市/櫃後四日勝率%','上市/櫃後五日勝率%']
make_form.index = industry_name
make_form

a = industry_name.tolist()
b = make_form['上市/櫃後一日勝率%']
c = make_form['上市/櫃後二日勝率%']
d = make_form['上市/櫃後三日勝率%']
e = make_form['上市/櫃後四日勝率%']
f = make_form['上市/櫃後五日勝率%']
y = []
for i in range(len(b)):
    b[i] = float(b[i])
    c[i] = float(c[i])
    d[i] = float(d[i])
    e[i] = float(e[i])
    f[i] = float(f[i])
for i in range(27):
    y.append(round((b[i]+c[i]+d[i]+e[i]+f[i])/5,2))

plt.figure(figsize=(20,15))
plt.plot(a,b,color = 'red',marker='o', label="上市/櫃後一日勝率%")
plt.plot(a,c,color = 'green',marker='o', label="上市/櫃後二日勝率%")
plt.plot(a,d,color = 'orange',marker='o', label="上市/櫃後三日勝率%")
plt.plot(a,e,color = 'mediumblue',marker='o', label="上市/櫃後四日勝率%")
plt.plot(a,f,color = 'purple',marker='o', label="上市/櫃後五日勝率%")
plt.axhline(y=60, xmin=0, xmax=1, label='60%線')
plt.title("上市/櫃 勝率",fontsize=30, x=0.5, y=1.03)
plt.xticks(fontsize=15)
plt.yticks(fontsize=20)
plt.xlabel("產業", fontsize=30, labelpad = 20)
plt.ylabel("勝率%", fontsize=30, labelpad = 20)
plt.legend(loc = "best",fontsize=20)
plt.gcf().autofmt_xdate()
plt.show()


PreIPO = PreIPO.dropna(axis=0,how='any') # 清空NA
industry_name = np.unique(PreIPO[['TSE 產業別']])
payoff = np.array(['後一日累積報酬率%','後二日累積報酬率%','後三日累積報酬率%','後四日累積報酬率%','後五日累積報酬率%'])
industry_number = len(PreIPO.groupby('TSE 產業別').count())
save_IPO = list()
for i in range(industry_number):
    for j in range(len(payoff)):        
        industry_payoff = PreIPO[payoff[j]][PreIPO['TSE 產業別']==industry_name[i]].mean()
        save_IPO.append(f'{round(industry_payoff*100,2)}')
x = np.array(save_IPO)
x = x.reshape([27,5])

make_form2= pd.DataFrame(x)
make_form2.columns = ['後一日累積報酬率%','後二日累積報酬率%','後三日累積報酬率%','後四日累積報酬率%','後五日累積報酬率%']
make_form2.index = industry_name

#=============================繪圖=================================

a = industry_name.tolist()
b = make_form2['後一日累積報酬率%']
c = make_form2['後二日累積報酬率%']
d = make_form2['後三日累積報酬率%']
e = make_form2['後四日累積報酬率%']
f = make_form2['後五日累積報酬率%']
for i in range(len(b)):
    b[i] = float(b[i])
    c[i] = float(c[i])
    d[i] = float(d[i])
    e[i] = float(e[i])
    f[i] = float(f[i])
y = []
for i in range(27):
    y.append(round((b[i]+c[i]+d[i]+e[i]+f[i])/5,2))
    

plt.figure(figsize=(23,13))
plt.plot(a,b,color = 'red',marker='o', label="後一日累積報酬率%")
plt.plot(a,c,color = 'green',marker='o', label="後二日累積報酬率%")
plt.plot(a,d,color = 'orange',marker='o', label="後三日累積報酬率%")
plt.plot(a,e,color = 'mediumblue',marker='o', label="後四日累積報酬率%")
plt.plot(a,f,color = 'purple',marker='o', label="後五日累積報酬率%")
plt.axhline(y=10, xmin=0, xmax=1, label='10%線')
plt.title("上市/櫃 報酬率",fontsize=30, x=0.5, y=1.03)
plt.xticks(fontsize=15)
plt.yticks(fontsize=20)
plt.xlabel("產業", fontsize=30, labelpad = 20)
plt.ylabel("報酬率%", fontsize=30, labelpad = 20)
plt.legend(loc = "best",fontsize=20)
plt.gcf().autofmt_xdate()
plt.show()

























