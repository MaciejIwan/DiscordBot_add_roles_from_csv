# Discord BOT
Application has been made to mass role assignment on a discord server from a .csv file. .csv.
Notice that bot is not safe, everyone could call commands, bot should be turn off after operation or improved.

## IDE
Program written using PyCharm.
## Bot command
* ```$hello``` - to check whether bot is working
* ```$install``` - trigger assignment proccess


## Requirements 
All dependencies are included in requirements.txt. You can install it using pip, or let PyCharm detect
```
$ pip install -r requirements.txt
```

## Get started
1. Prepere your .csv file. It should contain coulmn with ROLE_NAME (same as discord) and id's of users
2. Download repository, unpack and go to project folder
3. Copy .env.example file and remove .example postfix
4. Adjust .env fields with your data
   * DISCORD_TOKEN your private token from https://discord.com/developers/applications
   * FILENAME - file should be in same folder as example.csv
   * ROLE_NAME_COLUMN - Indexing start from 0.  
   * USER_ID_COLUMN=4 - Indexing start from 0.
5. Run app using python ```python3 main.py``` or  ```python src/main.py```
6. Add bot to your discord server
7. Check bot by sending  ```$hello``` on discord channel
8. Run assignment proccess using ```$install ``` on discord channel
        

