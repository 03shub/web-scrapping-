#!/usr/bin/env python
# coding: utf-8

# # Write a python program to display all the header tags from‘en.wikipedia.org/wiki/Main_Page’

# In[1]:


import bs4 
import requests
from bs4 import BeautifulSoup


# In[2]:


url = "https://en.wikipedia.org/wiki/Main_Page"


# In[3]:


data = requests.get(url)


# In[4]:


content=data.content


# In[5]:


soup = BeautifulSoup(content)


# In[6]:


for i in soup.select('.mw-headline'):
    print(i.text,end='')


# In[7]:


tag = soup.find_all("h2",class_="mp-h2")


# In[8]:


tags = []

for i in tag:
    tags.append(i.text)


# In[9]:


tags


# # Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. Name, IMDB rating, Year of

# In[10]:


page = requests.get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating")


# In[11]:


soup = BeautifulSoup(page.content)


# In[12]:


name = soup.find_all("h3",class_="lister-item-header")


# In[13]:


name_ = []

for i in name:
    name_.append(i.text.replace("\n",""))


# In[14]:


name_


# In[15]:


rate = soup.find_all("div",class_="inline-block ratings-imdb-rating")


# In[16]:


rate_ = []

for i in rate:
    rate_.append(i.text.replace("\n",""))


# In[17]:


year = soup.find_all("span",class_="lister-item-year text-muted unbold")


# In[18]:


year_ = []

for i in year:
    year_.append(i.text.replace("\n",""))


# In[19]:


import pandas as pd 


# In[20]:


web_series=pd.DataFrame({})
web_series["name_"]=name_[:100]
web_series["rate_"]=rate_[:100]
web_series["year_"]=year_[:100]


# In[21]:


web_series


# In[22]:


page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")


# In[23]:


page


# In[24]:


soup = BeautifulSoup(page.content)


# In[25]:


name = soup.find_all("td",class_="titleColumn")


# In[26]:


name


# In[27]:


name_ = []

for i in name:
    name_.append(i.text.replace("\n",""))


# In[28]:


name_


# In[29]:


rate = soup.find_all("td",class_="ratingColumn imdbRating")


# In[30]:


rate_ = []

for i in rate:
    rate_.append(i.text.replace("\n",""))


# In[31]:


rate_


# In[32]:


year = soup.find_all("span",class_="secondaryInfo")


# In[33]:


year_ = []

for i in year:
    year_.append(i.text.replace("\n",""))


# In[34]:


year_


# In[35]:


web_seriesb=pd.DataFrame({})
web_seriesb["name_"]=name_[:100]
web_seriesb["rate_"]=rate_[:100]
web_seriesb["year_"]=year_[:100]


# In[36]:


web_seriesb


# # Write a python program to scrap book name, author name, genre and book review of any 5 books from
# ‘www.bookpage.com’

# In[37]:


page = requests.get ("https://bookpage.com/reviews")


# In[38]:


page


# In[39]:


soup = BeautifulSoup(page.content)


# In[40]:


name = soup.find_all("h4",class_="italic")


# In[41]:


name_ = []
for i in name:
    name_.append(i.text.replace("\n",""))


# In[42]:


name_


# In[43]:


author_name = soup.find_all("p",class_="sans bold")


# In[44]:


author_name_ = []
for i in author_name:
    author_name_.append(i.text.replace('\n',''))


# In[45]:


author_name_


# In[46]:


about = soup.find_all("p",class_="excerpt")


# In[47]:


about_ = []

for i in about:
    about_.append(i.text.replace("\n",""))


# In[48]:


about_


# In[49]:


book=pd.DataFrame({})
book["name_"]=name_
book["author_name_"]=author_name_
book["about_"]=about_


# In[50]:


book


# In[ ]:





# In[51]:


page  = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.77493000000004&lon=-122.41941999999995#.YSY0hI4vM2w")


# In[52]:


content = page.content


# In[53]:


soup = BeautifulSoup(content)


# In[54]:


period = soup.find_all("p",class_="period-name")


# In[55]:


period_ = []
for i in period:
    period_.append(i.text)


# In[56]:


period_[0:5]


# In[57]:


temprature = soup.find_all("p",class_="temp temp-low")


# In[58]:


temprature_ = []
for i in temprature:
    temprature_.append(i.text)


# In[59]:


temprature_


# In[60]:


discription = soup.find_all("div",class_="col-sm-10 forecast-text")


# In[61]:


discription_ = []
for i in discription:
    discription_.append(i.text)


# In[62]:


discription_[0:5]


# In[63]:


short_discription = soup.find_all("p",class_="short-desc")


# In[64]:


short_discription_ = []
for i in short_discription:
    short_discription_.append(i.text)


# In[65]:


short_discription_[0:5]


# # Write a python program to extract information about the local weather from the National Weather Service 
# website of USA, https://www.weather.gov/ for the city, San Francisco. You need to extract data about 7 day 
# extended forecast display for the city. The data should include period, short description, temperature and 
# description.

# In[66]:


weather=pd.DataFrame({})
weather["period_"]=period_[0:5]
weather["discription"]=discription_[0:5]
weather["temprature_"]=temprature_[0:5]
weather["short_discription_"]=short_discription_[0:5]


# In[67]:


weather


# # . Write a python program to scrape house details from https://www.nobroker.in/ for any location. It should 
# include house title, location, area, emi and price

# In[68]:


page = requests.get("https://www.nobroker.in/property/sale/gurgaon/Sector%2056?searchParam=W3sibGF0IjoyOC40MjQ0NjAzLCJsb24iOjc3LjA5OTEyNDE5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSkZlTDFhUUVpRFRrUlh0YTJ5NEhQWFprIiwicGxhY2VOYW1lIjoiU2VjdG9yIDU2In1d&radius=2.0&type=BHK2&propertyAge=0")


# In[69]:


content = page.content


# In[70]:


soup = BeautifulSoup(content)


# In[71]:


title = soup.find_all("a",class_="nb__3CnI6")


# In[72]:


title_ = []

for i in title:
    title_.append(i.text.replace("\n",""))


# In[73]:


title_[0:10]


# In[74]:


location = soup.find_all("div",class_="nb__2CMjv")


# In[75]:


location_ = []

for i in location:
    location_.append(i.text)


# In[76]:


location_[0:10]


# In[77]:


area = soup.find_all("div",class_="nb__3oNyC")


# In[78]:


area_ = []

for i in area:
    area_.append(i.text)
    


# In[79]:


area_[0:10]


# In[80]:


emi = soup.find_all("div",class_="font-semi-bold heading-6")


# In[81]:


emi_ = []

for i in emi:
    emi_.append(i.text.replace("\n",""))


# In[82]:


emi_[2::3][0:10]


# In[83]:


house=pd.DataFrame({})
house["title_"]=title_[0:10]
house["area_"]=area_[0:10]
house["location_"]=location_[0:10]
house["emi_"]=emi_[0:10]


# In[84]:


house


# # Write a python program to scrape details of all the mobile phones under Rs. 20,000 listed on Amazon.in. The 
# scraped data should include Product Name, Price, Image URL and Average Rating

# In[85]:


page = requests.get("https://www.amazon.in/s?k=mobile+phone+under+20000+rupees&ref=nb_sb_noss_1")


# In[86]:


page # website not allowing me to fetch the data as it is not showing response 200 


# In[ ]:





# # Write a python program to scrape fresher job listings from ‘https://internshala.com/’. It should include job title, 
# company name, CTC, and apply date.

# In[87]:


page = requests.get("https://internshala.com/fresher-jobs/matching-preferences")


# In[88]:


content =page.content


# In[89]:


soup = BeautifulSoup(content)


# In[90]:


job_name = soup.find_all("div",class_="heading_4_5 profile")


# In[91]:


job_name_ = []
for i in job_name:
    job_name_.append(i.text.replace("\n",""))


# In[92]:


job_name_[0:20]


# In[93]:


company_name = soup.find_all("div",class_="heading_6 company_name")


# In[94]:


company_name_ = []
for i in company_name:
    company_name_.append(i.text.replace("\n",""))


# In[95]:


company_name_[0:20]


# In[96]:


ctc = soup.find_all("div",class_="other_detail_item")


# In[97]:


ctc_ = []
for i in ctc:
    ctc_.append(i.text.replace("\n",""))


# In[98]:


ctc_[1::3][0:20]


# In[99]:


apply_date = ctc_[2::3][0:20]


# In[100]:


job = pd.DataFrame({})
job["job_name_"]=job_name_[0:20]
job["company_name_"]=company_name_[0:20]
job["ctc_"]=ctc_[0:20]
job["apply_date"]=apply_date[0:20]


# In[101]:


job


# # Top 10 ODI teams in men’s cricket along with the records for matches, points andrating.

# In[102]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")


# In[103]:


page


# In[104]:


content = page.content


# In[105]:


soup = BeautifulSoup(content)


# In[106]:


team = soup.find_all("span",class_="u-hide-phablet")


# In[107]:


team_ = []
for i in team:
    team_.append(i.text.replace("\n",""))


# In[108]:


team_[0:10]


# In[109]:


matches = soup.find_all("td",class_="table-body__cell u-center-text")


# In[110]:


matches_ = []
for i in matches:
    matches_.append(i.text.replace("\n",""))


# In[111]:


matches_[2::2][0:10]


# In[112]:


points_=matches_[1::2][0:10]


# In[113]:


points_


# In[114]:


rate = soup.find_all("td",class_="table-body__cell u-text-right rating")


# In[115]:


rate_ = []
for i in rate:
    rate_.append(i.text.replace("\n",""))


# In[116]:


rate_[0:10]


# In[117]:


icc = pd.DataFrame({})
icc["team_"]=team_[0:10]
icc["matches_"]=matches_[0:10]
icc["points_"]=points_[0:10]
icc["rate_"]=rate_[0:10]


# In[118]:


icc


# # Top 10 ODI Batsmen in men along with the records of their team and rating

# In[119]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")


# In[120]:


page


# In[121]:


content = page.content


# In[122]:


soup = BeautifulSoup(content)


# In[123]:


name = soup.find_all("td",class_="table-body__cell name")


# In[125]:


name_ = []
for i in name:
    name_.append(i.text.replace("\n",""))


# In[127]:


name_[0:10]


# In[128]:


team  = soup.find_all("span",class_="table-body__logo-text")


# In[129]:


team_ = []
for i in team:
    team_.append(i.text.replace("\n",""))


# In[131]:


team_[0:10]


# In[132]:


ratings = soup.find_all("td",class_="table-body__cell u-text-right rating")


# In[133]:


ratings_ = []
for i in ratings:
    ratings_.append(i.text.replace("\n",""))


# In[135]:


ratings_[0:10]


# In[140]:


icc = pd.DataFrame({})
icc["name_"]=name_[0:11]
icc["team_"]=team_[0:11]
icc["ratings"]=ratings_[0:11]


# In[141]:


icc


# # Top 10 ODI bowlers along with the records of their team andrating.

# In[144]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")


# In[145]:


page


# In[146]:


content= page.content


# In[147]:


soup = BeautifulSoup(content)


# In[148]:


name = soup.find_all("td",class_="table-body__cell rankings-table__name name")


# In[150]:


name_ = []
for i in name:
    name_.append(i.text.replace("\n",""))


# In[152]:


name_[:10]


# In[153]:


team = soup.find_all("span",class_="table-body__logo-text")


# In[154]:


team_ = []
for i in team:
    team_.append(i.text.replace("\n",""))


# In[156]:


team_[:10]


# In[157]:


ratings = soup.find_all("td",class_="table-body__cell rating")


# In[158]:


ratings_ = []
for i in ratings:
    ratings_.append(i.text.replace("\n",""))


# In[159]:


ratings_[:10]


# In[160]:


icc = pd.DataFrame({})
icc["name_"]=name_[0:11]
icc["team_"]=team_[0:11]
icc["ratings"]=ratings_[0:11]


# In[161]:


icc


# # Top 10 ODI teams in women’s cricket along with the records for matches, points andrating.

# In[162]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")


# In[163]:


page


# In[164]:


content = page.content


# In[165]:


soup = BeautifulSoup(content)


# In[167]:


team = soup.find_all("span",class_="u-hide-phablet")


# In[168]:


team_ = []
for i in team:
    team_.append(i.text.replace("\n",""))


# In[187]:


team_[:11]


# In[188]:


matches = soup.find_all("td",class_="table-body__cell u-center-text")


# In[173]:


matches_ = []
for i in matches:
    matches_.append(i.text.replace("\n",""))


# In[189]:


matches_[2::2][0:11]


# In[190]:


points_=matches_[1::2][0:11]


# In[191]:


points_


# In[192]:


ratings = soup.find_all("td",class_="table-body__cell u-text-right rating")


# In[193]:


ratings_ = []
for i in ratings:
    ratings_.append(i.text.replace("\n",""))


# In[194]:


ratings_[0:11]


# In[197]:


icc = pd.DataFrame({})
icc["team_"]=team_[0:9]
icc["matches_"]=matches_[0:9]
icc["points_"]=points_[0:9]
icc["rate_"]=rate_[0:9]


# In[198]:


icc


# # Top 10 women’s ODI players along with the records of their team and rating

# In[199]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")


# In[200]:


page


# In[201]:


content = page.content


# In[202]:


soup = BeautifulSoup(content)


# In[203]:


name = soup.find_all("td",class_="table-body__cell name")


# In[204]:


name_ = []
for i in name:
    name_.append(i.text.replace("\n",""))


# In[206]:


name_[:10]


# In[207]:


team = soup.find_all("span",class_="table-body__logo-text")


# In[208]:


team_ = []
for i in team:
    team_.append(i.text.replace("\n",""))


# In[210]:


team_[:10]


# In[211]:


ratings = soup.find_all("td",class_="table-body__cell u-text-right rating")


# In[212]:


ratings_ = []
for i in ratings:
    ratings_.append(i.text.replace("\n",""))
    


# In[214]:


ratings_[:10]


# In[215]:


icc = pd.DataFrame({})
icc["name_"]=name_[0:11]
icc["team_"]=team_[0:11]
icc["ratings"]=ratings_[0:11]


# In[216]:


icc


# # Top 10 women’s ODI all-rounder along with the records of their team andrating.

# In[217]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")


# In[218]:


page


# In[219]:


content = page.content


# In[220]:


soup = BeautifulSoup(content)


# In[221]:


name = soup.find_all("td",class_="table-body__cell rankings-table__name name")


# In[222]:


name_ = []
for i in name:
    name_.append(i.text.replace("\n",""))


# In[223]:


name_[:10]


# In[224]:


team = soup.find_all("span",class_="table-body__logo-text")


# In[225]:


team_ = []
for i in team:
    team_.append(i.text.replace("\n",""))


# In[226]:


team_[:10]


# In[227]:


ratings = soup.find_all("td",class_="table-body__cell rating")


# In[228]:


ratings_ = []
for i in ratings:
    ratings_.append(i.text.replace("\n",""))
    


# In[229]:


ratings_[:10]


# In[230]:


icc = pd.DataFrame({})
icc["name_"]=name_[0:10]
icc["team_"]=team_[0:10]
icc["ratings"]=ratings_[0:10]


# In[231]:


icc


# In[ ]:




