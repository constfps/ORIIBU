import requests
from bs4 import BeautifulSoup

URL = "https://osu.ppy.sh/users/33933668"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
print(soup.encode("utf-8"))
