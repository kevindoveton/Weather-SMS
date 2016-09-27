import requests, json

consumerKey = '########################'
consumerSecret = '####################'

# Get an access token from telstra
def getToken():
	url = 'https://api.telstra.com/v1/oauth/token'

	headers = {
		"Content-Type" : "application/x-www-form-urlencoded"
	}

	data = {
		'client_id' : consumerKey,
		'client_secret' : consumerSecret,
		'grant_type' : 'client_credentials',
		'scope' : 'SMS'
	}

	# Send the request
	token = requests.post(url, headers=headers, data=data)
	
	# return the token received
	return token.json()['access_token']


# send an sms
def sendSMS(number, message, accessToken):
	url = 'https://api.telstra.com/v1/sms/messages'

	headers = {
		"Content-Type" : "application/json",
		"Authorization" : "Bearer " + accessToken
	}

	data = {
		'to' : number,
		'body' : message
	}

	message = requests.post(url, headers=headers, data=json.dumps(data))
	
	# return the message id
	return message
