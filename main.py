import requests

URL = "https://osu.ppy.sh/users/33933668"
r = requests.get(URL)
print(r.content)
