# Work with Python 3.6
import discord
from discord.ext import commands
import json
import requests

url = requests.get('https://db.ygoprodeck.com/api/v5/cardinfo.php?name=' + cardID)

print(url.json)
