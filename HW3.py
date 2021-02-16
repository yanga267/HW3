#!/usr/bin/env python
# coding: utf-8

# In[3]:


#q0
marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}


# In[11]:


#q1
for student,grades in marks.items():
    print(f'{student} scored {grades}')


# In[24]:


#q2
import statistics
from statistics import mean
key_max=max(marks,key=marks.get)
key_min=min(marks,key=marks.get)
print('mean= ',mean(marks[k] for k in marks))
print('max= ',marks[key_max])
print('min= ',marks[key_min])


# In[37]:


#q3
for student,grades in marks.items():
    if 'J' in student:
        break
    else:
        print({student})


# In[38]:


#q4
for student,grades in marks.items():
    if 'J' in student:
        print(end='')
    else:
        print({student})


# In[39]:


def print_student(student_name):
    marks = {'Andy':88, 'Amy':66, 'James': 90, 'Jules': 55, 'Arthur': 77}
    for student in marks:
        if student == student_name:
            print(marks[student])
            break
    else:
        print('No entry with name found.')
        
print_student('Andy')


# In[ ]:




