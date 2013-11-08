import json


class TwilioUtil(object):

	def __init__(self, auth, sid):
		self.auth = auth
		self.sid = sid
		