from Diet import *
from Medicine import *
from Other import *
from MedicalExams import *

class User:
	def __init__(self, name, surname, email, phone, city, username, password, birth, gender):
		self.name = name
		self.surname = surname
		self.email = email
		self.phone = phone
		self.city = city
		self.username = username
		self.password = password
		self.birth=birth
		self.gender=gender
		self.listOfMessages=[]
	#1. Message Functions	
	def addTitle(self, receiver):
		title = input('Enter Here The Title: ')
		self.addUrgency(receiver, title)

	def addUrgency(self, receiver, title):
		urgency = input('Is Your Message Urgent (yes/no): ')
		while (urgency != 'yes' and urgency != 'no'):
			urgency = input('Please Give a Valid Value (yes/no): ')
		self.addMessage(receiver, title, urgency)

	def addMessage(self, receiver, title, urgency):
		text = input('Enter Here Your Message: ')
		self.messageLength(text, receiver, title, urgency)

	def codeMessage(self, message, receiver, title, urgency):
		mes = Message(receiver, '', title, urgency)
		result = []
		for letter in message:
			l = ord(letter) - 20
			result.append(l)
		print('Encoded Message: ' + str(result))
		self.sendMessage(receiver, result, mes)

	def messageLength(self, message, receiver, title, urgency):
		length = len(message.split())
		print('Length: ' + str(length))
		if length < 200:
			self.codeMessage(message, receiver, title, urgency)
		else:
			self.messageError(receiver, title, urgency)

	def sendMessage(self, receiver, message, mes):
		receiver.listOfMessages.append(mes)
		self.decodeMessage(message, mes)

	def decodeMessage(self, message, mes):
		end_string = ""
		for numbers in message:
			l = int(numbers)
			l = l + 20
			l = chr(l)
			end_string = end_string + l
			mes.text = end_string
		print('Decoded Message: ' + end_string)
		self.updateInboxReceiver(mes)

	def updateInboxReceiver(self, mes):
		self.sentMessage(mes)

	def sentMessage(self, message):
		message.status = 'sent'
		print("Your Message was sent")

	def messageError(self, receiver, title, urgency):
		print("Your message should not contain more than 200 words")
		self.addMessage(receiver, title, urgency)
		
	def printEmptyLines(emptyLines):
		for i in range(emptyLines):
			print ("|                                                    |")
	
	def printBorder():
		print("======================================================")#footer		
	
	#def addRegistration():

class Doctor(User):
	def __init__(self, name, surname, email, phone, city, username, password,birth, gender, specialization, rank,cv,listOfDiplomas):
		User.__init__(self, name, surname, email, phone, city, username, password,birth, gender)
		self.specialization = specialization
		self.listOfPatients = []
		self.rank = rank
		self.numOfPatients=0
		self.cv=cv
		self.listOfDiplomas=listOfDiplomas
	

	#1. Message Functions	

	def selectReceiver(self):
		found = 0
		print('The Available Patients are: ')
		for Patient in self.listOfPatients:
			print('	' + Patient.surname + '  ' + Patient.name)
		surname = input('Give the surname of the Patient: ')
		name = input('Give the name of the Patient: ')
		for Patient in self.listOfPatients:
			if Patient.surname == surname and Patient.name == name:
				receiver = Patient
				found = 1
		if found == 1:
			self.addTitle(receiver)
		else:
			print('Patient not found')
			print()
			print()
			self.selectReceiver()

	#2. Notification Functions			
	
	def completeNotification(self):
		notif = input("Notification: ")
		pat_surname = input("Patient's surname: ")
		self.sendNotification(notif, pat_surname)

	def sendNotification(self, notification, pat_surname):
		for Patient in self.listOfPatients:
			if Patient.surname == pat_surname:
				pat = Patient
				pat.listOfNotifications.append(notification)
				print(pat.listOfNotifications)

	def notif_success(self):
		print("Notification sent.")

	def notif_fail(self):
		print("Notification failed.")

	def messagePatientNotFound(self):
		print("PATIENT NOT FOUND")

	def addPatientToListOfPatients(self, patient):
		self.listOfPatients.append(patient)

	def searchPatient(self, fullname):
		templist = []
		if not fullname[1]:
			fullname[1] = ""

		if not fullname[0]:
			fullname[0] = ""

		for p in self.listOfPatients:
			if p.surname == fullname[1] or p.name == fullname[0]:
				templist.append(p)

		if not templist:
			self.messagePatientNotFound()
			return []
		else:
			return templist



class Patient(User):
	
	def __init__(self, name, surname, email, phone, city, birth, username, password, gender, weight, height,id):
		User.__init__(self, name, surname, email, phone, city, username, password, birth, gender)
		self.weight=weight
		self.height=height
		self.id=id
		self.listOfDoctors= []
		self.listOfNotifications = []

	#def insertData():
	#def dataOptions():
	
	#1. Message Functions
	def selectReceiver(self):
		found = 0
		print('The Available Doctors are: ')
		for Doctor in self.listOfDoctors:
			print('	' + Doctor.surname + '  ' + Doctor.name)
		surname = input('Give the surname of the Doctor ')
		name = input('Give the name of the Doctor ')
		for Doctor in self.listOfDoctors:
			if Doctor.surname == surname and Doctor.name == name:
				receiver = Doctor
				found = 1
		if found == 1:
			self.addTitle(receiver)
		else:
			print('Doctor not found')
			print()
			print()
			self.selectReceiver()
	
	
	#2. Insertion Functions
	def check_choice(self, choice):

		if choice == "Diet":
			self.insert_diet()
		elif choice == "Exercise":
			self.insert_exercise()
		elif choice == "Medicne":
			self.insert_medicine()
		elif choice == "Medical Report":
			self.insert_medical_report()

	def insert_diet(self):
		
		print("===================Diet Insertion=====================")#header
		User.printEmptyLines(3)
		
		print ("|         Insert your diet input information:        |")
		User.printEmptyLines(3)
		
		diet = input("|      Diet: ")
		User.printEmptyLines(3)
		
		flag=0
		
		quantity = input("|      Quantity: ")
		while flag==0:
			try:
				quantity = int(quantity)
				flag = 1
			except ValueError:
				print("|That's not a valid input!Please reinsert this field |")
				quantity = input("|      Quantity: ")
		User.printEmptyLines(3)

		
		tempDiet = self.create_diet(diet.lower(), int(quantity))
		return tempDiet

	def create_diet(self, name, quantity):
		newDiet = Diet(name, quantity)
		newDiet.setID(self.id)

		return newDiet
		
		
	def insert_medical_report(self):
		type = input("Enter exams type (metabolism/heart/urinary/liver/vitamins/thyroid/immune/generalBlood)")
		type.lower()
		
		while (type != "metabolism" and type != "heart" and type != "urinary" and type != "liver" and type != "vitamins" and type != "thyroid" and type != "immune" and type != "generalblood"):
			type = input("Please enter correct type of exams (metabolism/heart/urinary/liver/vitamins/thyroid/immune/generalBlood)")
			type.lower()			
				
		tempExam = self.create_medical_report(type)				
		
	def create_medical_report(self,name):

		newExam = {
		        "metabolism": Metabolism(name),
        		"heart": Heart(name),
			"urinary": UrinarySystem(name),
			"liver": Liver(name),
			"vitamins": Vitamins(name),
			"thyroid": Thyroid(name),
			"immune": ImmuneSystem(name),
			"generalblood": GeneralBloodTest(name)
    		}[name] 

		newExam.setID(self.id)
		return newExam
		
		
	def insert_medicine(self):
		
		print("==================Medicine Insertion==================")#header
		User.printEmptyLines(3)
		
		print ("|       Insert your medicine input information:      |")
		User.printEmptyLines(5)
		
		medicine = input("|      Medicine: ")
		User.printEmptyLines(3)
		
		flag=0
		dosage = input("|      Dosage: ")
		while flag==0:
			try:
				dosage = int(dosage)
				flag = 1
			except ValueError:
				print("|That's not a valid input!Please reinsert this field |")
				dosage = input("|      Dosage: ")
		User.printEmptyLines(5)
	
		tempMedicine = self.create_medicine(medicine.lower(), float(dosage))
		tempMedicine.setID(self.id)
	
		return tempMedicine
		
	def create_medicine(self, name, dosage):
		newMedicine = Medicine(name, dosage)
		#Database.insertMedicine(newMedicine)
		return newMedicine

	def getID(self):
		return self.id
		
	def getName(self):
		return self.name
	
	def getSurname(self):
		return self.surname
	
	def getGender(self):
		return self.gender
	
	def getDateOfBirth(self):
		return self.birth
	
	def getHeight(self):
		return self.height
	
	def getWeight(self):
		return self.weight		

	#print(doc.name)
	#pat = patientRegistration()
	#pat.check_choice("Diet")