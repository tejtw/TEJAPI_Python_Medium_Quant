#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install tejapi


# In[60]:


import tejapi
import pandas as pd
import numpy as np

tejapi.ApiConfig.api_key = "Your Key"
tejapi.ApiConfig.ignoretz = True
#-----------------------------------------------------------------
mdate = {'gte':'2022-07-13', 'lte':'2022-11-08'}#國安基金進場期間
coid = "Y9999"#大盤代號
data = tejapi.get('TWN/APRCD1',
                          coid = coid,
                          mdate = mdate,
                          paginate=True)
df = pd.DataFrame({"日期":data["mdate"],"大盤":data["close_adj"]})


# In[18]:





# In[61]:


coid = ["1101","1301","1303","1326","2308","2317","2330","2382","2880","2886"]

for i in range(0,len(coid)):
    
    stock = tejapi.get('TWN/APRCD1',
                              coid = coid[i],
                              mdate = mdate,
                              paginate=True)
    df1 = pd.DataFrame({"日期":stock["mdate"],str(coid[i]):stock["close_adj"]})
    #以日期做合併
    df = pd.merge(df,df1,left_on="日期",right_on="日期",how="outer")
df


# In[ ]:





# In[62]:


#算個別個股績效
#(每天股價-國安基金進場第一天股價)/國安基金進場第一天股價
df2 = (df.iloc[:, 1:] - df.iloc[0, 1:].values.squeeze()).div(df.iloc[:, 1:])
#四捨五入
df2 = df2.astype(float).round(3)
df_result = pd.DataFrame({"日期":df["日期"]})

df_result = pd.merge(df_result,df2,left_on=None,right_on=None,left_index=True, 
                     right_index=True)
df_result


# In[63]:


df = df_result

import matplotlib.pyplot as plt

df.set_index(pd.to_datetime(df["日期"], format="%Y-%m-%d"), inplace=True)
del(df["日期"])

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

#畫圖
fig, ax1 = plt.subplots(figsize=(20, 10))
plt.plot(df.index,df[coid],lw=1.5,label=coid)
plt.plot(df.index,df["大盤"],lw=5,label="大盤",color="blue")
plt.xlabel("日期",fontsize=20)
plt.ylabel("累積報酬",fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.title("第八次國安基金熱門標的股價表現與大盤比較",fontsize=30)
plt.legend(bbox_to_anchor=(1, 1.0))
plt.show()


# In[ ]:


#=============================================================================================================


# In[51]:


import tejapi
import pandas as pd

tejapi.ApiConfig.api_key = "Your Key"
tejapi.ApiConfig.ignoretz = True
#-----------------------------------------------------------------------------
#第八次國安基金進場
mdate = {'gte':'2020-03-20', 'lte':'2020-10-12'}
#八大券商
bank = ["000102 合庫證券","000538 第一金證","000104 臺銀證券","2801   彰銀",
        "2834   臺企銀","5857   土銀","000930 華南永昌證券","000700 兆豐證券"]
#國安基金熱門標的
coid = ["1101","1301","1303","1326","2308","2317","2330","2382","2880","2886"]


# In[53]:


cor = []
for i in coid:
    
    #---------------------------------------------------------------------------
    #個股股價
    market = tejapi.get('TWN/AAPRCDA',
                      coid = i,
                      mdate = mdate,
                      paginate=True)
    #累積買賣超
    df = pd.DataFrame({"日期":market["mdate"],"股價":market["close_d"]})
    #---------------------------------------------------------------------------
    #個股券商買賣超
    data = tejapi.get('TWN/AMTOP1',
                      coid = i,
                      mdate = mdate,
                      paginate=True)
    #---------------------------------------------------------------------------
    for i in range(0,len(bank)):
        #選出八大券商
        broker = bank[i]
        data1 = data[data["key3"] == broker]
        
        bs_data = data1[["mdate","bs_m"]]
        bs_data = bs_data.rename(columns={"mdate": '日期',"bs_m": str(broker)})
        #算出八大券商期間累積買賣超
        df = pd.merge(df,bs_data,left_on="日期",right_on="日期",how="outer")
        df[str(broker)] = df[str(broker)].fillna(0)
        bs_m_list = list(df[str(broker)])
        agg  = []
        n = 0
        for j in range(0,len(bs_m_list)):
            n = n + bs_m_list[j] #每日淨買賣
            agg = agg + [n] # #每日加總
        df[str(broker)] = agg
    #八大券商買賣總金額    
    df_total = pd.DataFrame({"股價":market["close_d"],
                             "八大淨買賣總和":df[bank].sum(axis=1)})
    #標準化
    from sklearn.preprocessing import StandardScaler
    df_total[df_total.columns] = StandardScaler().fit_transform(df_total[df_total.columns])
    #相關性
    df_total_cor = round(df_total['股價'].corr(df_total["八大淨買賣總和"]),2)
    cor = cor + [df_total_cor]

df_cor = pd.DataFrame({"股票":coid,"相關係數":cor})
df_cor


# In[58]:


#Plot 八大行庫各家買賣超金額
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import datetime
#輸入個股代碼
coid = "2308"
#個股股價
market = tejapi.get('TWN/AAPRCDA',
                  coid = coid,
                  mdate = mdate,
                  paginate=True)

df = pd.DataFrame({"日期":market["mdate"],"股價":market["close_d"]})
#---------------------------------------------------------------------------
#個股券商買賣超
data = tejapi.get('TWN/AMTOP1',
                  coid = coid,
                  mdate = mdate,
                  paginate=True)

for i in range(0,len(bank)):
    
    broker = bank[i]
    data1 = data[data["key3"] == broker]
    
    bs_data = data1[["mdate","bs_m"]]
    bs_data = bs_data.rename(columns={"mdate": '日期',"bs_m": str(broker)})
    #累積買賣超
    df = pd.merge(df,bs_data,left_on="日期",right_on="日期",how="outer")
    df[str(broker)] = df[str(broker)].fillna(0)
    bs_m_list = list(df[str(broker)])
    agg  = []
    n = 0
    for j in range(0,len(bs_m_list)):
        n = n + bs_m_list[j] #每日淨買賣
        agg = agg + [n] # #每日更新
    df[str(broker)] = agg

df["八大淨買賣總和"] = df[bank].sum(axis=1)
df


# In[59]:


#Plot
#Index設定為日期
df.set_index(pd.to_datetime(df["日期"], format="%Y-%m-%d"), inplace=True)
del(df["日期"])

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
#畫雙軸圖
fig, ax1 = plt.subplots(figsize=(20, 10))
plt.plot(df.index,df[bank],lw=1.5,label=bank)
plt.plot(df.index,df["八大淨買賣總和"],lw=5,label="八大淨買賣總和")
plt.xlabel("日期",fontsize=20)
plt.ylabel("累積買賣超(元)",fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.title(str(coid)+" 國安基金期間八大券商累積買賣超關係圖",fontsize=30)
plt.legend(bbox_to_anchor=(-0.05, 1.0))

ax2 = ax1.twinx()
plt.plot(df.index,df["股價"],lw=5,label=str(coid)+"股價")
plt.ylabel("股價(元)",fontsize=20)
plt.yticks(fontsize=20)
plt.legend(bbox_to_anchor=(1, 1.0))
plt.show()

