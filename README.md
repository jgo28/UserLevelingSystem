# User Leveling System

This package creates a leveling system that monitors and grants users experience
points based on the number of message they send in a server. This package is
meant to be used in conjunction with Discord and a Discord bot. In particular,
it is for bots made with the discord.py library.
Currently, it uses a MySQL database to keep track of user progress.

## Starting the MySQL database

This is more for me to remember.

```
sudo service mysql start
mysql -uroot -p
sudo service mysql stop
```