#!/usr/bin/env python3

# Triggered by Deluge Execute plugin when download completes
#

from syslog import syslog
import sys, subprocess


syslog('torrentCompleted: Initiating actions..')
torrentId = sys.argv[1]
torrentName = sys.argv[2]
torrentPath = sys.argv[3]
message = "Torrent : " + torrentName + " Successfully downloaded"

p = subprocess.Popen(["python3", "./pushover.py", message], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

syslog('torrentCompleted: lets detect all argvs sent by Deluge...')
syslog(sys.argvs)
#for arg in argv[1:]:
#    syslog(arg)
