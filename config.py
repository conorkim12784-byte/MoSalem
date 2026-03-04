import json
import os

import requests
from database import get_db_general_rtb
from utils import get_restarted

# Super sudoers - مطور السورس الاساسي
super_sudoers = [1923931101]

####################################################################################

# Bot token
TOKEN = "5715894811:AAEdH_xnLRq1zoNMvZITgQSpJWn8pPjkb4k"

# Your API ID and Hash from https://my.telegram.org/apps
API_ID = 11966986
API_HASH = "53e499a620b4d132a8b0adb1015b04b5"

# Chat used for logs
log_chat = 1923931101

# Sudoers and super sudoers
sudoers = [1923931101]
sudoers += super_sudoers
developer = []
developer += sudoers

####################################################################################

def dev():
    lang = get_db_general_rtb("developer")
    lang2 = get_db_general_rtb("secdeveloper")
    if lang is None:
        print("No Developer")
    else:
        for row in lang:
            t = row[0]
            developer.append(t)
    if lang2 is None:
        print("No Second Devoloper")
    else:
        for row in lang2:
            t = row[0]
            developer.append(t)
    print(developer)


def get_bot_information():
    bot_inf = requests.get(
        "https://api.telegram.org/bot" + TOKEN + "/getme")
    bot_info = bot_inf.json()
    result = bot_info["result"]
    bot_id = result["id"]
    bot_username = result["username"]
    return bot_id, bot_username


#####################################################################################

# Prefixes for commands
prefix = ["/", "!"]

# List of disabled plugins
disabled_plugins = []

# API keys
TENOR_API_KEY = "2MAL8NKBOO01"

# Bot version
with open("version.txt") as f:
    version = f.read().strip()

# Run function
dev()
