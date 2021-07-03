#!/usr/bin/env python3

# Triggered by Deluge Execute plugin when download completes
#

from syslog import syslog
import sys, subprocess


syslog('torrentCompleted: Initiating actions..')
torrentId = sys.argv[1]
torrentName = sys.argv[2]
p = subprocess.Popen(["python3", "./pushover.py", torrentId+torrentName], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
