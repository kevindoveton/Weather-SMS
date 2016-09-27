mobileNumber = '##########'
wundergroundApiKey = '################'

import requests, TelstraSMS as sms

# Get the weather for Adelaide, South Australia from wunderground as JSON
a=requests.get('http://api.wunderground.com/api/'+wundergroundApiKey+'/forecast/q/Australia/Adelaide.json').json()

# create a text message limited to 160 characters 
text = a['forecast']['txt_forecast']['forecastday'][0]['fcttext_metric'][0:160]

# Send the message
sms.sendSMS(mobileNumber, text, sms.getToken())
