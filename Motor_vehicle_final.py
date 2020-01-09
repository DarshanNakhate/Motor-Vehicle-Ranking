#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


df=pd.DataFrame()
df=pd.read_csv('Motor_Vehicle.csv')


# In[41]:


# df['Vehicle Make'].nunique()


# In[42]:


# df['Contributing Factor 1'].nunique()


# In[108]:


# df.isnull


# In[111]:


dfnew = pd.DataFrame(data=df,columns=['Year','Vehicle Make','Contributing Factor 1'])


# In[119]:


# dfnew.isnull().any()


# In[120]:





# In[123]:


dfnew = dfnew.dropna(axis=0, subset=['Vehicle Make'])


# In[128]:


dfnew = dfnew.dropna(axis=0, subset=['Contributing Factor 1'])


# In[134]:


dfnew = dfnew.groupby(['Year', 'Vehicle Make', 'Contributing Factor 1']).size().reset_index(name='counts')


# In[151]:


dftotal_count=dfnew.groupby(['Year', 'Vehicle Make'],as_index=False).sum()


# In[156]:


df_vehicle_count=dfnew[dfnew['Contributing Factor 1']=='VEHICLE']


# In[158]:


df_vehicle_count.rename(columns={'counts':'vehicle_count'},inplace=True)


# In[153]:


dftotal_count.rename(columns={'counts':'total_count'},inplace=True)


# In[160]:


df_safety_indicator = pd.merge(df_vehicle_count,dftotal_count,on=['Year','Vehicle Make'])


# In[162]:


df_safety_indicator=df_safety_indicator.drop('Contributing Factor 1',1)


# In[179]:


df_safety_indicator['car_safety_indicator'] = round(df_safety_indicator['vehicle_count']/df_safety_indicator['total_count']*100,2)


# In[187]:


# df_safety_indicator=df_safety_indicator.drop('VehicleSafetyRank',1)


# In[188]:


df_safety_indicator_2014 = df_safety_indicator[df_safety_indicator['Year']==2014]


# In[196]:


df_safety_indicator_2014=df_safety_indicator_2014.sort_values(by=['car_safety_indicator'])


# In[201]:


df_safety_indicator_2014.reset_index(inplace=True)


# In[205]:


df_safety_indicator_2014_final = df_safety_indicator_2014.head(5)


# In[207]:


# df_safety_indicator_2014_final['Ranking'] = [i for i in range(1,6)]


# In[225]:


df_safety_indicator_2014_final['Ranking'] = df_safety_indicator_2014_final.index.values+1


# In[ ]:





# In[ ]:




