# YGO Card Update Discord Bot
 A bot written in python3 to alert users of new cards released.
 
 ## Usage Notes:
 
* You must generate a cardID list using the given script
* You must input your own token to use, this is the token relating to your discord bot
* The discord bot must be added to the server you wish to use the script on
* You can test card updates by removing an ID from the generated list and then running the main bot
* The bot requires there be a 'ygoupdates' channel in the given discord server
* The script will either handle new cards and then exit or exit if no changes are found
* The script runs and then closes; you may want to add scheduling in the form of Windows Task Scheduler or a Linux cron job
 
 
 ## Usage Commands:
 * source env/bin/activate (Python Virtual Environment)
 * python3 makeCardList.py (Card List Generation)
 * python3 YGOBot.py (Notifier)


 ## Prerequisites
 * Python3 (sudo apt-get install python3)
 * pip (sudo apt install python3-pip)
 * Discord.py (python3 -m pip install -U discord.py)
 * Requests.py (python3 -m pip install -U requests.py)
 

 ## Notice: 
 There are times when the script may fail, it makes use of both the YGODeck & Discord API services and such is at the mercy of their uptime. Rerun as needed.
 
 
 ## To-Do: 
 * Private Message Support
 * API Status Error Checking


 ## Built With:

 * [Python3](https://docs.python.org/3.6/) - The Language Used
 * [YGOPRODECK API](https://db.ygoprodeck.com/api-guide/) - The Data Source From JSON
 * [Discord.py API](https://discordpy.readthedocs.io/en/latest/) - The Communication Medium


## Authors:

* **Carl Slatter** - *Creation* - [Carlslatter16](https://github.com/carlslatter16)
