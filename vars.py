#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = os.environ.get("API_ID", "24473318")
    API_HASH = os.environ.get("API_HASH", "e7dd0576c5ac0ff8f90971d6bb04c8f5")
OWNER = int(environ.get("OWNER", "7841292070"))
CREDIT = "𝄟⃝‌🐬🇳‌ɪᴋʜɪʟ𝄟⃝🐬"
AUTH_USER = os.environ.get('AUTH_USERS', '7841292070,-1002624447857,-1002260543763,-1002501547365,-1002578436500,-1002780494901,-1002487629618, -1004958526346').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
