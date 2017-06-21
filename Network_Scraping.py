import requests
from bs4 import BeautifulSoup

url="https://losangeles.craigslist.org/search/sss?query=chair&min_price=350"
r=requests.get(url)
soup=BeautifulSoup(r.content)

links= soup.find_all("a")
for link in links:
        print("<a href= {}>{}</a>".format(link.get("href"), link.text))

g_data=soup.find_all("div")
print(g_data)

for item in g_data:
    print(item.contents)