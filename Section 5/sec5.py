# In[276]:


#data['age']


# In[277]:


#ozone_data['temp12']


# In[278]:


#data['marital_status']


# In[279]:


data[['education','education_num']].drop_duplicates().sort_values("education_num")


# In[280]:


data['hours_per_week'].hist()


# In[281]:


data['hours_per_week'].describe()


# In[282]:


data['marital_status'].value_counts()


# In[283]:


data['marital_status'].value_counts().plot(kind='bar')


# In[284]:


data['education_num'].value_counts().sort_index().plot(kind='bar')


# In[285]:


data['marital_status'].value_counts().plot(kind='pie')


# In[286]:


data['age'].mean()


# In[287]:


data['age'].sum() / len(data)


# In[288]:


data['age'].median()


# In[289]:


data['age'].var()


# In[290]:


data['age'].std()


# In[291]:


lt50k = data[data['income'] == '<=50K']
mt50k = data[data['income'] == '>50K']


# In[292]:


print(lt50k["age"].mean())
print(mt50k["age"].mean())


# In[293]:


print(lt50k["hours_per_week"].mean())
print(mt50k["hours_per_week"].mean())


# In[294]:


print(lt50k["age"].std())
print(mt50k["age"].std())


# In[295]:


print(lt50k["hours_per_week"].std())
print(mt50k["hours_per_week"].std())


# In[296]:


fig, axes = plt.subplots(2,1,figsize=(5,6))

axes[0].hist(ages_lt50k)
axes[0].set_title("less than 50k")
axes[1].hist(ages_mt50k)
axes[1].set_title("more than 50k")

plt.show()


# In[297]:


fig, axes = plt.subplots(1,2, figsize=(10,2))

axes[0].hist(ozone_data["temp15"], bins=9)
axes[0].set_title("temp15")
axes[1].hist(ozone_data["maxO3"], bins=9)
axes[1].set_title("maxO3")

plt.show()


# In[298]:


sns.jointplot("temp15","maxO3", ozone_data)


# In[299]:


import scipy.stats as st

st.pearsonr(ozone_data["temp15"], ozone_data['maxO3'])


# In[300]:


sns.jointplot("temp12","temp15", ozone_data)


# In[301]:


st.pearsonr(ozone_data["temp12"], ozone_data['temp15'])


# In[302]:


from scipy import stats as st

mu_0 = data.age.mean()
print(mu_0)

subsample = data.loc[data.income=='>50K', 'age']

st.ttest_1samp(subsample, mu_0)


# In[303]:


contingency = pd.crosstab(data['education'], data['income'])
contingency


# In[304]:


chi2, pvalue, dof, ex = st.chi2_contingency(contingency)
pvalue
