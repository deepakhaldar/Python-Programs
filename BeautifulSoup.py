from bs4 import BeautifulSoup
import requests

url = 'http://www.thefamouspeople.com/singers.php'
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

links=soup.find_all("a")
