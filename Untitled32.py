#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return 'fizzbuzz'
    elif num % 3==0:
        return 'fizz'
    elif num % 5==0:
        return ' buzz'
    else:
        return num
    
for i in range(1,100):
        print (fizz_buzz(i))


# In[ ]:




