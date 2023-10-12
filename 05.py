#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
index= np.arange(7)

data= pd.read_excel('D:GC/04_data1.xlsx',index_col='area')

plt.figure(figsize=(10,4))

data6 = data.loc['Seoul':'Ulsan','2017_common':'2020_common']
for year in range(2017,2021):
    year = str(year)+'_common'
    chartdata=data6[year]
    plt.barh(index, chartdata, label=year)
    
    plt.xlim(120,310)
    plt.ylabel('Area')
    plt.xlabel('Micrometer')
    plt.yticks(index,['Seoul','Busan','Daegu','Incheon','Guangju','Daejeon','Ulsan'])
    plt.title('2017~2020 Fine Dust(pm10) Common Group Barh Graph')
    plt.legend()
    plt.show()


# In[9]:


import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv('D:GC/titanic.csv')

data


# In[13]:


Fare = data['Fare']
Pclass = data['Pclass']

plt.figure(figsize=(10,4))
plt.scatter(Pclass,Fare,color='r')

plt.xlabel('Pclass')
plt.ylabel('Fare')
plt.title('Fare & Pclass')
plt.grid()
plt.show()


# In[18]:


newdata=data.copy().head(100)
newdata


# In[19]:





# In[27]:


plt.figure(figsize=(10, 6))
plt.hist(data['Fare'], bins=8, color='skyblue')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.title('Fare')
plt.grid()
plt.show()


# In[29]:


avg=data['Age'].mean()
data['Age']=data['Age'].fillna(avg)
data.isnull().sum()


# In[30]:


newdata=data.copy().head(100)
newdata


# In[45]:


plt.figure(figsize=(10,6))

plt.hist(newdata['Fare'],bins=5,alpha=0.5,label='Fare')
plt.hist(newdata['Age'],bins=5,alpha=0.5,label='Age')

plt.xlabel('amount')
plt.ylabel('frequency')
plt.title('Age&Fare')
plt.legend()
plt.grid()
plt.show()


# In[60]:


Age=newdata['Age']

plt.figure(figsize=(8,5))
plt.boxplot([Age,Fare], labels=['Age','Fare'],vert=False)

plt.xlabel('Age')
plt.ylabel('Value')
plt.title('Box')
plt.show()


# In[59]:


import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_excel('D:/GC/04_data1.xlsx',index_col='area')
data


# In[74]:


data.isnull().sum()


# In[69]:


avg=data['2015_good'].mean()
data['2015_good']=data['2015_good'].fillna(avg)
data.isnull().sum()
avg=data['2015_common'].mean()
data['2015_common']=data['2015_common'].fillna(avg)
data.isnull().sum()
avg=data['2015_bad'].mean()
data['2015_bad']=data['2015_bad'].fillna(avg)
data.isnull().sum()
data


# In[80]:


data.columns


# In[81]:


plt.figure(figsize=(8,5))
plt.boxplot([data['2015_good'],data['2015_common'],data['2015_bad']])

plt.xlabel('width')
plt.ylabel('value')
plt.title('dust')
plt.show()


# In[83]:


import seaborn as sns

data= pd.read_excel('D:GC/05_data1.xlsx')
data


# In[84]:


data.isnull().sum()


# In[85]:


data.columns


# In[87]:


data6 = data.loc[:,['gender','height','weight','waist','drinking','smoking']]

data6.loc[data6['gender']==1,['gender']]='M'
data6.loc[data6['gender']==2,['gender']]='F'
data6.loc[data6['drinking']==0,['drinking']]='Non-drinking'
data6.loc[data6['drinking']==1,['drinking']]='Drinking'
data6.loc[data6['smoking']==1,['smoking']]='Non-smoking'
data6.loc[data6['smoking']==2,['smoking']]='Quit-smoking'
data6.loc[data6['smoking']==3,['smoking']]='Smoking'
data6


# In[90]:


drinking = data6.groupby(['gender','drinking'])['drinking'].count()
smoking = data6.groupby(['gender','smoking'])['smoking'].count()
drinking = drinking.to_frame(name='count')
smoking = smoking.to_frame(name='count')
drinking = drinking.reset_index()
smoking = smoking.reset_index()

drinking


# In[91]:


smoking


# In[93]:


fig = plt.figure(figsize=(12,10))
fig.subtitle('2020 Health Check Drinking & Smoking Type Bar Graph',fontweight = 'bold')
index1 = np.arange(4)
index2 = np.arange(6)

fig.add_subplot(2,1,1)

plt.bar(index1,drinking['count'])
plt.title('Drinking Type')
plt.ylabel('Count')
plt.xticks(index1, ['Non-drinking(M)','Drinking(M)','Non-drinking(F)','Drinking(F)'])

fig.add_subplot(2,1,2)
plt.bar(index2, smoking['count'])
plt.title('Smoking Type')
plt.ylabel('Count')
plt.xticks(index2, ['Non-smoking(M)','Quit-smoking(M)','Smoking(M),''Non-smoking(F)','Quit-smoking(F)','Smoking(F),'])
plt.show()


# In[107]:


newdata = data.loc[:,['gender','age_code','height','weight','blood_sugar']]
newdata


# In[110]:


newdata.loc[data6['gender']==1,['gender']]='M'
newdata.loc[data6['gender']==2,['gender']]='F'
newdata.loc[data6['blood_sugar']>=120,['blood_sugar']]='Over'
newdata.loc[data6['blood_sugar']<120,['blood_sugar']]='Under'
newdata


# In[104]:


blood_sugar=newdata.groupby(['gender','blood_sugar'])['blood_sugar'].count()
blood_sugar=blood_sugar.to_frame(name='count')
blood_sugar=blood_sugar.reset_index()

blood_sugar


# In[ ]:




