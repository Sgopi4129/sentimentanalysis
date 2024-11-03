from bs4 import BeautifulSoup
from rake_nltk import Rake
import  numpy as np
import pandas as pd
import requests
url='https://www.reddit.com/r/antiwork/'
HTML_data=requests.get(url).text
data=BeautifulSoup(HTML_data,'lxml')
text_data=data.find('div',class_='i18n-subreddit-description description text-left text-neutral-content-weak').text
r=Rake()
data=r.extract_keywords_from_text(text_data)
print(data)