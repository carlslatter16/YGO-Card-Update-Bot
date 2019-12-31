# YGO Card Update Discord Bot
 A bot written in python3 to alert users of new cards released
 
 Module Requirements
 Discord.py (sudo pip -m install discord.py)
 Requests.py (sudo pip -m install requests.py)
 
 Usage:
 You must generate a cardID list using the given script
 You must input your own token to use, this is the token relating to your discord bot
 The discord bot must be added to the server you wish to use the script on
 You can test card updates by removing an ID from the generated list and then running the main bot
 The bot requires there be a 'ygoupdates' channel in the given discord server
 The script will either handle new cards and then exit or exit if no changes are found
 
 source env/bin/activate (Python Virtual Environment)
 python3 makeCardList.py (Card List Generation)
 python3 YGOBot.py (Notifier)

 The script runs and then closes; you may want to add scheduling, Windows Task Scheduler or a Linux cron job


 Note: Currently updates are only given in a server channel, I may add private message support in future
 
 IMPORTANT: There are times when the script may fail, it makes use of both the YGODeck & Discord API services and such is at the mercy of their uptime. Rerun as needed.
