# ### Video 1.3 - Installing Python and creating a first Jupyter notebook 

# In[2]:


9 + 3


# In[3]:


20+1
3


# ### Video 1.4 - Overview of the different variable types 

# In[4]:


20 + 1


# In[5]:


age = 20+1


# In[6]:


age


# In[7]:


2022 - age


# In[8]:


age = 37


# In[9]:


age


# In[10]:


name = 'Olivia'


# In[11]:


name = "Olivia"


# In[12]:


name


# In[13]:


name[4]


# In[14]:


name[0]


# In[15]:


name[4:6]


# In[16]:


children = ["Lea","Rob","Tina"]
children


# In[17]:


children[0]


# In[18]:


children[0][2]


# In[19]:


children[2]


# In[20]:


children[-1]


# In[21]:


children[0:2]


# In[22]:


#children[3]


# In[23]:


children[1] = "Bobby"
children


# In[24]:


len(children)


# In[25]:


someone = {
    'age': 37,
    'name': 'olivia',
    'hours_per_week': 40,
    'children': ["Lea","Rob","Tina"],
}


# In[26]:


#someone[2]


# In[27]:


someone["age"]


# In[28]:


someone["children"]


# In[29]:


someone["children"][1][0]


# In[30]:


type(someone)


# In[31]:


type(someone["children"])


# In[32]:


type("female")


# In[33]:


type(2)


# In[34]:


type(2.3)


# In[35]:


type(2.0)


# In[36]:


type(2.)


# In[37]:


float(2)


# In[38]:


int(2.3)


# In[39]:


str(2)


# ### Video 1.5 Manipulating variables with operators
# 

# In[40]:


age = 10


# In[41]:


age + 4


# In[42]:


age - 2


# In[43]:


(10 * age) / 2


# In[44]:


age**2


# In[45]:


age = age + 5
age


# In[46]:


age += 5
age


# In[47]:


age -= 5
age


# In[48]:


age *= 2
age


# In[49]:


age /= 2
age


# In[50]:


age > 10


# In[51]:


age <= 10


# In[52]:


age == 15


# In[53]:


age == 16


# In[54]:


age != 16


# In[55]:


condition = (3 == 4)
condition


# In[56]:


condition == False


# In[57]:


condition is False


# In[58]:


condition is True


# In[59]:


age = None
age


# In[60]:


age is None


# In[61]:


type(age)


# In[62]:


age == 2


# In[63]:


name = "Tina"
sentence = "Hello, my name is " + name
sentence


# In[64]:


age = 30


# In[65]:


"I'm " + str(30) + "years old"


# In[66]:


children = ["Lea","Rob","Tina"]


# In[67]:


children + ["Tom"]


# In[68]:


children


# In[69]:


children = children + ['Tom', 'Eve']
# children += ['Tom', 'Eve']
children


# In[70]:


children.append('Donald')
# children += ['Donald']
children


# In[71]:


children.extend(['Isabella','Emma'])
children


# In[72]:


RGB = (0.2, 0, 0.99)
RGB


# In[73]:


coordinates = (2.3, 4.554)
coordinates


# In[74]:


(x, y) = (2.3, 4.554)
x


# In[75]:


y


# ### Video 1.6 - Writing functions with python 

# In[76]:


len([56, 23, "something"])


# In[77]:


hours_per_week = 40
hours_per_day = hours_per_week / 5
hours_per_day


# In[78]:


def compute_hours_per_day(hours_per_week):
    hours_per_day = hours_per_week / 5
    return hours_per_day


# In[79]:


compute_hours_per_day(40)


# In[80]:


a_variable = 30
compute_hours_per_day(a_variable)


# In[81]:


def compute_hours_per_day(hours_per_week, working_days):
    hours_per_day = hours_per_week / working_days
    return hours_per_day


# In[82]:


compute_hours_per_day(30, 5)


# In[83]:


compute_hours_per_day(30, 6)


# In[84]:


#compute_hours_per_day(30)


# In[85]:


def compute_hours_per_day(hours_per_week, working_days = 5):
    hours_per_day = hours_per_week / working_days
    return hours_per_day


# In[86]:


compute_hours_per_day(30, 6)


# In[87]:


compute_hours_per_day(30, working_days=6)


# ### Video 1.7 - Conditions and loops 

# In[88]:


group = [
    {
        'first_name': 'Claudia',
        'last_name': 'Foufoune',
        'sex': 'female',
        'native_country': 'France'
    },
    {
        'first_name': 'Aditya',
        'last_name': 'Patel',
        'sex': 'male',
        'native_country': 'India'
    },
    {
        'first_name': 'Olivia',
        'last_name': 'Becker',
        'sex': 'female',
        'native_country': 'United States'
    },
    {
        'first_name': 'Tom',
        'last_name': 'Parker',
        'sex': None,
        'native_country': 'USA'
    },
]


# In[89]:


for person in group:
    print()
    print(person['first_name'] + ' :')
    print(person)


# In[90]:


for person in group:
    
    if person['sex'] == 'female':
        title = "Mrs"
    elif person['sex'] == 'male':
        title = "Mr"
    else :
        title = person['first_name']
    
    print()
    print(title + " " + person['last_name'] + ' :')
    print(person)


# In[91]:


country = None
i = 0

while country != "USA" and country != "United States" and i<len(group) :
    
    person = group[i]
    
    message = "iteration {} : Currently analysing {} {} "
    message = message.format(i, person['first_name'], person['last_name'])
    print(message)
    
    country = person['native_country']
    
    i += 1
    
if person != None:
    print("Someone from the USA :")
    print(person)


# In[92]:


country = "United States"


# In[93]:


country != "USA"


# In[94]:


country != "United States"


# In[95]:


country != "USA" and country != "United States"


# In[96]:


True and True


# In[97]:


False and True


# In[98]:


False or True


# In[99]:


False or False


# In[100]:


not False


# In[101]:


not True


# In[102]:


country != "USA" and country != "United States"

not (country == "USA" or country == "United States")


# In[103]:


country = None
i = 0

while not (country in ["USA", "United States"]) and i<len(group) :
    
    person = group[i]
    
    message = "iteration {} : Currently analysing {} {} "
    message = message.format(i, person['first_name'], person['last_name'])
    print(message)
    
    country = person['native_country']
    
    i += 1
    
if person != None:
    print("Someone from the USA :")
    print(person)


# In[104]:


#while True:
#    print("hello")


# In[105]:


for n in range(0, 100, 10):
    print(n)


# In[106]:


a_list = []
for n in range(0, 100, 10):  
    a_list.append(2*n)


# In[107]:


a_list


# In[108]:


[2*n for n in range(0, 100, 10)]


# In[109]:


a_dict = {}
some_data = [["alicia", 4],["bob", 2],["betty", 3]]

{element[0]:element[1] for element in some_data}


# ### Video 1.8 - Object Oriented programming with Python 

# In[110]:


class Person:
    def __init__(self, name, age, education_num, hours_per_week):
        self.name = name
        self.age = age
        self.education = education_num
        self.hpw = hours_per_week
        
    def get_hours_per_day(self):
        return self.hpw/5
    
    def increase_age(self, delta):
        self.age = self.age + delta


# In[111]:


person1 = Person("Anna", 28, 10, 40)
person1.hpw


# In[112]:


person1.get_hours_per_day()


# In[113]:


person1.increase_age(1)
person1.age


# In[114]:


anna = [28, 10, 40]
bob = [34, 5, 35]


# In[115]:


group = [anna, bob]
group


# In[116]:


[[28, 10, 40], 
 [34, 5 , 35]]


# In[117]:


class groupOfPeople:   
    def __init__(self):   
        self.data = []
        self.columns = ['age', 'education.num', 'hours.per.week']
        self.names = []
        self.size = 0
        self.shape = (0, 3)
        
    def addPerson(self, person):
        person_info = [person.age, person.education, person.hpw]
        self.data.append(person_info)
        self.names.append(person.name)
        
        self.size += 1
        self.shape = (self.size, 3)
        
        #print("\n" + person.name + " sucessfully added. \nCurrent shape of the data :" + 
        #      str(self.shape))
        
    def displayPersonInfo(self, index):
        person_info = self.data[index]
        print("Age : ", person_info[0])
        print("Education : " , person_info[1])
        print("Hours per week : ", person_info[2])
        print("Name : ", self.names[index])
        
    def getAllAges(self):
        result = []
        for person_info in self.data:
            age = person_info[0]
            result.append(age)
        return result
    
    def getAllEduc(self):
        return [person_info[1] for person_info in self.data]
    
    def getAllHpw(self):
        return [person_info[2] for person_info in self.data]
        
    def mean(self):
        all_ages = self.getAllAges()
        all_educ = self.getAllEduc()
        all_hpw  = self.getAllHpw()
        
        average_age = sum(all_ages)/self.size
        average_edu = sum(all_educ)/self.size
        average_hpw = sum(all_hpw) /self.size
        
        return [average_age, average_edu, average_hpw]
    
    def __getitem__(self,index):
        return self.data[index]


# In[118]:


group = groupOfPeople()

group.addPerson(person1)

person2 = Person("Bob", 45, 9, 30)
group.addPerson(person2)

group.addPerson(Person("Andy", 34, 5, 35))
group.addPerson(Person("Lea", 38, 4, 35))

#group.displayPersonInfo(2)

group.getAllAges()

group.mean()

group[2]


