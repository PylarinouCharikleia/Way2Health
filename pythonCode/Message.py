import datetime

class Message:
    def __init__(self, senderUser, receiverUser , text, urgency):
        self.sender = senderUser
        self.receiver =  receiverUser
        self.text = text
	self. urgency = urgency
        self.date = datetime.datetime.now()
        self.status = "Not Sent"
