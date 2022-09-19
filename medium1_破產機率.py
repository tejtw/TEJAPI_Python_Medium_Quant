#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import tejapi
import statsmodels.formula.api as smf
tejapi.ApiConfig.api_key = "maQNDP8Vb5bBB8b55kCkR2TC6s65Eg"
tejapi.ApiConfig.api_base="http://10.10.10.66"
tejapi.ApiConfig.ignoretz = True


# In[3]:


df1 = tejapi.get('TWN/ACRQMTAB', #從TEJ api撈取所需要的資料
                chinese_column_name = True,
                paginate = True,
#                 mdate = {'gt':'2018-01-01'},
                opts={'columns':['coid','mdate','xcdt']})


# In[4]:


df1


# 先確認狀況有幾種類別

# In[5]:


df1['狀況'].unique()


# 將上市前股票排除

# In[6]:


df2 = df1[df1['狀況'] != '上市前']


# In[7]:


df2


# 將全交下市及下市 股票設為1 其餘為0

# In[8]:


df2['狀況'] = df2[['狀況']].applymap(lambda x:1 if x =='全交下市' or x =='下市'  else 0)


# 抓變數會用到的財報資料

# In[12]:


a1 = tejapi.get('TWN/AIFIN', #從TEJ api撈取所需要的資料
                chinese_column_name = True,
                paginate = True,
                mdate = {'gt':'2008-01-01', 'lt':'2011-01-01'},
                acc_code = ['R678', '0010','2341','2402','MV','1000', 'R607','R11V', 'R505'])


# In[14]:


a2 = tejapi.get('TWN/AIFIN', #從TEJ api撈取所需要的資料
                chinese_column_name = True,
                paginate = True,
                mdate = {'gt':'2011-01-01', 'lt':'2014-01-01'},
                acc_code = ['R678', '0010','2341','2402','MV','1000', 'R607','R11V', 'R505'])


# In[25]:


a3 = tejapi.get('TWN/AIFIN', #從TEJ api撈取所需要的資料
                chinese_column_name = True,
                paginate = True,
                mdate = {'gt':'2014-01-01', 'lt':'2017-01-01'},
                acc_code = ['R678', '0010','2341','2402','MV','1000', 'R607','R11V', 'R505'])


# In[26]:


a4 = tejapi.get('TWN/AIFIN', #從TEJ api撈取所需要的資料
                chinese_column_name = True,
                paginate = True,
                mdate = {'gt':'2017-01-01', 'lt':'2020-01-01'},
                acc_code = ['R678', '0010','2341','2402','MV','1000', 'R607','R11V', 'R505'])


# In[27]:


a5 = tejapi.get('TWN/AIFIN', #從TEJ api撈取所需要的資料
                chinese_column_name = True,
                paginate = True,
                mdate = {'gt':'2020-01-01'},
                acc_code = ['R678', '0010','2341','2402','MV','1000', 'R607','R11V', 'R505'])


# In[37]:


acc = pd.concat([a1,a2,a3,a4,a5])


# In[39]:


acc1 = acc.pivot_table(values='數值', index=['公司','年/月'], columns='會計科目') #用pivot table將會計科目放到columns上


# In[40]:


acc1


# In[41]:


acc1['X1'] = (acc1['R678']/acc1['0010'])*100
acc1['X2'] = (acc1['2341']/acc1['0010'])*100
acc1['X3'] = (acc1['2402']/acc1['0010'])*100
acc1['X4'] = (acc1['MV']/acc1['1000'])*100
acc1 = acc1.rename(columns = {'R607':'X5', 'R11V':'X6', 'R505':'X7'})
acc2 = acc1[['X1','X2','X3','X4','X5','X6','X7']]


# In[42]:


df3 = df2.merge(acc2, on=['公司','年/月']) #合併應變數跟自變數


# In[43]:


df3 = df3.rename(columns = {'狀況':'Y'})


# In[44]:


df3


# linear probility model

# In[45]:


result_ols = smf.ols('Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X7', data=df3).fit()
print(result_ols.summary())


# probit model

# In[72]:


result_probit = smf.probit('Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X7 ', data=df3).fit()
print(result_probit.summary())


# logit model

# In[71]:


result_Logit = smf.logit('Y ~ X1 + X2 + X3 + X4 + X5 + X6 + X7  ', data=df3).fit()
print(result_Logit.summary())


# 台積電

# In[50]:


TSMC = df3[df3['公司']=='2330']


# In[51]:


a = TSMC.iloc[-1:,:] #取得最新一筆資料


# In[52]:


result_ols.predict(a) #linear probility model


# In[53]:


result_probit.predict(a) #probit model


# In[54]:


result_Logit.predict(a) #logit model


# 英瑞ky

# In[55]:


Enterex = df3[df3['公司']=='1592']


# In[56]:


b = Enterex.iloc[-1:,:]


# In[57]:


result_ols.predict(b) #linear probility model


# In[58]:


result_probit.predict(b) #probit model


# In[59]:


result_Logit.predict(b) #logit model


# 華映

# In[60]:


CPT = df3[df3['公司']=='2475']


# In[61]:


d = CPT.iloc[-1:,:]


# In[62]:


result_ols.predict(d) #linear probility model


# In[63]:


result_probit.predict(d) #probit model


# In[64]:


result_Logit.predict(d) #logit model


# 和進

# In[94]:


hold = df3[df3['公司']=='3191']


# In[95]:


e = hold.iloc[-1:,:]


# In[96]:


result_ols.predict(e) #linear probility model


# In[97]:


result_probit.predict(e) #probit model


# In[98]:


result_Logit.predict(e) #logit model


# In[ ]:




