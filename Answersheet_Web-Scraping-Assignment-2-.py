#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# WEB Scraping using Selenium


# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import pandas as pd


# In[3]:


import selenium
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[4]:


driver = webdriver.Chrome(r"C:\Users\91817\Downloads\chromedriver_win32\chromedriver.exe")


# In[ ]:


driver.get("http://www.naukri.com/")


# In[ ]:


designation = driver.find_element(By.CLASS_NAME, "suggestor-input")
designation.send_keys('Data analyst')


# In[ ]:


location = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[ ]:


job_title = []
job_location = []
companyname= []
experience_required= []


# In[ ]:





# In[ ]:


search = driver.find_element(By.CLASS_NAME, "qsbSubmit")
search.click()


# In[ ]:


# Job Title

title_tags = driver.find_elements(By.XPATH, '//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title= i.text

    job_title.append(title)


# In[ ]:





# In[ ]:





# In[ ]:


location_tags = driver.find_elements(By.XPATH, '//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location= i.text

    job_location.append(location)


# In[ ]:





# In[ ]:


company_tags = driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company= i.text

    companyname.append(company)
companyname


# In[ ]:


experience_tags = driver.find_elements(By.XPATH, '//li[@class="fleft grey-text br2 placeHolderLi experience"]')
for i in experience_tags[0:10]:
    experience= i.text

    experience_required.append(experience)


# In[ ]:


experience_required


# In[ ]:


print(len(job_title),len(companyname), len(job_location), len(experience_required))


# In[ ]:


df=pd.DataFrame({'job_title': job_title, 'Job_location': job_location, 'company_name': companyname, 'Experience_required':experience_required})
df


# In[ ]:


# Question-1 from Assignment-2 completed


# In[ ]:


driver = webdriver.Chrome(r"C:\Users\91817\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://www.naukri.com/")


# In[ ]:


designation1 = driver.find_element(By.CLASS_NAME, "suggestor-input")
designation1.send_keys('Data Scientist')

location1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location1.send_keys('Bangalore')

search1 = driver.find_element(By.CLASS_NAME, "qsbSubmit")
search1.click()


# In[ ]:


job_title1 = []
job_location1 = []
companyname1= []


# In[ ]:


# Job Title

title_tags1 = driver.find_elements(By.XPATH, '//a[@class="title fw500 ellipsis"]')
for i in title_tags1[0:10]:
    title1= i.text

    job_title1.append(title1)
    
 # Job Location   
location_tags1 = driver.find_elements(By.XPATH, '//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags1[0:10]:
    location1= i.text

    job_location1.append(location1)

# Company_name    
company_tags1 = driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tags1[0:10]:
    company1= i.text

    companyname1.append(company1)  


# In[ ]:


print(len(job_title1),len(companyname1), len(job_location1))


# In[ ]:


df=pd.DataFrame({'job_title1': job_title1, 'Job_location1': job_location1, 'company_name1': companyname1})
df


# In[ ]:


#  Question-2 from Assignment-2 completed


# In[ ]:





# In[ ]:


driver = webdriver.Chrome(r"C:\Users\91817\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://www.naukri.com/")


# In[ ]:


designation2 = driver.find_element(By.CLASS_NAME, "suggestor-input")
designation2.send_keys('Data Scientist')

search1 = driver.find_element(By.CLASS_NAME, "qsbSubmit")
search1.click()


# In[ ]:


location = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/section[1]/div[2]/div[5]/div[2]/div[3]/label/p/span[1]")
location.click()


# In[ ]:


salary_filter = driver.find_element(By.XPATH, "/html/body/div/div[4]/div/section[1]/div[2]/div[6]/div[2]/div[2]/label/p/span[1]")
salary_filter.click()


# In[ ]:


job_title2 = []
job_location2 = []
companyname2= []
experience_required2= []


# In[ ]:





# In[ ]:


title_tags2 = driver.find_elements(By.XPATH, '//a[@class="title fw500 ellipsis"]')
for i in title_tags2[0:10]:
    title2= i.text

    job_title2.append(title2)
    
 # Job Location   
location_tags2 = driver.find_elements(By.XPATH, '//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags2[0:10]:
    location2= i.text

    job_location2.append(location2)

# Company_name    
company_tags2 = driver.find_elements(By.XPATH, '//a[@class="subTitle ellipsis fleft"]')
for i in company_tags2[0:10]:
    company2= i.text

    companyname2.append(company2) 
    
#Experience_required
    experience_tags2 = driver.find_elements(By.XPATH, '//li[@class="fleft grey-text br2 placeHolderLi experience"]')
for i in experience_tags2[0:10]:
    experience2= i.text

    experience_required2.append(experience2)


# In[ ]:


print(len(job_title2),len(companyname2), len(job_location2), len(experience_required2))


# In[ ]:


df=pd.DataFrame({'job_title': job_title2, 'Job_location': job_location2, 'company_name': companyname2, 'Experience_required':experience_required2})
df


# In[ ]:


# #  Question-3 from Assignment-2 completed


# In[ ]:


driver = webdriver.Chrome(r"C:\Users\91817\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/")

frontpage = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
frontpage.click()

designation3 = driver.find_element(By.CLASS_NAME, "_3704LK")
designation3.send_keys('sunglasses')


# In[ ]:


search3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search3.click()


# In[ ]:


brand = []
product_discription = []
price=[]


# In[ ]:





# In[ ]:


start=0
end=3
for page in range(start, end):
    brand_tags = driver.find_elements(By.XPATH, '//div[@class="_2WkVRV"]')
    for i in brand_tags:
        brand.append(i.text)
        
    product_tags = driver.find_elements(By.XPATH, '//a[@class="IRpwTa"]')
    for i in product_tags:
        product_discription.append(i.text)

    price_tags = driver.find_elements(By.XPATH, '//a[@class="_3bPFwb"]')
    for i in price_tags:
        price.append(i.text)
    
    
    next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(5)
    


# In[ ]:


len(brand),len(product_discription),len(price)


# In[ ]:


brand1 = []
product_discription1 = []
price1=[]


# In[ ]:


for i in brand[0:100]:
    brand1.append(i)


for i in product_discription[0:100]:
    product_discription1.append(i)
    
    
for i in price[0:100]:
    price1.append(i)


# In[ ]:


len(brand1),len(product_discription1),len(price1)


# In[ ]:


df4=pd.DataFrame({'brand': brand1, 'product_discription': product_discription1, 'price': price1})
df4


# In[ ]:


# #  Question-4 from Assignment-2 completed


# In[ ]:


driver = webdriver.Chrome(r"C:\Users\91817\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/")

frontpage = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
frontpage.click()

designation3 = driver.find_element(By.CLASS_NAME, "_3704LK")
designation3.send_keys('iphone 11')

search3 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search3.click()


# In[ ]:


search4 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]')
search4.click()


# In[ ]:


rating= []
review_summary= []
full_review=[]


# In[ ]:





# In[175]:


start=0
end=12
for page in range(start, end):
    rating_tags = driver.find_elements(By.XPATH, '//div[@class="_3LWZlK _1BLPMq"]')
    for i in rating_tags:
        rating.append(i.text)
        
    summary_tags = driver.find_elements(By.XPATH, '//p[@class="_2-N8zT"]')
    for i in summary_tags:
        review_summary.append(i.text)

    review_tags = driver.find_elements(By.XPATH, '//div[@class="t-ZTKy"]')
    for i in review_tags:
        full_review.append(i.text)
        
    next_button4 = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div/div[2]/div[13]/div/div/nav/a[11]')
    next_button4.click(
    
        


# In[176]:


# I am facing problem here to click on All reviews (please share the Answer sheet)


# In[ ]:





# In[5]:


driver = webdriver.Chrome(r"C:\Users\91817\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.flipkart.com/")

frontpage = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
frontpage.click()

designation3 = driver.find_element(By.CLASS_NAME, "_3704LK")
designation3.send_keys('sneakers')


# In[6]:


search6 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search6.click()


# In[7]:


brand1 = []
product_discription1 = []
price1=[]


# In[9]:


start=0
end=3
for page in range(start, end):
    brand_tags = driver.find_elements(By.XPATH, '//div[@class="_2WkVRV"]')
    for i in brand_tags:
        brand1.append(i.text)
        
    product_tags = driver.find_elements(By.XPATH, '//a[@class="IRpwTa"]')
    for i in product_tags:
        product_discription1.append(i.text)

    price_tags = driver.find_elements(By.XPATH, '//div[@class="_30jeq3"]')
    for i in price_tags:
        price1.append(i.text)
    
    
    next_button1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button1.click()
    time.sleep(5)


# In[10]:


len(brand1),len(product_discription1),len(price1)


# In[11]:


brand2 = []
product_discription2 = []
price2=[]


# In[ ]:





# In[12]:


for i in brand1[0:100]:
    brand2.append(i)


for i in product_discription1[0:100]:
    product_discription2.append(i)
    
    
for i in price1[0:100]:
    price2.append(i)


# In[13]:


df6=pd.DataFrame({'brand': brand2, 'product_discription': product_discription2, 'price': price2})
df6


# In[14]:


# #  Question-6 from Assignment-2 completed


# In[ ]:





# In[17]:


driver = webdriver.Chrome(r"C:\Users\91817\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://www.myntra.com/shoes")


# In[18]:


#Question-7 I have faced probelm with the site as no right click work on that site. 


# In[ ]:





# In[19]:


driver = webdriver.Chrome(r"C:\Users\91817\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://www.amazon.in/")


# In[20]:


search = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search.send_keys('Laptop')


# In[21]:


search7 = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search7.click()


# In[22]:


filter1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[5]/li[12]/span/a/span')
filter1.click()


# In[23]:


title = []
ratings = []
price=[]


# In[24]:


title_tags8 = driver.find_elements(By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title_tags8[0:10]:
    title2= i.text

    title.append(title2)
    
 # Rating  
rating_tag8 = driver.find_elements(By.XPATH, '//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in rating_tag8[0:10]:
    rating= i.text

    ratings.append(rating)

# price    
price_tags8 = driver.find_elements(By.XPATH, '//span[@class="a-price-whole"]')
for i in price_tags8[0:10]:
    company2= i.text

    price.append(company2) 
    


# In[27]:


len(title),len(ratings),len(price)


# In[ ]:





# In[26]:


# Rating  
rating_tag8 = driver.find_elements(By.XPATH, '//div[@class="a-row a-size-small"]')
for i in rating_tag8[0:10]:
   rating= i.text

   ratings.append(rating)
   len(ratings)


# In[28]:


df8=pd.DataFrame({'title': title, 'ratings': ratings, 'price': price})
df8


# In[30]:


#Question - 8 from Assignment-2 is completed


# In[ ]:





# In[31]:


driver = webdriver.Chrome(r"C:\Users\91817\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://www.ambitionbox.com/")


# In[32]:


search9 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/header/nav/ul/li[5]/a')
search9.click()


# In[33]:


search10 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/div/span/input')
search10.send_keys('Data Scientist')


# In[34]:


search11 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/button/span')
search11.click()


# In[35]:


search12 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/p')
search12.click()


# In[37]:


search13 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/input')
search13.send_keys('Noida')


# In[38]:


search14 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/label')
search14.click()


# In[49]:


companyname = []
days_of_posting = []
rating=[]


# In[50]:


company_tags8 = driver.find_elements(By.XPATH, '//p[@class="company body-medium"]')
for i in company_tags8[0:10]:
    title2= i.text

    companyname.append(title2)
    
 # Rating  
posting_tag8 = driver.find_elements(By.XPATH, '//span[@class="body-small"]')
for i in posting_tag8[0:10]:
    rating11= i

    days_of_posting.append(rating11)

# price    
rating_tags8 = driver.find_elements(By.XPATH, '//a[@class="rating rating-4"]')
for i in rating_tags8:
    company2= i.text

    rating.append(company2) 


# In[51]:


len(companyname),len(days_of_posting),len(rating)


# In[53]:


companyname1 = []
days_of_posting1 = []
rating1=[]


# In[ ]:





# In[54]:


for i in companyname[0:9]:
    companyname1.append(i)


for i in days_of_posting[0:9]:
    days_of_posting1.append(i)
    


# In[55]:


len(companyname1),len(days_of_posting1),len(rating)


# In[56]:


df8=pd.DataFrame({'companyname1': companyname1, 'days_of_posting1': days_of_posting1, 'rating': rating})
df8


# In[57]:


#Question - 9 from Assignment-2 is completed


# In[ ]:





# In[66]:


driver = webdriver.Chrome(r"C:\Users\91817\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://www.ambitionbox.com/")


# In[ ]:





# In[62]:


search9 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/header/nav/ul/li[3]/span')
search9.click()
search10 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/header/nav/ul/li[3]/div/ul/li[1]/div/div[2]/p')
search10.click()


# In[64]:


search11 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/span/input')
search11.send_keys('Data Scientist')


# In[65]:


search12 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/button/span')
search12.click()


# In[67]:


#Question - 10 from Assignment-2 is not matching with your screen shot, the website is not working as shown in assignment please help. 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


brand1


# In[ ]:





# In[ ]:





# In[ ]:


len(brand)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


brand


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




