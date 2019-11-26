# In[356]:


data_dum = data.drop(columns=['fnlwgt', 'education'])


# In[357]:


data_dum = pd.get_dummies(data_dum, columns=['workclass', 'marital_status', 
                                             'occupation', 'relationship', 
                                             'sex','native_country'])


# In[358]:


data_dum["income_num"] = [0 if i == "<=50K" else 1 for i in data_dum["income"]]


# In[359]:


X = data_dum.drop(columns = ["income","income_num"])
y = data_dum["income_num"]


# In[360]:


from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(X, y)

lr = LogisticRegression()

lr.fit(X_train,y_train)

y_prob = lr.predict_proba(X_test)[:,1] 
y_prob


# In[361]:


y_pred = np.where(y_prob > 0.3, 1, 0) 
y_pred


# In[362]:


result = X_test.copy()
result["real_class"] = ["<=50K" if i == 0 else ">50K" for i in y_test]
result["real_class_code"] = y_test
result["predicted_class_code"] = y_pred
result


# In[363]:


from sklearn import metrics
metrics.confusion_matrix(y_test, y_pred)


# In[364]:


from sklearn.svm import LinearSVC

svm = LinearSVC()

svm.fit(X_train,y_train)

y_pred = svm.predict(X_test) 

metrics.confusion_matrix(y_test, y_pred)


# In[368]:


from sklearn import linear_model

X = ozone_data[['temp9', 'temp12', 'temp15', 'cloud9', 'cloud12',
       'cloud15', 'wind9', 'wind12', 'wind15', 'prev_maxO3']]
y = ozone_data['maxO3']

X_train, X_test, y_train, y_test = train_test_split(X, y)

linreg = linear_model.LinearRegression()

linreg.fit(X_train,y_train)

y_pred = linreg.predict(X_test)

linreg.score(X_test, y_test)
