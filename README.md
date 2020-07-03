# User Leveling System

This package creates a leveling system that monitors and grants users experience
points based on the number of message they send in a server. This package is
meant to be used in conjunction with Discord and a Discord bot. In particular,
it is for bots made with the discord.py library.
Currently, it uses a MySQL database to keep track of user progress.

## Connecting to the Database

You'll need to create a `.env` file in the following format:

```
# .env
USERNAME=your_username
PASSWORD=your_password
DATABASE=name_of_your_database
HOST=how_you're_hosting_the_database
```

Then you'll need to install `python-dotenv`.

## Starting the MySQL database

This is more for me to remember.

```
sudo service mysql start
mysql -u root -p
sudo service mysql stop
```
