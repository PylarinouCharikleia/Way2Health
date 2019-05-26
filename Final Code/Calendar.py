import datetime
import calendarModule
from Viewcalendar import *
import random
import time
from User import *

class Event:
	def __init__(self, evType, color, title, description, date):
		self.evType = evType
		self.color = color
		self.title = title
		self.description = description
		self.date = date

	def set_evType(self,in_evType):
		self.evType =  in_evType

	def set_color(self,in_color):
		self.color = in_color

	def set_title(self,in_title):
		self.title = in_title

	def set_descr(self,in_descr):
		self.description = in_descr

	def set_date(self,in_date):
		self.date = in_date

	def get_evType(self):
		return self.evType

	def get_color(self):
		return self.color

	def get_title(self):
		return self.title

	def get_descr(self):
		return self.description

	def get_date(self):
		return self.date

	def printEventData(self):
		print("Title: ", self.title)
		print("Event Type: ", self.evType)
		print("Color:", self.color)
		print("Description: ", self.description)
		print("Date: ", self.date)


class Period(Event):
	def __init__(self,dayType, pregracyChance, evType, color, title, description, date):
		Event.__init__(self, evType, color, title, description, date)
		self.dayType = dayType
		self.pregnancyChance = pregracyChance

	def set_dayType(self, in_dayType):
		self.dayType = in_dayType

	def set_pregracyChance(self, in_pregChance):
		self.pregnancyChance = in_pregChance;

	def get_dayType(self):
		return self.dayType

	def get_pregracyChance(self):
		return self.pregracyChance

	def printEventData(self):
		print("|	Title: ", self.title)
		print("|	Event Type: ", self.evType)
		print("|	Color:", self.color)
		print("|	Description: ", self.description)
		print("|	Date: ", self.date)
		print("|	Day Type: ", self.dayType)
		print("|	Pregnancy Chance:", self.pregnancyChance,"%")


class Dietary(Event):
	def __init__(self, foodSuggestion, evType, color, title, description, date):
		Event.__init__(self, evType, color, title, description, date)
		self.foodSuggestion = foodSuggestion

	def set_foodSuggestion(self, in_food):
		self.foodSuggestion = in_food

	def get_foodSuggestion(self):
		return self.foodSuggestion

	def printEventData(self):
		print("|	Title: ", self.title)
		print("|	Event Type: ", self.evType)
		print("|	Color:", self.color)
		print("|	Description: ", self.description)
		print("|	Date: ", self.date)
		print("|	Food Suggestion: ", self.foodSuggestion)


class Medication(Event):
	def __init__(self, time, name, quantity, evType, color, title, description, date):
		Event.__init__(self, evType, color, title, description, date)
		self.time = time
		self.name = name
		self.quantity = quantity

	def set_time(self, in_time):
		self.time = in_time

	def set_name(self,in_name):
		self.name = in_name

	def set_quantity(self, in_quantity):
		self.quantity = in_quantity

	def get_time(self):
		return self.time

	def get_name(self):
		return self.name

	def get_quantity(self):
		return self.quantity

	def printEventData(self):
		print("|	Title: ", self.title)
		print("|	Event Type: ", self.evType)
		print("|	Color:", self.color)
		print("|	Description: ", self.description)
		print("|	Date: ", self.date)
		print("|	Time: ", self.time)
		print("|	Name: ", self.name)
		print("|	Quantity", self.quantity)


class ExerciseEvent(Event):
	def __init__(self, muscleslist, exType, evType, color, title, description, date):
		Event.__init__(self, evType, color, title, description, date)
		self.muscleslist = muscleslist
		self.exType = exType

	def set_exType(self, in_exType):
		self.exType = in_exType

	def set_muscleslist(self, in_muscles):
		self.muscleslist = in_muscles

	def get_exType(self):
		return self.exType

	def get_muscleslist(self):
		return self.muscleslist

	def printEventData(self):
		print("|	Title: ", self.title)
		print("|	Event Type: ", self.evType)
		print("|	Color:", self.color)
		print("|	Description: ", self.description)
		print("|	Date: ", self.date)
		for m in self.muscleslist:
			if len(m) > 1:
				print("|	Muscle: ", m)
		print("|	Exercise Type: ", self.exType)


class Examination(Event):
	def __init__(self, conditions, lab, evType, color, title, description, date):
		Event.__init__(self, evType, color, title, description, date)
		self.conditions = conditions
		self.lab = lab

	def set_conditions(self, in_cond):
		self.conditions = in_cond

	def set_lab(self, in_lab):
		self.lab = in_lab

	def get_conditions(self):
		return self.conditions

	def get_lab(self):
		return self.lab

	def printEventData(self):

		print("|	Title: ", self.title)
		print("|	Event Type: ", self.evType)
		print("|	Color:", self.color)
		print("|	Description: ", self.description)
		print("|	Date: ", self.date)

		for m in self.conditions:
			if len(m) > 1:
				print("|	Conditions: ", m)
		print("|	Lab: ", self.lab)


class Appointment(Event):
	def __init__(self, user, symptoms, appointOrderer, severity, evType, color, title, description, date):
		Event.__init__(self, evType, color, title, description, date)
		self.user = user
		self.symptoms = symptoms
		self.appointOrderer = appointOrderer
		self.severity = severity

	def set_user(self, in_user):
		self.user = in_user

	def set_symptoms(self, in_symp):
		self.symptoms = in_symp

	def set_appointOrderer(self, in_orderer):
		self.appointOrderer = in_orderer

	def set_severity(self, in_sev):
		self.severity = in_sev

	def get_user(self):
		return self.user

	def get_symptoms(self):
		return self.symptoms

	def get_appointOrderer(self):
		return self.appointOrderer

	def get_severity(self):
		return self.severity

	def printEventData(self):
		print("|	Title: ", self.title)
		print("|	Event Type: ", self.evType)
		print("|	Color:", self.color)
		print("|	Description: ", self.description)
		print("|	Date: ", self.date)

		print("|	User: ")
		printName(self.user)
		print("|	Orderer: ")
		printName(self.appointOrderer)
		print("|	Symptoms:")
		for m in self.symptoms:
			print(m)
		print("|	Severity:", self.severity)


class Calendar:

	def __init__(self, title, description, user):
		self.title = title
		self.description = description
		self.user = user
		self.listOfEvents = []
		self.textCalendar = calendarModule.TextCalendar()

	def set_title(self, in_title):
		self.title = in_title

	def set_descr(self, in_descr):
		self.description = in_descr

	def set_user(self, in_user):
		self.user = in_user

	def set_listOfEvents(self, in_list):
		self.listOfEvents = in_list

	def get_title(self):
		return self.title

	def get_descr(self):
		return self.description

	def get_user(self):
		return self.user

	def get_listOfEvents(self):
		return self.listOfEvents

	def loadDateData(self, date):
		templist = []
		for e in self.listOfEvents:
			if e.date == date:
				templist.append(e)
		#self.showDateData(templist)
		return templist



	def addEventToListOfEvents(self, event):
		self.listOfEvents.append(event)
		print(self.listOfEvents)
		return True
		
	def chooseEventType(self):
		choice = -1
		showEventMenu(self)

		while choice not in range(0,7):
			try:
				print("|                                                    |")
				choice = int(input("|	Enter Type Of Event: "))
				if choice not in range(0,7):
					print ("|				Not Valid Type Of Event				 |")
				if choice == 6 and self.user.gender == "male":
					print ("|	            Not Valid Type Of Event	             |")
					choice = -1
					
			except ValueError:
				print("|                                                    |")
				print ("|	               Invalid Input!	                |")
				continue

		print("|	You choose: ", eventTypes[choice])
		return choice

	def messageNotCompletedFields(self):
		print("|                                                    |")
		print("|Not All Fields are completed.Event cannot be created|")
		openCalendar(self)

	def addEvent(self, in_date):
		type = self.chooseEventType()
		in_evType = eventTypes[type]

		in_data = showForm(self)
		if not in_data:
			return 0
		else:
			in_color = in_data[0]
			in_title = in_data[1]
			in_description = in_data[2]


		if type == 0:
			new_event = Event(in_evType, in_color, in_title, in_description, in_date)

		elif type == 1:
			in_foodSuggestion = "default"
			new_event = Dietary(in_foodSuggestion,in_evType, in_color, in_title, in_description, in_date)
			print("|              Dietary Event Created                 |")

		elif type == 2:

			flag = 1
			while flag:
				try:
					in_hour = int(input("|	Enter Hour: "))
					in_min = int(input("|	Enter Minutes: "))
					flag = 0
				except ValueError:
					print("|                  Invalid Input                     |")
					flag = 1
					continue

			in_time = datetime.time(in_hour, in_min)
			in_name = input("|	Enter Name: ")

			flag = 1
			while flag:
				try:
					in_quantity = int(input("|	Enter quantity: "))
					flag = 0
				except ValueError:
					print("|                  Invalid Input                     |")
					flag = 1
					continue

			if checkDataFields([in_name, in_quantity]) == False:
				self.messageNotCompletedFields()

			new_event = Medication(in_time,in_name,in_quantity,in_evType, in_color, in_title, in_description, in_date)
			print("|             Medication Event Created               |")
			
			
		elif type == 3:
			in_muscleslist = []

			for e in range(1, len(exerciseTypes)):
				print(e, exerciseTypes[e])
			
			c_in_exType = -1
			
			while c_in_exType not in range(1, len(exerciseTypes)):
				try:
					c_in_exType = int(input("|	Choose type of exercise: "))
					if c_in_exType == 0:
						break
				except ValueError:
					print("|                  Invalid Input                     |")
					continue

			in_exType = exerciseTypes[c_in_exType]
			if checkDataFields([in_exType]) == False:
				self.messageNotCompletedFields()
				return 0

			try:
				num = int(input("|	Enter number of muscles: "))
			except ValueError:
				num = 0
				print("|            No muscles will be inserted             |")
				
			m = 0
			while m < num:
				tmp = input("|	Muscle: ")
				in_muscleslist.append(tmp)
				m = m + 1

			new_event = ExerciseEvent(in_muscleslist, in_exType, in_evType, in_color, in_title, in_description, in_date)
			print("|           ExerciseEvent Event Created              |")
			
		elif type == 4:
			in_conditions = []
			c_choice = True
			while c_choice == True:
				tempCond = input("|	Enter condition: ")
				if not tempCond:
					continue
				else:
					in_conditions.append(tempCond)
					cd = input("|	Do you want to enter more conditions? y/n?")
					if cd == "y":
						c_choice = True
					else:
						c_choice = False

				in_lab = input("|	Enter Lab's Name: ")

				if checkDataFields([in_lab]) == False:
					self.messageNotCompletedFields()
					return 0

			new_event = Examination(in_conditions, in_lab, in_evType, in_color, in_title, in_description, in_date)
			print("|             Examination Event Created              |")
		elif type == 5:

			in_appointOrderer = self.user
			m = 0
			if isinstance(self.user, Patient):
				if not self.user.listOfDoctors:
					print("|          		  No doctors Found         	        |")
					viewSelectedDate(self, in_date)
				else:
					print("|	Doctors:")
					for docs in self.user.listOfDoctors:
						print("|	Doctor", m, ":")
						printName(docs)
						m = m + 1

				choice = -1
				while choice not in range(0, len(self.user.listOfDoctors)):
					try:
						choice = int(input("|	Choose Doctor: "))
					except ValueError:
						print("|                  Invalid Input                     |")
						continue
				
				in_user = self.user.listOfDoctors[choice]

			elif isinstance(self.user, Doctor):
				print("|	Patients:")
				for pats in self.user.listOfPatients:
					print("|	Patient", m, ":")
					printName(pats)
					print("\n")
					m = m + 1

				choice = -1
				while choice not in range(0, len(self.user.listOfPatients)):
					try:
						choice = int(input("|	Choose Patient: "))
					except ValueError:
						print("|                  Invalid Input                     |")
						continue

				in_user = self.user.listOfPatients[choice]

			in_symptoms = []
			cd = input("|	Do you want to enter symptoms? y/n?")
			if cd == "y":
				c_choice = True
			else:
				c_choice = False

			while c_choice:
				tempSymp = input("|	Enter symptoms: ")
				if not tempSymp:
					continue
				else:
					in_symptoms.append(tempSymp)
			
				cd = input("|	Do you want to enter more symptoms? y/n?")
				if cd == "y":
					c_choice = True
				else:
					c_choice = False

			for s in range(1,len(severityOptions)):
				print(s, severityOptions[s])

			in_sev = -1;
			while in_sev not in range(1,len(severityOptions)):
				try:
					in_sev = int(input("|	Choose Severity Level: "))
					if in_sev == 0:
						break
				except ValueError:
					print("|                  Invalid Input                     |")
					continue

			in_severity = severityOptions[in_sev]


			new_event = Appointment(in_user, in_symptoms, in_appointOrderer, in_severity, in_evType, in_color, in_title, in_description, in_date)
			print("|            Appointment Event Created               |")
			
			
		elif type == 6:
			in_dayType = input("|	Enter Day Type: ")
			in_pregnancyChance = random.randint(0,100)

			new_event = Period(in_dayType,in_pregnancyChance,in_evType, in_color, in_title, in_description, in_date)
			print("|        	  Period Event Created                  |")

		else:
			print("|        	 Not Valid Type Of Event                |")

		ret = self.addEventToListOfEvents(new_event)

		if ret:
			print("|     	Event Successfully added to Calendar        |")
		else:
			print("|Error Occured During adding your new event to Calendar|")
		viewSelectedDate(self, in_date)

		return new_event