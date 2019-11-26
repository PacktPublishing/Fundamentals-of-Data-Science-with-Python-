# ### Video 2.1 - Introduction to the Numpy Array

# In[119]:


group.shape


# In[120]:


group[2]


# In[121]:


group.getAllAges()


# In[122]:


group.mean()


# In[123]:


group.data


# In[124]:


persons_data = [[29, 10, 40], 
                [45, 9 , 30], 
                [34, 5 , 35],
                [38, 4 , 35]]


# In[125]:


import numpy as np

numpy_group = np.array(persons_data)
numpy_group


# In[126]:


numpy_group.shape


# In[127]:


numpy_group[2]


# In[128]:


numpy_group[:,0]


# In[129]:


numpy_group.mean(axis=0)


# In[130]:


np.array([7, 2, 9, 1, 3, 2])


# In[131]:


np.array([3, 5, 1, 7, 9, 2.43])


# In[132]:


np.array([[23, 1], [67, 3], [50, 1]])


# In[133]:


np.array([[[23,2], [3,1]], [[67,1], [4,3]], [[50,23], [2,1]]]).shape


# In[134]:


np.zeros(4)


# In[135]:


np.ones((3,6))


# In[136]:


np.full((3, 6), 23)


# In[137]:


np.random.random((3, 6))


# In[138]:


np.arange(0, 20, 4)


# In[139]:


numpy_group


# In[140]:


numpy_group[0]


# In[141]:


numpy_group[-1]


# In[142]:


numpy_group[0,2]


# In[143]:


numpy_group[0,2] = 5000
numpy_group


# In[144]:


numpy_group[0] = [30,11,5000]
numpy_group


# In[145]:


numpy_group[0:2]


# In[146]:


numpy_group[:2]


# In[147]:


numpy_group[2:]


# In[148]:


numpy_group[:]


# In[149]:


numpy_group[-3:]


# In[150]:


numpy_group[0:4:2]


# In[151]:


numpy_group[::-1]


# In[152]:


numpy_group


# In[153]:


numpy_group[0:3,1:3]


# In[154]:


numpy_group[:,2]


# In[155]:


numpy_group[0:3:2 , ::-1]


# ### Video 2.2 – Manipulating Numpy Arrays with operators and aggregation functions

# In[156]:


numpy_group


# In[157]:


numpy_group + 1


# In[158]:


numpy_group / 10


# In[159]:


numpy_group * 2


# In[160]:


numpy_group + numpy_group


# In[161]:


numpy_group - numpy_group


# In[162]:


numpy_group


# In[163]:


numpy_group > 30


# In[164]:


numpy_group == 35


# In[165]:


numpy_group


# In[166]:


(numpy_group > 30) & (numpy_group <= 35)


# In[167]:


(numpy_group <= 30) | (numpy_group > 35)


# In[168]:


~((numpy_group <= 30) | (numpy_group > 35))


# In[169]:


values = np.array([3,5,1,5])
mask = [True,False,False,True]
values[mask]


# In[170]:


values > 4


# In[171]:


values = np.array([3,5,1,5])
mask = values > 4
values[mask]


# In[172]:


values[values > 4]


# In[173]:


numpy_group[0,2] = 45
numpy_group


# In[174]:


numpy_group[:,2]


# In[175]:


numpy_group[:,2] > 32


# In[176]:


numpy_group[numpy_group[:,2] > 32]


# In[177]:


numpy_group


# In[178]:


numpy_group.sum()


# In[179]:


numpy_group.sum(axis=0)


# In[180]:


numpy_group.sum(axis=1)


# In[181]:


numpy_group.mean(axis=0)


# In[182]:


numpy_group.std(axis=0)


# In[183]:


numpy_group.max(axis=0)


# ### Video 2.3 – Making your first steps with Pandas

# In[184]:


print(group.shape)
print(group[2])
print(group.getAllAges())
print(group.mean())


# In[185]:


group.names


# In[186]:


group.columns


# In[187]:


persons_data = [[29, 10, 40], 
                [45, 9 , 30], 
                [34, 5 , 35],
                [38, 4 , 35]]

names = ['Anna', 'Bob', 'Andy', 'Lea']
columns = ['age', 'education_num', 'hours_per_week']


# In[188]:


import pandas as pd

pandas_group = pd.DataFrame(persons_data, columns = columns, index = names)

pandas_group


# In[189]:


pandas_group.columns


# In[190]:


pandas_group.index


# In[191]:


pandas_group.shape


# In[192]:


pandas_group.values


# In[193]:


pandas_group.mean()


# In[194]:


type(pandas_group.mean())


# In[195]:


s = pd.Series([98, 10, 0], index=['age','education_level','hours_per_week'])


# In[196]:


pd.DataFrame({'first_column': s, 'second_column': 2*s+1})


# In[197]:


pandas_group


# In[198]:


pandas_group["age"]


# In[199]:


pandas_group.loc["Anna", "education_num"]


# In[200]:


pandas_group.iloc[0, 1]


# In[201]:


pandas_group


# In[202]:


pandas_group.loc["Anna"]


# In[203]:


pandas_group.loc[:,"education_num"]


# In[204]:


pandas_group


# In[205]:


pandas_group.iloc[0]


# In[206]:


pandas_group.iloc[:,1]


# In[207]:


pandas_group


# In[208]:


pandas_group.iloc[2:,::-1]


# In[209]:


pandas_group.loc["Bob":"Lea","education_num":]


# In[210]:


pandas_group.loc["Bob":"Lea":2,:"education_num"]


# ### Video 2.4 – Performing common operations with Pandas

# In[211]:


pandas_group


# In[212]:


pandas_group["hours_per_week"] > 32


# In[213]:


pandas_group[pandas_group["hours_per_week"] > 32]


# In[214]:


pandas_group.loc[pandas_group["hours_per_week"] > 32, ["age","hours_per_week"]]


# In[215]:


pandas_group[["age","hours_per_week"]]


# In[216]:


pandas_group


# In[217]:


new_data = {"sex": ["Female","Male","Female","Female"], 
            "income": ["<=50K", "<=50K", ">50K", ">50K"]}

new_df = pd.DataFrame(new_data, index = ["Anna", "Bob", "Andy", "Marta"])
new_df


# In[218]:


pd.concat([pandas_group, new_df], axis=1, sort=False)


# In[219]:


new_people = [
 {'name': 'Harper', 'age': 32, 'education_num': 9, 'hours_per_week': 40},
 {'name': 'Sofia', 'age': 37, 'education_num': 8, 'hours_per_week': 29},
 {'name': 'Sophia', 'age': 44, 'education_num': 15, 'hours_per_week': 30},
 {'name': 'John', 'age': 33, 'education_num': 9, 'hours_per_week': 20},
 {'name': 'Thomas', 'age': 33, 'education_num': 10, 'hours_per_week': 40},
 {'name': 'David', 'age': 26, 'education_num': 8, 'hours_per_week': 35},
 {'name': 'Mark', 'age': 34, 'education_num': 7, 'hours_per_week': 40},
 {'name': 'James', 'age': 44, 'education_num': 1, 'hours_per_week': 40},
 {'name': 'Robert', 'age': 40, 'education_num': 2, 'hours_per_week': 30},
 {'name': 'Ella', 'age': 30, 'education_num': 1, 'hours_per_week': 40},
 {'name': 'William', 'age': 74, 'education_num': 3, 'hours_per_week': 30},
 {'name': 'Isabella', 'age': 39, 'education_num': 14, 'hours_per_week': 34},
 {'name': 'Amelia', 'age': 36, 'education_num': 11, 'hours_per_week': 30},
 {'name': 'Aria', 'age': 45, 'education_num': 4, 'hours_per_week': 27},
 {'name': 'Mila', 'age': 77, 'education_num': 3, 'hours_per_week': 25},
 {'name': 'Joseph', 'age': 78, 'education_num': 7, 'hours_per_week': 35},
 {'name': 'Daniel', 'age': 36, 'education_num': 1, 'hours_per_week': 40},
 {'name': 'Evelyn', 'age': 40, 'education_num': 4, 'hours_per_week': 35},
 {'name': 'Abigail', 'age': 37, 'education_num': 9, 'hours_per_week': 30},
 {'name': 'Emily', 'age': 35, 'education_num': 8, 'hours_per_week': 30},
 {'name': 'Charles', 'age': 79, 'education_num': 5, 'hours_per_week': 35},
 {'name': 'Michael', 'age': 37, 'education_num': 2, 'hours_per_week': 35},
 {'name': 'Avery', 'age': 41, 'education_num': 9, 'hours_per_week': 35},
 {'name': 'Paul', 'age': 38, 'education_num': 9, 'hours_per_week': 35},
 {'name': 'Camila', 'age': 31, 'education_num': 4, 'hours_per_week': 27},
 {'name': 'Mia', 'age': 56, 'education_num': 13, 'hours_per_week': 35},
 {'name': 'Elizabeth', 'age': 28, 'education_num': 16, 'hours_per_week': 35},
 {'name': 'Charlotte', 'age': 33, 'education_num': 16, 'hours_per_week': 35},
 {'name': 'Scarlett', 'age': 79, 'education_num': 2, 'hours_per_week': 35},
 {'name': 'Richard', 'age': 36, 'education_num': 16, 'hours_per_week': 40}
]
new_people_df = pd.DataFrame(new_people)
new_people_df.head()


# In[220]:


new_people_df.index = new_people_df["name"]
new_people_df = new_people_df.drop(columns=["name"])
new_people_df.head()


# In[221]:


pandas_group


# In[222]:


pandas_group = pandas_group.append(new_people_df)
#pandas_group


# In[223]:


education = {
    1: 'Preschool',
    2: '1st-4th',
    3: '5th-6th',
    4: '7th-8th',
    5: '9th',
    6: '10th',
    7: '11th',
    8: '12th',
    9: 'HS-grad',
    10: 'Some-college',
    11: 'Assoc-voc',
    12: 'Assoc-acdm',
    13: 'Bachelors',
    14: 'Masters',
    15: 'Prof-school',
    16: 'Doctorate'
}

educ_series = pd.Series(education)


# In[224]:


educ_series.index


# In[225]:


educ_series.values


# In[226]:


corresp_educ = pd.DataFrame({"educ_code": educ_series.index, "educ_label": educ_series.values})
corresp_educ.head()


# In[227]:


pandas_group.head()


# In[228]:


pandas_group = pd.merge(pandas_group, corresp_educ, left_on="education_num", right_on="educ_code")
pandas_group = pandas_group.drop(columns=["educ_code"])
pandas_group.head()


# In[229]:


pandas_group.groupby("educ_label")


# In[230]:


pandas_group.groupby(["educ_label","education_num"]).mean()


# In[231]:


gb = pandas_group.groupby(["educ_label","education_num"])


# In[232]:


data_agg = {
    "mean_age": gb["age"].mean() ,
    "max_age": gb["age"].max() ,
    "mean_hpw": gb["hours_per_week"].mean()
}

pd.DataFrame(data_agg)
