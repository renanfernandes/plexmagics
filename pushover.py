# Sends a message via pushover
# Requires: token file and takes message as parameter
#
# token file:
#        1st line: token
#        2nd line: user

import http.client, urllib, sys

message = sys.argv[1]

f = open('token')
token = f.readline().rstrip('\n')
user = f.readline().rstrip('\n')

conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": token,
    "user": user,
    "message": message,
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
