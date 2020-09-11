import requests
from win32com.client import Dispatch
import time

speak = Dispatch('SAPI.spvoice')
speak.Speak('Today\'s headlines are: ')
url = 'https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=YOUR NEWS API KEY HERE'
news = requests.get(url).json()

headlines = news['articles']
newslist1 = []
for i in headlines:
    newslist1.append(i['title'])
str1 = ''
for j in range(len(newslist1)):
    str1 = str(j+1) + ': ' + newslist1[j]
    print(str1)
    speak.Speak(str1)


