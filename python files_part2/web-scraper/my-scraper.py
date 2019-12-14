from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.01xq.com/xqplayer/xqrating.asp')

soup = BeautifulSoup(page.content,'html.parser')

#12019-2Wang TianYiBeiJing271112724-1310
# print(soup.find_all('tr')[2].contents[2].get_text())

# for tr in soup.find_all('tr'):
#     td=tr.find('td')[2]

arr=[]
for i,j in enumerate(soup.find_all('tr')):
    print(j)
    break

# print(soup.title.string)
# print(soup.title)