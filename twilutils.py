import json
import httphelper
from twilio.rest import TwilioRestClient


class TwilioUtil(object):


	def __init__(self, sid, token):
		self.sid = sid
		self.token = token
		self.baseuri = 'https://api.twilio.com/2010-04-01'
		self.client = TwilioRestClient(sid, token)
	
	def avail(self, country='GB', contains=None):

		url = '%s/Accounts/%s/AvailablePhoneNumbers/%s/Local.json' % (self.baseuri, self.sid, country)

		client = TwilioRestClient(account_sid, auth_token)
 
		numbers = client.phone_numbers.search(
		    country=country,
		    contains=contains,
		    type="local")
		return uri

