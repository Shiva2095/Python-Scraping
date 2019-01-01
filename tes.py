import requests
import bs4
res =requests.get("https://plantvillage.psu.edu/topics/aloe-vera/infos")
print(type(res))
#print(res.text)
soup=bs4.BeautifulSoup(res.text,'lxml')
print(type(soup))
hi=soup.select('title')
print(hi)
