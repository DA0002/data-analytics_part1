#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# list 실습


# In[1]:


list1 = [1,2,3,4,5]


# In[2]:


list1.pop()
list1


# In[5]:


# 리스트 삭제


# In[7]:


list1.extend(['aa', 'bb', 'vv']) 
list1


# In[8]:


# 다수의 데이터 추가


# In[9]:


list1.remove('vv')
list1


# In[10]:


# 해당 데이터 삭제


# In[12]:


pybook = ['파이썬 머신러닝 완벽가이드', '파이썬 철저 입문', '파이썬 코딩 도장', '파이썬 라이브러리를 활용한 머신러닝', '파이썬 프로그래밍']
pybook


# In[13]:


pybook.append('모두의 파이썬')


# In[23]:


pybook.insert(1, 34200)
pybook


# In[18]:


# 원하는 위치에 데이터 추가 가능


# In[27]:


del pybook[1:12]
pybook


# In[28]:


pybook.insert(3,24300)
pybook.insert(5,22500)
pybook.insert(7,27000)
pybook.insert(9,25000)
pybook.insert(11,10800)
pybook


# In[ ]:


# 가격 insert


# In[29]:


pybook.append(24750)


# In[30]:


pybook

