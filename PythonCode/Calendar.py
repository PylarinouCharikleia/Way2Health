class Calendar:
	def __init__(self,title,description,user):
		self.title=title
		self.description=description
		self.user=user

	def loadDateData(date):
	def addEventToListOfEvents():

class Event:
	def __init__(self,evType,color,title,description,date):
		self.evType=evType
		self.color=color
		self.title=title
		self.description=description
		self.date=date

	def createEventObject():


class Period(Event):
	def __init__(self,dayType,pregracyChance,evType,color,title,description,date):
		Event.__init__(self,evType,color,title,description,date):
		self.dayType=dayType
		self.pragnacyChance=pregracyChance

class Dietary(Event):
	def __init__(self,foodSuggestion,evType,color,title,description,date):
		Event.__init__(self,evType,color,title,description,date):
		self.foodSuggestion=foodSuggestion

class Medication(Event):
	def __init__(self,time,name,quantity,evType,color,title,description,date):
		Event.__init__(self,evType,color,title,description,date):
		self.time=time
		self.name=name
		self.quantity=quantity

class ExerciseEvent(Event):
	def __init__(self,muscleslist,exType,evType,color,title,description,date):
		Event.__init__(self,evType,color,title,description,date):
		self.muscleslist
		self.exType=exType

class Examination(Event):
	def __init__(self,conditions,lab,evType,color,title,description,date):
		Event.__init__(self,evType,color,title,description,date):
		self.conditions=contitions
		self.lab=lab

class Appointment(Event):
	def __init__(self,user,symptoms,appointOrderer,severity,evType,color,title,description,date):
		Event.__init__(self,evType,color,title,description,date):
		self.user=user
		self.symptoms=symptoms
		self.appointOrderer=appointOrderer
		self.severity=severity