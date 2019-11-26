# ### Video 3.3 - Loading the datasets into your program

# In[233]:


import pandas as pd


# In[234]:


data = pd.read_csv("adult.csv", na_values="?")


# In[235]:


data.head()


# In[236]:


data = data.rename(columns = {
    "education.num" : "education_num",
    "marital.status" : "marital_status",
    "capital.gain" : "capital_gain",
    "capital.loss" : "capital_loss",
    "hours.per.week" : "hours_per_week",
    "native.country" : "native_country"
})
data.columns


# In[237]:


ozone_data = pd.read_csv("ozone.csv", sep=";", decimal=",")
ozone_data.head()


# In[238]:


ozone_data = ozone_data.rename(columns = {
    'obs' : 'id',
    'T9' : 'temp9',
    'T12' : 'temp12',
    'T15' : 'temp15',
    'Ne9' : 'cloud9',
    'Ne12' : 'cloud12',
    'Ne15' : 'cloud15',
    'Vx9' : 'wind9',
    'Vx12' : 'wind12', 
    'Vx15' : 'wind15', 
    'maxO3v' : 'prev_maxO3',
    'vent' : 'wind',
    'pluie' : 'rain'                                          
})
ozone_data.head()


# ### Video 3.4 – Getting a global overview of the data 

# In[239]:


data.head()


# In[240]:


#data['education'].value_counts()


# In[241]:


data['workclass'].value_counts()


# In[242]:


data['marital_status'].value_counts()


# In[243]:


#data.occupation.value_counts()


# In[244]:


data.relationship.value_counts()


# In[245]:


data.sex.value_counts()


# In[246]:


#data.native_country.value_counts()


# In[247]:


data.income.value_counts()


# In[248]:


data.head()


# In[249]:


data.describe()


# ### Video 3.5 - Finding missing values in Data

# In[250]:


data.info()


# 
# 

# ### Video 3.6 - Cleaning the data for use

# In[251]:


data = data.drop(columns= ["race"])


# In[252]:


data.head()


# In[253]:


data[(data["capital_gain"] > 0) & (data["capital_loss"] > 0)]


# In[254]:


data["capital"] = data["capital_gain"] - data["capital_loss"]


# In[255]:


del data["capital_gain"], data["capital_loss"]


# In[256]:


for column in ['temp9','temp12','temp15']:
    ozone_data[column] = (ozone_data[column] * 9/5) + 32

ozone_data.head()


# In[257]:


#ozone_data = ozone_data.replace({
#    'Nord': "north",
#    'Est': "east",
#    'Ouest': "west",
#    "Sud": "south"
#})

ozone_data = ozone_data.replace({
    'Sec': "dry",
    'Pluie': "rain",
})


# In[258]:


values = []

for word in ozone_data['wind'].values :
    if word == 'Nord':
        translation = 'north'
    elif word == 'Est':
        translation = 'east'
    elif word == 'Ouest':
        translation = "west"
    elif word == 'Sud':
        translation = 'south'
    else :
        translation = word
    
    values.append(translation)
    
#values


# In[259]:


ozone_data['wind'] = values
ozone_data.head()


