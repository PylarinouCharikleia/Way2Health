from datetime import date

class Medicine:
	def __init__(self,name,dose):
		self.name=name
		self.dose=dose
		
	def setMedicine(self,type,activeIngredient,maxDose,sideEffects,reactList):
		self.type=type
		self.activeIngredient=activeIngredient
		self.maxDose=maxDose
		self.sideEffects=sideEffects
		self.reactList=reactList
		#self.getMedicine()
		
	def getMedicine(self):
		print(self.type)
		print(self.activeIngredient)
		print(self.dose)
		print(self.maxDose)
		print(self.sideEffects)
		print(self.reactList)
		
	def setID(self,id):
		self.id = id
	
	def getID(self):
		return self.id
		
	def getName(self):
		return self.name
		
	def getDose(self):
		return self.dose

class MedicationReport:
	
	def __init__(self,date):
		self.date=date
		
	def setMedicationReport(self,case,id,medicine):
	# Method that sets the medicineReport instances attributes with values
		
		if (case == "new"):	
			
			##if the medicineReport is new set its ID
			self.setID(id)
			
			##attributes initialization 			
			self.statin=0
			self.esomeprazole=0
			self.antiplatelet=0
			self.aripiprazole=0
			self.montelukast=0
			self.antipsychotic=0
			self.antifungal=0

			self.listOfActiveIngredients=[]
			self.listOfSideEffects=[]
			self.listOfReactants=[]
			self.listOfReacts=[]
			self.listOfMaxDose=[]

			self.medicationReportMessage=[]
			self.medicationReportCode=[]

		##count the amount of medicine insertions types
		if   (medicine.type=="Statin"):
			self.statin = 1 * medicine.dose + self.statin
		
		elif (medicine.type=="Esomeprazole"):
			self.esomeprazole = medicine.dose + self.esomeprazole
		
		elif (medicine.type=="Antiplatelet"):
			self.antiplatelet = medicine.dose + self.antiplatelet
		
		elif (medicine.type=="Aripiprazole"):
			self.aripiprazole = medicine.dose + self.aripiprazole
		
		elif (medicine.type=="Montelukast"):
			self.montelukast = medicine.dose + self.montelukast
		
		elif (medicine.type=="Antipsychotic"):
			self.antipsychotic = medicine.dose + self.antipsychotic
		
		elif (medicine.type=="Antifungal"):
			self.antifungal = medicine.dose + self.antifungal
			
		##set medicine stats
		self.listOfActiveIngredients.append(medicine.activeIngredient)
		self.listOfMaxDose.append(medicine.maxDose)
		
		self.setSideEffects(medicine.sideEffects)
		self.setReacts(medicine.reactList)
		
		##self.getAll()
		self.checkReport()
		
		
	def setSideEffects(self,sideEffects):
	# Method that parses and sets side effects from the side effects string of the medicine instance
		
		if sideEffects!="No":
			tempListOfSideEffects = sideEffects.split(',')
		
			for i in range (len(tempListOfSideEffects)):
				tempSideEffect = tempListOfSideEffects[i]
				
				if (tempSideEffect=="AllergicReaction"):
					
					flag = self.checkList("AllergicReaction",self.listOfSideEffects) 
					
					if flag==0:
						self.listOfSideEffects.append("AllergicReaction")
				
				if (tempSideEffect=="Constipation"):
					
					flag = self.checkList("Constipation",self.listOfSideEffects) 
					
					if flag==0:
					
						self.listOfSideEffects.append("Constipation")
				
				if (tempSideEffect=="Dizziness"):
					
					flag = self.checkList("Dizziness",self.listOfSideEffects) 
					
					if flag==0:
						self.listOfSideEffects.append("Dizziness")
				
				if (tempSideEffect=="DryMouth"):
					
					flag = self.checkList("DryMouth",self.listOfSideEffects) 
					
					if flag==0:
						self.listOfSideEffects.append("DryMouth")
						
				if (tempSideEffect=="Fatigue"):
					
					flag = self.checkList("Fatigue",self.listOfSideEffects) 
					
					if flag==0:
					
						self.listOfSideEffects.append("Fatigue")
						
				if (tempSideEffect=="Headache"):
				
					flag = self.checkList("Headache",self.listOfSideEffects) 
					
					if flag==0:
						
						self.listOfSideEffects.append("Headache")
					
				
				if (tempSideEffect=="OrthostaticHypotension"):
					
					flag = self.checkList("OrthostaticHypotension",self.listOfSideEffects) 
					
					if flag==0:
						self.listOfSideEffects.append("OrthostaticHypotension")
						
				if (tempSideEffect=="ReducedNutrientsAbsorption"):
					
					flag = self.checkList("ReducedNutrientsAbsorption",self.listOfSideEffects) 
					
					if flag==0:
						
						self.listOfSideEffects.append("ReducedNutrientsAbsorption")
						
				if (tempSideEffect=="Tiredness"):
					
					flag = self.checkList("Tiredness",self.listOfSideEffects) 
					
					if flag==0:
						self.listOfSideEffects.append("Tiredness")

					
	def checkList(self,searchTerm,list):
	# Check a list for an item 
		
		flag = 0
		for i in range (len(list)):
			if list[i] == searchTerm:
				flag=1
				
		return flag 
					
					
	def setReacts(self,reactList):
	# Method that parses and sets electrolytes from the electrolytes string of the medicine instance
		
		if reactList!="No":
			tempListOfReacts = reactList.split(',')	
			
			for i in range(len(tempListOfReacts)):

				tempReactant = tempListOfReacts[i].split(':')[0]
				tempReact = tempListOfReacts[i].split(':')[1]

				self.listOfReactants.append(tempReactant)
				self.listOfReacts.append(tempReact)
		
		elif reactList=="No":
		
			self.listOfReactants.append("No")
			self.listOfReacts.append("No")
		


	def checkReport(self):
	# Method that creates the medicine report status 
	
		#0. Variables
		tempMessage=[]
		tempCode = []
	
		tempListOfActiveIngredients=self.listOfActiveIngredients
		tempListOfSideEffects=self.listOfSideEffects
	
		#1. Check for each active ingredients
		
		for i in range(len(tempListOfActiveIngredients)):
		
			##a. Get category of the active ingredient
			tempActiveIngredient = tempListOfActiveIngredients[i]
			tempCategory = self.activeIngredientToCategory(tempListOfActiveIngredients[i]) 
			
			##b. Check Dose

			if tempCategory > self.listOfMaxDose[i]:
				tempMessage.append("You exceeded the max dose of {0} which is {1}mg!".format(tempActiveIngredient,self.listOfMaxDose[i]))
		

			##c. Check Reacts
			
			if self.listOfReacts[i]!="No":
				
				### Get if the reacting active ingredient was inserted
				reactantExists = self.checkList(self.listOfReactants[i],self.listOfActiveIngredients)
				
				### If the reacting active ingredient is inserted
				if reactantExists==True:
					
					if self.listOfReacts[i]=="Arrythmia":
						
						#### check if code already has code 7
						inserted = self.checkList(7,tempCode)
						
						if inserted == 0:
							tempCode.append(7)
							tempMessage.append("Warning,{0} reacts with {1} with this side effect {2}!".format(tempActiveIngredient,self.listOfReactants[i],self.listOfReacts[i]))
							
					elif self.listOfReacts[i]=="Bleeding":
					
						#### check if code already has code 6
						inserted = self.checkList(6,tempCode)
						
						if inserted == 0:
							tempCode.append(6)
							tempMessage.append("Warning,{0} reacts with {1} with this side effect {2}!".format(tempActiveIngredient,self.listOfReactants[i],self.listOfReacts[i]))
		
		
		#2. Check Side Effects 
		
		inserted = 0
		
		for i in range(len(tempListOfSideEffects)):
		
			tempSideEffect = tempListOfSideEffects[i]
		
			if (tempSideEffect=="AllergicReaction"):
				
				## check if code already has code 1
						inserted = self.checkList(1,tempCode)
						
						if inserted == 0:
							tempCode.append(1)
				
				
			elif (tempSideEffect=="Constipation"):
				
				## check if code already has code 2
						inserted = self.checkList(2,tempCode)
						
						
						if inserted == 0:
							
							tempCode.append(2)
					
				
			elif (tempSideEffect=="Dizziness"):
				
				## check if code already has code 3
						inserted = self.checkList(3,tempCode)
						
						if inserted == 0:
							
							tempCode.append(3)
					
				
			elif (tempSideEffect=="DryMouth"):
				
				## check if code already has code 4
						inserted = self.checkList(4,tempCode)
						
						if inserted == 0:
							tempCode.append(4)
						
			elif (tempSideEffect=="Fatigue"):
				
				## check if code already has code 3
						inserted = self.checkList(3,tempCode)
						
						if inserted == 0:
							
							tempCode.append(3)
					
						
			elif (tempSideEffect=="Headache"):
				
				## check if code already has code 3
						inserted = self.checkList(3,tempCode)
						
						if inserted == 0:
							
							tempCode.append(3)
					
					
			elif (tempSideEffect=="OrthostaticHypotension"):
				
				## check if code already has code 3
						inserted = self.checkList(3,tempCode)
						
						if inserted == 0:
							
							tempCode.append(3)
					
						
			elif (tempSideEffect=="ReducedNutrientsAbsorption"):
				
				## check if code already has code 5
						inserted = self.checkList(5,tempCode)
						
						if inserted == 0:
							
							tempCode.append(5)	
					
			
			elif (tempSideEffect=="Tiredness"):
					
				## check if code already has code 3
						inserted = self.checkList(3,tempCode)

						if inserted == 0:
							
							tempCode.append(3)
			
		
		tempMessage.append("Possible side effects include: {0}!".format(tempListOfSideEffects))
		
		#3. Creating the medicationReport message and code
		
		## code to str for join function
		for i in range(len(tempCode)):
			tempCode[i] = str(tempCode[i])
		
		
		
		## append new codes 
		
					
		self.medicationReportCode = ''.join(tempCode)
		
		
		self.medicationReportMessage = ''.join(tempMessage)
		
		#print(self.medicationReportCode)
		self.printMedicationReportMessage()
		self.printBorder()
	
	def activeIngredientToCategory(self,activeIngredient):
    # Method that returns the active ingredients category 
	
			if (activeIngredient=='Atorvastasin'):
				return self.statin
			
			elif (activeIngredient=='Esomeprazole'):
				return self.esomeprazole
			
			elif (activeIngredient=='Clopidogrel'):
				return self.antiplatelet
			
			elif (activeIngredient=='Aripiprazole'):
				return self.aripiprazole
			
			elif (activeIngredient=='Montelukast'):
				return self.montelukast
			
			elif (activeIngredient=='Pimozide'):
				return self.antipsychotic
			
			elif (activeIngredient=='Ketoconazole'):
				return self.antifungal
	
	
	def printMedicationReportMessage(self):
	
		print ("|       Creating MedicationReport message...         |")

		self.printEmptyLines(2)
		tempListOfMessages = self.medicationReportMessage.split('!')
		
		for i in range (len(tempListOfMessages)-1):
			print("|  "+tempListOfMessages[i] + "!")
		
		self.printEmptyLines(3)
	
	
	def getAll(self):
		
		print(self.statin)
		print(self.esomeprazole)
		print(self.antiplatelet)
		print(self.aripiprazole)
		print(self.montelukast)
		print(self.antipsychotic)
		print(self.antifungal)
		print(self.listOfSideEffects)
		print(self.listOfReacts)

	def getStatin(self):
		return self.statin
		
	def getEsomeprazole(self):
		return self.esomeprazole
		
	def getAntiplatelet(self):	
		return self.antiplatelet
	
	def getAripiprazole(self):
		return self.aripiprazole
	
	def getMontelukast(self):
		return self.montelukast
		
	def getAntipsychotic(self):
		return self.antipsychotic
		
	def getAntifungal(self):
		return self.antifungal
	
	def getListOfSideEffects(self):
		return self.listOfSideEffects
	
	def getListOfReacts(self):
		return self.listOfReacts
	
	def setID(self,id):
		self.id = id
	
	def getID(self):
		return self.id
		
	def getDate(self):
		return self.date
		
	def getMedicationReportCode(self):
		return self.medicationReportCode
	
	def getMedicationReportMessage(self):
		print(self.medicationReportMesage)
		
	def printEmptyLines(self,emptyLines):
		for i in range(emptyLines):
			print ("|                                                    |")
	
	def printBorder(self):
		print("======================================================")#footer	