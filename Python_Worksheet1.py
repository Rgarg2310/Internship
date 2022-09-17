#!/usr/bin/env python
# coding: utf-8

# # Python_worksheet-1

# In[ ]:





# In[1]:


#Code to find factorial of a number
def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))


# In[2]:


num=int(input("Enter any number"))
result= factorial(num)
result


# In[6]:


# Code to find a prime and composite number
n= int (input("Enter any value"))
if (n==0 or n==1):
    print (n, "number is neither prime nor composite")
elif n>1:
    if (n%2==0):
        print (n, "number is composite number")
    else:
        print (n, "number is prime number")
else:
    print("Print positive number only")


# In[25]:


#code to find out wheather a string is palindrome or not

Str = "civic"
def string(Str):
    Str = str(input("The Word "))
    Str= Str.casefold()
    rev_str = reversed(Str)

    if list(Str) == list(rev_str):
        print ("the string is a palindrome")
    else:
        print ("the string is not a palindrome")


# In[26]:


Result = string(Str)


# In[27]:


Result1 = string(Str)


# In[ ]:





# In[30]:


# Code to find out third side of right angle triangle from two given side

def triangle():
    AB = int(input("First Side "))
    BC = int(input("Second Side "))
    AC = ((AB**2)+ (BC**2))**(1/2)
    print ("The thirld side of triangle is", AC)


# In[31]:


result= triangle()


# In[ ]:





# In[ ]:





# In[33]:


String = "hhmmtt"
str1= list(String)


# In[34]:


str1


# In[35]:


strlist=[]


# In[36]:


strlist


# In[37]:


freq= str1


# In[38]:


freq


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




