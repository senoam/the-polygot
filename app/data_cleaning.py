#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[32]:


data = pd.read_excel('data.xlsx')
data = data.tail(72)
data = data.head(30)
data.reset_index(inplace=True, drop=True)


# In[33]:


data = data.drop(['Jam', 'Tanggal Jam', 'Belum Ada Data', 'Tanpa Gejala', 'Total Pasien', 'Masih Perawatan', 'Bergejala',
                  'Self Isolation'],axis=1)
data = data.rename(columns={'Tanggal': 'Date', 'Meninggal': 'Deaths', 'Sembuh': 'Recoveries', 
                            'Positif Harian': 'Daily Positive Cases', 'Sembuh Harian': 'Daily Recoveries',
                            'Positif Aktif': 'Active Cases'})


# In[35]:


data
data.to_csv('df.csv')

