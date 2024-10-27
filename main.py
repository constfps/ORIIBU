from ossapi import Ossapi
import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = os.getenv("USER_ID")
api = Ossapi(client_id, client_secret)

user = api.user(user_id, mode="osu")
print(user.rank_highest.rank)
