
# coding: utf-8

# In[27]:


import numpy as np
import pandas as pd
course = pd.read_csv('Course_Rating.csv')
def myfunc(s1,s2):
        s1_c = s1-s1.mean()
        s2_c = s2-s2.mean()
        return (np.sum(s1_c*s2_c)/np.sqrt(np.sum(s1_c ** 2) * np.sum(s2_c ** 2)))


# In[28]:


class Recommend():
    def __init__(self):
        self.course_name = None

    def recomm(self,course_name):
        self.course_name = course_name
        reviews = []
        for name in course.columns:
            if name == course_name:
                continue
            cor = myfunc(course[course_name],course[name])
            if np.isnan(cor):
                continue
            else:
                reviews.append((name,cor))
        reviews.sort(key=lambda tup: tup[1], reverse=True)
        return reviews[:5]

