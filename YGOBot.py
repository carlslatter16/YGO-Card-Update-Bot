#!/usr/bin/env python3

import requests, sys, discord
from discord.ext import commands

TOKEN = "XXXXXXXXXXXXXXXXX"
client = discord.Client()
localFile = "Saved_Cards.txt"

def scrapeCard(cardID):
    url = "https://db.ygoprodeck.com/api/v5/cardinfo.php?name=" + cardID
    imageUrl = "https://storage.googleapis.com/ygoprodeck.com/pics/" + cardID + ".jpg"
    cardData = requests.get(url).json()

    cardDict = {"id": cardID}

    cardDict["name"] = cardData[0]["name"]
    cardDict['imageUrl'] = imageUrl

    return cardDict


def addCards(cardID):
    f = open(localFile, "a")
    f.write(cardID + '\n')
    f.close()


def discordPush(newCardsList):
    @client.event
    async def on_ready():
        for server in client.guilds:
            for channel in server.channels:
                if channel.name == 'ygoupdates':
                    print("------------------------------------------------")
                    for newCardID in newCardsList:
                        embed = discord.Embed( title=scrapeCard(newCardID)['name'], description= + "Click Image If On Desktop", color=0xeee657)
                        embed.add_field(name="Link: ", value="https://db.ygoprodeck.com/card/?search=" + scrapeCard(newCardID)['name'], inline=False)
                        embed.set_thumbnail(url=scrapeCard(newCardID)["imageUrl"])
                        print("Card Found - " + scrapeCard(newCardID)['name'])
                        await channel.send(embed = embed)
                        addCards(newCardID)
                    print("------------------------------------------------")
                    print("New Cards Have Been Saved")
                    print("")
                    print("Updates Sent, Closing...")
                    print("")
                    sys.exit(1)
    client.run(TOKEN)
    return


def checkForNew():
    localSplitList = open(localFile,'r').read().split('\n')
    localCardList = []
    onlineCardList = []
    newCardsList = []
    apiIdResponce = requests.get("https://db.ygoprodeck.com/api/v5/cardinfo.php").json()

    print('Comparing Online Database With Cached Version...')

    for id in localSplitList:
        localCardList.append(id)

    for card in apiIdResponce:
        onlineCardList.append(card['id'])

    newCardsList = set(onlineCardList).difference(set(localCardList))

    if newCardsList:
        discordPush(newCardsList)
    else:
        print("No Updates, Closing..")
        print("")


def scriptInfo():

    print("")
    print("Python YGOProDeck Card Update Notifier")
    print("-------------------------------------")
    print("    By github.com/carlslatter16")
    print("=====================================")
    print("")

    checkForNew()

scriptInfo()
