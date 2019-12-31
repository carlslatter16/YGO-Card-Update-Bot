import requests
import json

onlineCardList = []
apiIdResponce = requests.get("https://db.ygoprodeck.com/api/v5/cardinfo.php").json()
f = open("Saved_Cards.txt", "w")

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

for id in onlineCardList:
    f.write(id + '\n')

f.close()

print("Complete - Your Cardlist Should Now Be Up To Date")
print("")

exit()
