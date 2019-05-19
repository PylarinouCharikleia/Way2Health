from colorama import Fore, Style

class HealthStatus:
	def __init__(self):
		self.status = None
		self.historyStatus = None
		self.medicalReportStatus = None
		self.medicationStatus = None
		self.exerciseStatus = None
		self.dietStatus = None
		self.code = None

	def sendMessage(self, message1, message2, message3):
		self.checkMessages(message1, message2, message3)

	def checkMessages(self, message1, message2, message3):

		#message 1 arguments
		ok1 = 0
		fats = 0
		vitamins = 0
		sugars = 0 
		calories = 0
		fiber = 0

		#message 2 arguments
		ok2 = 0
		allergic = 0
		constipation = 0
		head = 0
		dry_mouth = 0
		nutrients = 0
		bleeding = 0
		arrythmia = 0

		for letter in message1:
			if (letter == '0'): ok1 = 1
			elif (letter == '1'): fats = 1 
			elif (letter == '2'): vitamins = 1
			elif (letter == '3'): sugars = 1
			elif (letter == '4'): calories = 1
			elif (letter == '5'): fiber = 1		

		for letter in message3:
			if (letter == '0'): ok3 = 1
			elif (letter == '1'): allergic = 1 
			elif (letter == '2'): constipation = 1
			elif (letter == '3'): head = 1
			elif (letter == '4'): dry_mouth = 1			
			elif (letter == '5'): nutrients = 1
			elif (letter == '6'): bleeding = 1
			elif (letter == '7'): arrythmia = 1	

	
		if ok1 == 1 and message2 == 1 and ok3 == 1:
			warning = ""
			self.status = "Overall Health: Healthy"
			self.code = 0

		elif fats == 1 and message2 == 4 and arrythmia == 1:
			warning = "Critical cardiac burden! Suggestions: Lower consumption of saturated fats and medical check from cardiologist"
			self.status = "Overall Health: Severe"
			self.code = 1
		elif sugars == 1 and message2 == 1 and dry_mouth == 1:
			warning = "Warning! Aggravating factors for tooth decay. Suggestions: oral hygiene care or medication change"
			self.status = "Overall Health: In Risk"
			self.code = 2
		elif fiber == 1 and message2 == 1 and ok3 == 1:
			warning = "Warning! Aggravating factors for constipation. Suggestions: increase consumption of fibers"
			self.status = "Overall Health: In Risk"
			self.code = 3
		elif calories == 1 and message2 == 1 and ok3 == 1:
			warning = "Warning possible weight gain"
			self.status = "Overall Health: In Risk"
			self.code = 2

		print(self.status)	
		self.updateStatus(self.status)
		self.printAvatar(self.code)
		
		self.warnPatient(warning)
		
	def printAvatar(self,code):

		print("        //////\n       .  o o .\n      .    >   .")
		
		if (code == 2):
			print("      .  "),
			print(Fore.RED +"(*)"),
			print(Style.RESET_ALL),
			print(".") 
		else: print("      .    o   .")
			
		print("       .      .\n        ------\n       |   >  |\n ___--/        \--___")
		print("(##.###          ###.##)")

		if (code == 1) :
		
			print(".##. ## o"),
			print(Fore.RED +"(*)"),
			print(Style.RESET_ALL),
			print("o ## .##.")
		else: print(".##. ## o      o ## .##.")

		print(".##. ##          ## .##.\n.  . ##     o    ## .  .\n.  . ############## .  .")
		
		if (code == 3):
			print(".  . ###"),
			print(Fore.RED +"(*)"),
			print(Style.RESET_ALL),
			print("##### .  .") 
		else: print(".  . ############## .  .") 
		print("....\.###########./ ....\n ```` .##.    .##.  ````\n      .##.    .##.\n      .##.    .##.\n      .##.    .##.\n      .##.    .##.\n     .###.    .###.\n    (____|    |____)")

 
	def warnPatient(self,warning):
		print(warning)


	def updateStatus(self,status):
		self.status=status

		
