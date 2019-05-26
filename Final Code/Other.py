import datetime

class Message:
	def __init__(self,user,receiverUser,text,title,urgency):
		self.sender = user
		self.receiver =  receiverUser
		self.text = text
		self.urgency = urgency
		self.title = title
		self.date = datetime.datetime.now()
		self.status = 'Not Sent'