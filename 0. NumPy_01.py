#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math


# # Array Creation

# In[2]:


a = np.array([1, 2, 3])
print(a) 


# In[5]:


b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)


# In[6]:


b.shape


# In[7]:


a.dtype


# In[8]:


c = np.array([[1.1, 2.2, 3.4], [4.6, 5.7, 6.8]])
print(c)


# In[9]:


c.dtype.name


# In[10]:


d = np.zeros((2,3))
print(d)


# In[11]:


e = np.ones((2,3))
print(e)


# In[16]:


f = np.random.rand(2,3)
print(f)


# In[19]:


g = np.arange(10, 50, 2) #começa no 10, termina no 50 com 2 de espaçamento
print(g)


# In[21]:


h = np.linspace(0,2,15)
print(h)


# # Arrays Operations
# 

# In[24]:


a = np.array([10,20, 30, 40])
a


# In[26]:


b = np.array([1, 2, 3, 4])
b


# In[27]:


c = a - b
c


# In[28]:


d = a*b
d


# In[30]:


farenheit = np.array([0, -10, -5, -15, 0])

celcius = (farenheit - 31)*(5/9)

print(farenheit)

print(celcius)


# In[31]:


celcius > 20


# In[32]:


celcius < 20


# In[33]:


celcius < - 20


# In[35]:


celcius%2 == 0 #módulo 2 = 0


# In[36]:


#Produto de matrizes
A = np.array([[1, 2], [7, 8]])
B = np.array([[3, 4], [5, 6]])

print(A*B)


# In[37]:


print(A@B)


# In[38]:


A.shape


# In[39]:


B.shape


# In[40]:


array1 = np.array([[1, 2, 3], [4, 5, 6]])
print(array1.dtype)

array2 = np.array([[7.1, 8.2, 9.3], [10.4, 11.5, 12.6]])
print(array2.dtype)


# In[43]:


array3 = array1 + array2
print(array3.dtype)
array3


# In[42]:


print(array3.dtype)


# In[44]:


print(array3.sum())
print(array3.max())
print(array3.min())
print(array3.mean())


# In[48]:


b = np.arange(1, 16, 1).reshape(3, 5)
print(b)


# # Indexing, Slicing and Interating

# ## Indexing

# In[50]:


a = np. array( [1, 3, 5, 7])
a[2]


# In[52]:


a = np.array([[1, 2], [3, 4], [5, 6]])
a


# In[54]:


np.array([a[0, 0], a[1, 1], a[2, 1]])


# In[55]:


print(a[[0 , 1, 2], [0, 1, 1]])


# ## Boolean Indexing

# In[56]:


print(a>5)


# In[57]:


print(a[a>5])


# ## Slicing

# In[58]:


a = np.array([0, 1, 2, 3, 4, 5])
print(a)


# In[59]:


print(a[:3])


# In[60]:


print(a[1:3])


# In[61]:


print(a[2:4])


# In[63]:


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a


# In[66]:


a[:2, 1:3] #primeiro argumento para linhas e segundo para colunas


# In[68]:


sub_array = a[:2, 1:3]
print(sub_array[0,0])


# In[69]:


sub_array[0, 0] = 50


# In[70]:


print(a)


# In[80]:


wines = np.genfromtxt("C:\\Users\\valvi\\Documents\\5. Coursera\\0. Introducing to Python\\Week 1\\CSV\\winequality-red.csv", delimiter=";", skip_header=1)
print(wines)


# In[82]:


print("one integer 0 for slicing: ", wines[:,0]) #lista única, todas as linhas e primeira coluna


# In[83]:


print("0 to 1 for slicing: ", wines[:,0:1]) #coluna original


# In[84]:


wines[:, 0:3]


# In[85]:


wines[:,[0, 2, 4]]


# In[92]:


wines[:, -1].mean()


# In[122]:


graduate_admission = np. genfromtxt('C:\\Users\\valvi\\Documents\\5. Coursera\\0. Introducing to Python\\Week 1\\CSV\\Admission_Predict.csv', delimiter=',', skip_header=1, names=('Serial No', 'GRE_Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research', 'Chance_of_Admit'))
graduate_admission


# In[126]:


graduate_admission['CGPA'][0:5]


# In[127]:


graduate_admission['CGPA'] = graduate_admission['CGPA'] /10 *4
graduate_admission['CGPA'][0:20]


# In[128]:


len(graduate_admission[graduate_admission['Research'] ==1]) #descobre quantos alunos fizeram pesquisa, quantos valores são verdadeiros == 1


# In[129]:


print(graduate_admission[graduate_admission['Chance_of_Admit']>0.8]['GRE_Score'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit']<0.4]['GRE_Score'].mean())


# In[130]:


print(graduate_admission[graduate_admission['Chance_of_Admit']>0.8]['CGPA'].mean())
print(graduate_admission[graduate_admission['Chance_of_Admit']<0.4]['CGPA'].mean())


# In[ ]:




