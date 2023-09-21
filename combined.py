#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df1=pd.read_csv('D:/GC/2014.csv',encoding='euc-kr')

df1


# In[7]:


import pandas as pd
df2=pd.read_csv('D:/GC/2015.csv',encoding='euc-kr')

df2


# In[6]:


import pandas as pd
df3=pd.read_csv('D:/GC/2016.csv',encoding='euc-kr')

df3


# In[10]:


import pandas as pd

combine_df = pd.contact([df1,df2],axis=0)


# In[15]:


combined_df = pd.concat([df1, df2,df3], axis=0)

combined_df


# In[16]:


w=combined_df['사고(건)']==combined_df['사고(건)'].max()
combined_df[w]


# In[ ]:





# In[ ]:




