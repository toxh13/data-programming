#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
data= pd.read_excel('D:GC/05_data1.xlsx')
data


# In[2]:


data.isnull().sum()


# In[3]:


data.columns


# In[10]:


newdata=data.loc[:,['gender','height','weight','blood_sugar']]
newdata


# In[18]:


newdata.loc[data['gender']==1,['gender']]='M'
newdata.loc[data['gender']==2,['gender']]='F'
newdata.loc[data['blood_sugar']>=120,['blood_sugar']]='over'
newdata.loc[data['blood_sugar']<120,['blood_sugar']]='under'
weight=data['weight']
height=data['height']/100
bmi=weight/(height**2)


# In[36]:


newdata['bmi'] = np.where(bmi >= 25, 'Fat', np.where((bmi >= 23) & (bmi < 25), 'overweight', 'normal'))

newdata


# In[20]:


blood_sugar=newdata.groupby(['gender','blood_sugar'])['blood_sugar'].count()
blood_sugar=blood_sugar.to_frame(name='count')
blood_sugar=blood_sugar.reset_index()

blood_sugar


# In[37]:


bmi_count=newdata.groupby(['gender','bmi'])['bmi'].count()
bmi_count=bmi_count.to_frame(name='count')
bmi_count=bmi_count.reset_index()

bmi_count


# In[32]:


import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))

plt.bar(blood_sugar['gender'] + ' - ' + blood_sugar['blood_sugar'], blood_sugar['count'])
plt.xlabel('Gender - Blood Sugar')
plt.ylabel('Count')
plt.title('Blood Sugar by Gender')
plt.show()


# In[38]:


plt.figure(figsize=(10, 6))

plt.bar(bmi_count['gender'] + ' - ' + bmi_count['bmi'], bmi_count['count'])
plt.xlabel('Gender - bmi_count')
plt.ylabel('Count')
plt.title('bmi_count by Gender')
plt.show()


# In[ ]:





# In[ ]:




