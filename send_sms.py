from twilio.rest import TwilioRestClient
import requests
import json
import time
from datetime import datetime

url1 = 'http://cricapi.com/api/matches'
payload1 = {
	'apikey' : 'xxxxxxxxxxxxxxxxxxxxxx'
}
request1 = requests.post(url1, params = payload1)
data1 = json.loads(request1.text)
for d in data1['matches']:
	print d['team-1'] + ' vs ' + d['team-2']
	print '>>>>>>unique_id : ' + str(d['unique_id'])
	print '\n'
choice = raw_input('Enter the unique_id of the match\n')
choice = int(choice)

for d in data1['matches']:
	if d['unique_id'] == choice:
		selectedMatch = d

# Ball by ball api
iterations = 0
while( iterations < 1000 ):
	url = 'http://cricapi.com/api/cricketScore'
	payload = {
		'apikey' : 'xxxxxxxxxxxxxxxxxxxxxxx',
		'unique_id' : selectedMatch['unique_id']
	}

	r = requests.get(url, params = payload)
	data = json.loads(r.text)
	print data['team-1']
	print data['team-2']
	print data['score']

	account_sid = "xxxxxxxxxxxxxxxxxxxxxxx"
	auth_token = "xxxxxxxxxxxxxxxxxxxxxxx"
	client = TwilioRestClient(account_sid, auth_token)
	msg = ">Match Status : " + data['team-1'] + ' vs ' + data['team-2'] + '\n' + data['score']

	message = client.messages.create(to="xxxxxxxxxx", from_="xxxxxxxxx",
	                                     body=msg)

	print 'Sending message....' + str(datetime.now()) 
	print message.sid
	time.sleep(45)
