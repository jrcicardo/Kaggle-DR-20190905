#!/usr/bin/env python
# coding: utf-8

# In[1]:


#copy file
#erase original file
#cd
#write file


# In[16]:


import os
import random
import re
import sys
 

where = '../data/train'  
 
subdirs = list(filter(lambda x: re.search('^[0-9]*$', x), os.listdir(where)))
subdir = os.path.join(where,random.choice(subdirs))
print(os.path.join(subdir,random.choice(os.listdir(subdir))))


# In[ ]:




