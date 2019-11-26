# ### Video 4.1 - Using the simple bar graph 

# In[260]:


import matplotlib.pyplot as plt
plt.bar(["Wife","Husband","Unmarried"], [302,289,567])
plt.show()


# In[261]:


distribution = data["relationship"].value_counts()
distribution


# In[262]:


import matplotlib.pyplot as plt

plt.bar(distribution.index, distribution.values)
plt.title('Relationship')

plt.show()


# ### Video 4.2 - Exploring Histogram

# In[263]:


plt.hist(data["age"].values, bins=20)
plt.title('Age')
plt.show()


# ### Video 4.3 - Working with boxplots

# In[264]:


plt.boxplot(data['age'].values)
plt.show()


# In[265]:


plt.boxplot(data['age'].values, vert=False)
plt.show()

plt.hist(data['age'])
plt.show()


# In[266]:


ages_lt50k = data.loc[data['income'] == '<=50K', "age"]
ages_mt50k = data.loc[data['income'] == '>50K', "age"]

plt.boxplot([ages_lt50k.values, ages_mt50k.values], labels=['<=50K', '>50K'])

plt.xlabel("income")
plt.ylabel("age")
plt.title('Is there a relation between Income and Age ?')
plt.show()


# ### Video 4.4 - Detecting correlations with scatterplots

# In[267]:


plt.scatter([20, 30, 10, 25], [1, 1.5, 2, 1.6])
plt.show()


# In[268]:


plt.scatter(ozone_data['temp12'].values, ozone_data['temp15'].values)

plt.xlabel("temp12")
plt.ylabel("temp15")
plt.title("Relationship between Temp12 and Temp15")
plt.show()


# In[269]:


plt.scatter(ozone_data['wind15'].values, ozone_data['prev_maxO3'].values)

plt.xlabel("wind15")
plt.ylabel("prev_maxO3")
plt.title("Relationship between wind15 and prev_maxO3")
plt.show()


# ### Video 4.5 - Extending Matplotlib’s possibilities thanks to Seaborn

# In[270]:


import seaborn as sns
sns.set()

plt.scatter(ozone_data['wind15'].values, ozone_data['prev_maxO3'].values)

plt.xlabel("wind15")
plt.ylabel("prev_maxO3")
plt.title("Relationship between wind15 and prev_maxO3")
plt.show()


# In[271]:


sns.jointplot("temp12", "temp15", ozone_data, kind="reg")
plt.show()


# In[272]:


sns.pairplot(ozone_data)
plt.show()


# ### Video 4.6 - Dealing with several plots

# In[273]:


fig, [ax1, ax2] = plt.subplots(2)

ax1.set_title("title 1")
ax2.set_title("title 2")

ax1.xaxis.set_view_interval(-10,10) # horizontal axis
ax1.yaxis.set_view_interval(0,100) # vertical axis
ax2.xaxis.set_view_interval(-2000,2000) # horizontal axis
ax2.yaxis.set_view_interval(0,3000) # vertical axis

fig.suptitle("General title")

plt.show()


# In[274]:


fig, axes = plt.subplots(2,3)

axes[1,2].hist(data["age"])

plt.show()


# In[275]:


fig, axes = plt.subplots(2,3)
print("Shape of axes : ", axes.shape)
print("axes :")
print(axes)

axes[1,2].hist(data["age"])
plt.show()
