#!/usr/bin/env python
# coding: utf-8

# In[84]:


# Import Splinter and BeautifulSoup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.firefox import GeckoDriverManager


# In[85]:


executable_path = {'executable_path': GeckoDriverManager().install()}
browser = Browser('firefox', **executable_path, headless=False)


# In[86]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[87]:


# Set up the html parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[88]:


slide_elem.find('div', class_='content_title')


# In[89]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[90]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[91]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[92]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[93]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[94]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[95]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[96]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[97]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[98]:


df.to_html()


# In[99]:


browser.quit()


# In[ ]:





# In[100]:


# Import Splinter and BeautifulSoup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.firefox import GeckoDriverManager


# In[101]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': GeckoDriverManager().install()}
browser = Browser('firefox', **executable_path, headless=False)


# # Visit the NASA Mars News Site

# In[102]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[103]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[104]:


slide_elem.find('div', class_='content_title')


# In[105]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[106]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # JPL Space Images Featured Image

# In[107]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[108]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[109]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[110]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[111]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Mars Facts

# In[112]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[113]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[114]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[115]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[116]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
hemisphere_soup = soup(html, 'html.parser')

result_box = hemisphere_soup.find('div', class_="collapsible results")

links_with_text = []
for a in result_box.find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])



# for loop over the link of each sample picture
for i in range (4):
    # Create an empty dict to hold the search results
    hemisphere_image_results = {}
    # Find link 
    browser.visit(f'https://marshemispheres.com/{links_with_text[i]}')
    
    # Parse the new html page with soup
    html = browser.html
    sample_image_soup = soup(html, 'html.parser')
    # Get the full image link
    img_url = sample_image_soup.select_one("div.downloads ul li a").get('href')
    # Get the full image title
    img_title = sample_image_soup.select_one("h2.title").get_text()
    # Add extracts to the results dict
    hemisphere_image_results = {
        'img_url': f'https://marshemispheres.com/{img_url}' ,
        'title': img_title}
    # Append results dict to hemisphere image urls list
    hemisphere_image_urls.append(hemisphere_image_results)
    # Return to main page
    browser.back()


# In[117]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[118]:


# 5. Quit the browser
browser.quit()


# In[ ]:




