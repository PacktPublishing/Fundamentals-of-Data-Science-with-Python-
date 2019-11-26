# In[305]:


import statsmodels.formula.api as smf


# In[306]:


m = smf.ols("maxO3 ~ temp15", ozone_data).fit()
m.summary()


# In[340]:


temp15 = 70
maxO3 = -104.3993 + 2.6771*temp15
maxO3


# In[341]:


m = smf.ols("age ~ income", data).fit()
m.summary()


# In[352]:


data["income_num"] = [0 if i == "<=50K" else 1 for i in data["income"]]
#data[["income","income_num"]]


# In[353]:


m = smf.logit("income_num ~ age", data).fit()
m.summary()


# In[313]:


m.predict({"age":-200})


# In[314]:


m.predict({"age":10})


# In[315]:


m.predict({"age":50})


# In[354]:


m.predict({"age":200})


# In[355]:


m.pred_table()
