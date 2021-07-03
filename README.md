# plexmagics
![commit](https://img.shields.io/github/last-commit/renanfernandes/plexmagics)

A Collection of tools to automate my [Plex](http://www.plex.tv) and [Deluge](https://deluge-torrent.org) setup.

**Author**: Renan Mathias Fernandes ![twitter](https://img.shields.io/twitter/follow/renanmf?style=social)

## Table of Contents
1. [Table of Contents](#table-of-contents)
2. [token](#token)
3. [pushover.py](#pushover.py)
4. [torrentCompleted.py](#torrentcompleted.py)
## token
Text file containing the token information to be used by Pushover using the following format:
```
e2fdspi5390kfeiopdit043-ordew0
fdjsifjoidsqjr3209ruife90sdaff
```
1st line: token, 2nd line: user

## pushover.py
Simple script to send push notifications via [Pushover API](http://pushover.net)

## torrentCompleted.py
Called by Deluge's Execute plugin when a torrent completes
