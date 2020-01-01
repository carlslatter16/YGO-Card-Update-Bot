#!/usr/bin/env python3

import requests, os, json
localFile = "Saved_Cards.txt"


onlineCardList = []
apiIdResponce = requests.get("https://db.ygoprodeck.com/api/v5/cardinfo.php").json()


print("")
print("Python YGOProDeck CardID Downloader")
print("-------------------------------------")
print("    By github.com/carlslatter16")
print("=====================================")
print("")

print("Getting Online CardID List...")
for card in apiIdResponce:
    onlineCardList.append(card['id'])

print("Writing Found IDs To Local File...")
print("")

if os.path.exists(localFile):
    try:
        os.remove(localFile)
    except:
        print("Cannot Remove Existing List, You May Have To Do This Manually And Run Again")
        exit()

f = open(localFile, "w")

for id in onlineCardList:
    f.write(id + '\n')

f.close()

print("Complete - Your Cardlist Should Now Be Up To Date")
print("")

exit()
