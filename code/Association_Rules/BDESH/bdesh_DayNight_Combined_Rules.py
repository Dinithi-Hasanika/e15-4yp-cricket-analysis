#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[2]:


match_data = pd.read_csv('bdesh.csv')


# In[3]:


match_data.head()


# In[4]:


del match_data["Home"]
del match_data["Bat"]
del match_data["Toss"]
del match_data["Opposition"]


# In[5]:


match_data


# In[6]:


match_data['Day_Night'].unique()


# In[7]:


player_combo = [] #list of lists match players and result
for i in range(0, 78):
    rowItem = []
    for j in range(0, 13):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[8]:


te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[9]:


match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
match_sup


# In[10]:


rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[11]:


rules


# In[12]:


won_rules = rules[(rules['consequents'] == {"won"})]


# In[13]:


won_rules


# In[14]:


won_rules.values[0,:]


# In[15]:


col_names = ["antecedents","consequents","antecedent support","consequent support","support","confidence","lift","leverage","conviction"]
DN_won_rules = pd.DataFrame(columns = col_names)


# In[16]:


i = 0
for x in won_rules['antecedents']:
    for y in x:
        if y == 'DN':
            #print(won_rules.values[i,0])
            DN_won_rules = DN_won_rules.append({'antecedents':won_rules.values[i,0],"consequents":won_rules.values[i,1],"antecedent support":won_rules.values[i,2],"consequent support":won_rules.values[i,3],"support":won_rules.values[i,4],"confidence":won_rules.values[i,5],"lift":won_rules.values[i,6],"leverage":won_rules.values[i,7],"conviction":won_rules.values[i,8]},ignore_index=True)
    i = i + 1


# In[17]:


DN_won_rules


# In[18]:


DN_won_rules.to_csv('DN_won_rules.csv')


# In[19]:


col_names = ["antecedents","consequents","antecedent support","consequent support","support","confidence","lift","leverage","conviction"]
D_won_rules = pd.DataFrame(columns = col_names)


# In[20]:


i = 0
for x in won_rules['antecedents']:
    for y in x:
        if y == 'D':
            #print(won_rules.values[i,0])
            D_won_rules = D_won_rules.append({'antecedents':won_rules.values[i,0],"consequents":won_rules.values[i,1],"antecedent support":won_rules.values[i,2],"consequent support":won_rules.values[i,3],"support":won_rules.values[i,4],"confidence":won_rules.values[i,5],"lift":won_rules.values[i,6],"leverage":won_rules.values[i,7],"conviction":won_rules.values[i,8]},ignore_index=True)
    i = i + 1


# In[21]:


D_won_rules#no rules


# In[22]:


D_won_rules.to_csv('D_won_rules.csv')


# In[ ]:




