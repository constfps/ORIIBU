from ossapi import Ossapi
from instagrapi import Client
import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = os.getenv("USER_ID")
username = os.getenv("ACCOUNT_USERNAME")
password = os.getenv("ACCOUNT_PASSWORD")

api = Ossapi(client_id, client_secret)
cl = Client()
cl.login(username, password)

user = api.user(user_id, mode="osu")
rank = user.rank_highest.rank
bio = f"{rank:,d}"

if rank % 10 == 1:
    bio += "st "
elif rank % 10 == 2:
    bio += "nd "
elif rank % 10 == 3:
    bio += "rd "
else:
    bio += "th "

bio += "best circle clicker\n2nd best in RSS\n(updated by ORIIBU)"

cl.account_edit(biography=bio)
