# Basic User Leveling System

This package creates a basic leveling system that monitors and grants users experience
points based on the number of message they send in a server. This package is
meant to be used in conjunction with Discord and a Discord bot. In particular,
it is for bots made with the **discord.py** library.

By default, it uses a MySQL database to keep track of user progress.

## Running

Install the requirements in `requirements.txt`. The main commands that will be
used are in `/utils/levels.py`. To use it with a Discord bot, set the `msg_sent()`
function to activate whenever a user sends a message through the Discord channel.

The `script.py` file provides an example of how functions may be used to interact
with the database and modify its' attributes.

## Modifying Level Progression

Everything to modify how the level progression works throughout the system can
be found in `/utils/levels.py`. Here are some of the attributes that can be
modified:

* exp_mod - modifies the amount of experience rewarded in the system per message.
* exp_gain - experience points gained per message
* msg_list - an array where each element is the number of messages required
to progress to the next level.

There are others that can be modified as well if you desire.

## Connecting to the Database

You'll need to create a `.env` file in the following format:

```
# .env
USERNAME=your_username
PASSWORD=your_password
DATABASE=name_of_your_database
HOST=how_you're_hosting_the_database
```

Then you'll need to install `python-dotenv` through pip.

## Starting the MySQL database

This is more for me to remember.

```
sudo service mysql start
mysql -u root -p
sudo service mysql stop
```
