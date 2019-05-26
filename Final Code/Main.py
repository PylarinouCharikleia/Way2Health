import pandas
from datetime import date
from Diet import *
from Sensor import *
from User import *
from Calendar import *
from MedicalExams import *
from HealthStatus import *
import pandas as pd
import csv
from time import sleep
import random
import keyboard
import sys


if __name__ == '__main__':
	
	listOfDietReports = []
	listOfMedicationReports = []
	listofMedicalReports = []
	
	lastDietReport = None 
	lastMedicationReport = None
	lastMedicalReport = None
	
	dietInserts=0
	medicineInserts=0
	examsInserts = 0
	
	patients=0
	doctors=0
	
	sensor = Sensor("Jerry", "S")
	bloodSensor = BloodSensor("Jerry", "BS")
	generalSensor = GeneralSensor("Jerry", "GS")
	respiratorySensor = RespiratorySensor("Jerry", "RS")
	cardiacsensor = CardiacSensor("Jerry", "CS")
	environmentalSensor = EnvironmentalSensor("Jerry", "ES")
	
	cache = np.zeros([20,10]) 
	running = 1
	counter = 1
	cacheRefreshCount = 0
	
	
	
	
	
	#1. User Insertion Methods
	
	## Patient Methods 
	
	def completeForm1():
		
		for i in range(8):
			if (i==5):
				print ("|         Insert your personal information:          |")
			else:
				printEmptyLines(1)

		name = 	input ("|      Name: ")
		printEmptyLines(1)
		
		surname = input("|      Surname: ")
		printEmptyLines(1)
		
		email = input("|      E-mail: ")
		printEmptyLines(1)
		
		phone = input("|      Phone: ")
		printEmptyLines(1)
		
		city = input("|      City: ")
		printEmptyLines(1)
		
		flag = 0
		birth = input("|      Date of birth: ")
		printEmptyLines(2)
		
		while flag==0:
			try:
				time.strptime(birth, '%d/%m/%Y')
				flag=1;
			except ValueError:
				print ("|    Incorrect data format, should be DD/MM/YYYY!    |")
				birth = input("|      Date of birth: ")
		
		print ("|         Insert your account information:           |")
		printEmptyLines(2)
			
		username = input("|      Username: ")
		printEmptyLines(1)
		password = input("|      Password: ")
		printEmptyLines(3)
		
		printBorder()
		
		return name, surname, email, phone, city, birth, username, password

	def completeForm2():
		
		print("==============Patient Registration(2/2)===============")#header
		
		printEmptyLines(5)
		print ("|         Insert your body type information:         |")
		printEmptyLines(3)
		
		gender = input("|      Gender: ")
		
		while gender.lower()!='male' and gender.lower()!='female':
			print ("|   That's not a valid input! Type male or female!   |")
			gender = input("|      Gender: ")

			
		printEmptyLines(3)
		
		flagW = 0
		weight = input("|      Weight: ")
		
		while flagW==0:
			try:
				weight = int(weight)
				flagW = 1
			except ValueError:
				print("|That's not a valid input!Please reinsert this field |")
				weight = input("|      Weight: ")
		printEmptyLines(3)
		
		flagH = 0
		height = input("|      Height: ")
		
		while flagH==0:
			try:
				height = int(height)
				flagH = 1
			except ValueError:
				print("|That's not a valid input!Please reinsert this field |")
				print("|   That's not a valid input!Please reinsert in cm   |")
				height = input("|      Height: ")
		printEmptyLines(3)

		printEmptyLines(11)
		printBorder()
		
		return gender, weight, height

	def allFieldsOK1(name, surname, email, phone, city, birth, username, password, gender, weight, height):
		if name == '' or surname == '' or birth == '' or city == '' or email == '' or phone == '' or username == '' or password == '' or gender == '' or weight == '' or height == '':
			messageCompleteFields()
			return 1
		else:
			return 0	

	def patientRegistration():
		
		print("==============Patient Registration(1/2)===============")#header

		tempID = random.randint(1,999)
		check = 1
		while check == 1:
			newName, newSurname, newEmail, newPhone, newCity, newBirth, newUsername, newPassword = completeForm1()
			newGender, newWeight, newHeight = completeForm2()
			check = allFieldsOK1(newName, newSurname, newEmail, newPhone, newCity, newBirth, newUsername, newPassword, newGender, newWeight, newHeight)
			
		newPatient = Patient(newName.lower(), newSurname.lower(), newEmail, newPhone, newCity.lower(), newBirth, newUsername.lower(), newPassword, newGender.lower(), newWeight, newHeight, tempID)

		# Save the patient in the insertedPatients "Database" file
		
		with open('InsertedPatients.csv', 'a', newline='') as f:
				fieldnames = ['UserID','Name','Surname','Gender','Date of Birth','Height','Weight']
		
				writer = csv.DictWriter(f,fieldnames=fieldnames)
				writer.writerow({'UserID': newPatient.getID(),'Name': newPatient.getName(),'Surname': newPatient.getSurname(),'Gender': newPatient.getGender(),'Date of Birth' : newPatient.getDateOfBirth(),'Height' : newPatient.getHeight(),'Weight' : newPatient.getWeight()})
	
			
		return newPatient			
	
	## Doctor Methods
	def completeForm():
		
		for i in range(8):
			if (i==5):
				print ("|         Insert your personal information:          |")
			else:
				printEmptyLines(1)
		
		
		name = input("|      Name: ")
		printEmptyLines(1)
		
		surname = input("|      Surname: ")
		printEmptyLines(1)
		
		email = input("|      E-mail: ")
		printEmptyLines(1)
		
		specialization = input("|      Specialization: ")
		printEmptyLines(1)
		
		phone = input("|      Phone: ")
		printEmptyLines(1)
		
		city = input("|      City: ")
		printEmptyLines(1)

		flag = 0
		birth = input("|      Date of birth: ")
		printEmptyLines(1)
		
		while flag==0:
			try:
				time.strptime(birth, '%d/%m/%Y')
				flag=1;
			except ValueError:
				print ("|    Incorrect data format, should be DD/MM/YYYY!    |")
				birth = input("|      Date of birth: ")

				
		gender = input("|      Gender: ")
		
		while gender.lower()!='male' and gender.lower()!='female':
			print ("|   That's not a valid input! Type male or female!   |")
			gender = input("|      Gender: ")
		
		printEmptyLines(1)
		
		username = input("|      Username: ")
		printEmptyLines(1)
		
		password = input("|      Password: ")
		printEmptyLines(1)
		
		rank = input("|      Rank: ")
		printEmptyLines(1)
		
		cv = input("|      CV: ")
		printEmptyLines(1)
		
		listOfDiplomas = input("|      Diplomas: ")
		printEmptyLines(1)

		return name, surname, email, specialization, phone, city, birth, gender, username, password, rank, cv, listOfDiplomas

	def allFieldsOK2(name, surname, email, specialization, phone, city, birth, gender, username, password, rank, cv, listOfDiplomas ):
		if name == '' or surname == '' or birth == '' or specialization == '' or city == '' or email == '' or phone == '' or username == '' or password == '' or gender == '' or rank == '' or cv == '' or listOfDiplomas == '':
			messageCompleteFields()
			return 1
		else:
			return 0

	def docValidate():
		return "Documents have been validated!"

	def messageCompleteFields():
			 
		print("|           Please complete all the fields.          |")

	def messageSuccess():
		print("|              Successful Registration.              |")
		
	def messageFail():
		print("|                Failed Registration.                |")

	def doctorRegistration():
		
		print("===============Doctor Registration(1/2)===============")#header
		check = 1
		while check == 1:
			newName, newSurname, newEmail, newSpecialization, newPhone, newCity, newBirth, newGender, newUsername, newPassword, newRank, newCv, newListOfDiplomas = completeForm()
			check = allFieldsOK2(newName, newSurname, newEmail, newSpecialization, newPhone, newCity, newBirth, newGender, newUsername, newPassword, newRank, newCv, newListOfDiplomas)

		validation = docValidate()
		while validation != "Documents have been validated!":
			messageFail()
			check = 1
			while check == 1:
				newName, newSurname, newEmail, newSpecialization, newPhone, newCity, newBirth, newGender, newUsername, newPassword, newRank, newCv, newListOfDiplomas = completeForm()
				check = allFieldsOK2(newName, newSurname, newEmail, newSpecialization, newPhone, newCity, newBirth, newGender, newUsername, newPassword, newRank, newCv, newListOfDiplomas)

			validation = docValidate()

		newDoctor = Doctor(newName, newSurname, newEmail, newSpecialization, newPhone, newCity, newBirth, newGender, newUsername, newPassword, newRank, newCv, newListOfDiplomas)
		messageSuccess()
		return newDoctor
	
	
	# Insertion Methods 
	
	def insertItem(item,type):
	# Method that saves the diet instance in a "database" file named 'InsertedDiet'.
	
        #0. Variables	
		
		##Item data
		
		###Save the patients id
		tempID = item.getID()
		tempDate = date.today().strftime("%d/%m/%Y")
		tempName = item.getName()
		tempQuantity = 1
		
		if (type=="diet"):
			
			tempQuantity = item.getQuantity()
			
		elif (type=="medicine"):
		
			tempQuantity = item.getDose()
		
		##Flags and counters
		
		###Flag that indicates if there is an other input of this kind of item from the same user the current day
		flag = 0
	
		##CSV Files Dataframes

		if (type=="diet"):
			
			inserted='InsertedDiet.csv'
			instances='DietInstances.csv'
			
		elif (type=="medicine"):
		
			inserted='InsertedMedicine.csv'
			instances='MedicineInstances.csv'
		
		elif (type=="exam"):
		
			inserted = 'InsertedMedicalExams.csv'
			instances = {
				"metabolism": 'MetabolismInstances.csv',
				"heart": 'HeartInstances.csv',
				"urinary": 'UrinaryInstances.csv' ,
				"liver": 'LiverInstances.csv',
				"vitamins": 'VitaminsInstances.csv' ,
				"thyroid": 'ThyroidInstances.csv',
				"immune": 'ImmuneInsances.csv',
				"generalblood": 'GeneralBloodInstances.csv' 
    		}[tempName] 
		
		###Variables for diet dataframes 
		df = pandas.read_csv(inserted)
		df1 = pandas.read_csv(instances,sep=",")
			
		
		##Check Variable for search in inserted items file
		
		if (type=="diet"):
			global dietInserts
			check = dietInserts
				
		elif (type=="medicine"):
			global medicineInserts
			check = medicineInserts
		
		elif (type == "exam"):
			global examsInserts 
			check = examsInserts
		
		#1. Check the database for other this type of instances of this user 
		
		if (check>0):
			
			##result holds the item records of the specific user the same day
			resultID = df['UserID']==tempID
			resultDate = df['Date']==tempDate
			result = resultID & resultDate

			
			##if there is an other item from the same user the same day
			for i in range(check):
				if (result[i] == True):	
					flag = 1 ##flag==1 -> the user had inserted an item instance again this day
					break 
		
		#2. Save the item input in the inserted item file (UserID, Name, Quantity)
		
		with open(inserted, 'a', newline='') as f:
			fieldnames = ['UserID','Date','Name','Quantity']
		
			writer = csv.DictWriter(f,fieldnames=fieldnames)
			writer.writerow({'UserID' : tempID,'Date' : tempDate,'Name' : tempName,'Quantity' : tempQuantity})
		
		if (type=="diet"):
			dietInserts = dietInserts + 1
		elif (type=="medicine"):
			medicineInserts = medicineInserts+1
		elif (type == "exams"):
			examsInserts = examsInserts + 1
		
		#3. Get the item instance stats from the instances database file
		
		# stats record from 'Instances' database file
		
		resultFlag = True  
		
		#if type!="exam":
		result = df1[df1['Name'] == item.getName()]
		
		#else:
			#print(df1.values[0])
			#result = df1.values[0]
		#	print(df1.iloc[0,:])
		#	result = df1.iloc[0,:]
			
		while resultFlag==True:
			try:
				if (type=="diet"):
					item.setDiet(result.values[0,1],result.values[0,2],result.values[0,3],result.values[0,4],result.values[0,5],result.values[0,6],result.values[0,7],result.values[0,8],result.values[0,9],result.values[0,10])
			
				elif (type=="medicine"):
					item.setMedicine(result.values[0,2],result.values[0,1],result.values[0,3],result.values[0,4],result.values[0,5])
				
				elif (type=="exam"):

					if (tempName=="metabolism"):
						item.setMetabolism(result.values[0,0])

					elif(tempName=="heart"):
						item.setHeart(result.values[0,0],result.values[0,1])

					elif(tempName=="urinary"):
						item.setUrinary(result.values[0,0],result.values[0,1],result.values[0,2],result.values[0,3],result.values[0,4],result.values[0,5],
						result.values[0,6],result.values[0,7],result.values[0,8],result.values[0,9])

					elif(tempName=="liver"):
						item.setLiver(result.values[0,0],result.values[0,1],result.values[0,2],result.values[0,3],result.values[0,4],result.values[0,5],
					    result.values[0,6],result.values[0,7],result.values[0,8],result.values[0,9],result.values[0,10],result.values[0,11])

					elif(tempName=="vitamins"):
						item.setVitamins(result.values[0,0],result.values[0,1],result.values[0,2],result.values[0,3],result.values[0,4],result.values[0,5],
					    result.values[0,6],result.values[0,7],result.values[0,8],result.values[0,9],result.values[0,10],result.values[0,11])

					elif(tempName=="thyroid"):
						item.setThyroid(result.values[0,0],result.values[0,1],result.values[0,2],result.values[0,3])

					elif(tempName=="immune"):
						item.setImmune(result.values[0,0],result.values[0,1])
	
					elif(tempName=="generalblood"):
						item.setGeneralBloodTest(result.values[0,0],result.values[0,1],result.values[0,2],result.values[0,3],result.values[0,4],result.values[0,5])
				
				resultFlag = result.empty
				
			except IndexError:
				
				print ("|     Item not found! Insert an existing item!       |")
				printEmptyLines(2)
				
				if (type=="diet"):
					tempDiet = pat.insert_diet()
					insertItem(tempDiet,"diet")
					return 
					
				elif (type=="medicine"):
					tempMedicine = pat.insert_medicine()
					insertItem(tempMedicine,"medicine")
					return 
				
				elif (type=="exam"):
					tempExam = pat.insert_medical_report()
					insertItem(tempExam,"exam")
					return 
	
		#4. Create (if new) a report and call the insertReport to save it in the inserted reports file
		if ( flag == 0 ): ##if first item instance of the user this day = if itemReport not created for this day
			if (type=="diet"):
				dietReport = DietReport(tempDate)
				dietReport.setDietReport("new",tempID,item)
				report=dietReport
				#report.getAll()
				
			elif (type=="medicine"):
				medicationReport = MedicationReport(tempDate)
				medicationReport.setMedicationReport("new",tempID,item)
				report=medicationReport
			
			elif (type=="exam"):
				medicalReport = MedicalReport(tempDate)
				medicalReport.setMedicalReport(tempID,item)
				report = medicalReport
			
			insertReport("new",type,report)
			#report.getAll()
			
		elif ( flag == 1 ):
			if (type=="diet"):
				for i in range (len(listOfDietReports)):
					if (listOfDietReports[i].getDate()==tempDate)&(listOfDietReports[i].getID()==tempID):
						listOfDietReports[i].setDietReport("old",tempID,item)
						insertReport("old",type,listOfDietReports[i])
						#Main.listOfDietReports[i].getAll()
						
			elif (type=="medicine"):
				for i in range (len(listOfMedicationReports)):
					if (listOfMedicationReports[i].getDate()==tempDate)&(listOfMedicationReports[i].getID()==tempID):
						listOfMedicationReports[i].setMedicationReport("old",tempID,item)
						insertReport("old",type,listOfMedicationReports[i])
						#Main.listOfMedicationReports[i].getAll()
			
			elif (type=="exam"):
				for i in range (len(listOfMedicalReports)):
					if (listOfMedicalReports[i].getDate()==tempDate)&(listOfMedicalReports[i].getID()==tempID):
						listOfMedicalReports[i].setMedicalReport(tempID,item)
						insertReport("old",type,listOfMedicalReports[i])	
						#listOfMedicalReports[i].getAll()

			
	def insertReport(case,type,report):	
	# Method that saves the reports in the listOfReports of Main class and in the Inserted Reports once old	
		
		#if we have a new report we append it to the list 
		if case=="new":
			if (type=="diet"):
				listOfDietReports.append(report)
				global lastDietReport
				check = lastDietReport
				insertedReports='InsertedDietReports.csv'
			
			elif (type=="medicine"):
				listOfMedicationReports.append(report)
				global lastMedicationReport
				check = lastMedicationReport
				insertedReports='InsertedMedicationReports.csv'
			
			elif (type=="exam"):
				listofMedicalReports.append(report)
				global lastMedicalReport
				check = lastMedicalReport
				insertedReports='InsertedMedicalReports.csv'
			
			
			#if we had a previous report we write it in the inserted reports file
			if (check!=None):
				
				if (type=="diet"):
					with open(insertedReports, 'a', newline='') as f:
						fieldnames = ['UserID','Date','Meals','Beverages','Supplements','Calories (J)','Protein (g)','Carbonhydrates (g)','Sugars (g)','Fat (g)','Fiber (g)','VitaminA(%)','VitaminC(%)','Sodium(mg)','Potassium(g)','Calcium(g)','Iron(g)']
						writer = csv.DictWriter(f,fieldnames=fieldnames)
						writer.writerow({'UserID':lastDietReport.getID(),'Date':lastDietReport.getDate(),'Meals':lastDietReport.getMeals(),'Beverages':lastDietReport.getBeverages(),'Supplements':lastDietReport.getSupplements(),'Calories (J)':lastDietReport.getCalories(),'Protein (g)':lastDietReport.getProtein(),'Carbonhydrates (g)':lastDietReport.getCarbonhydrates(),'Sugars (g)':lastDietReport.getSugars(),'Fat (g)':lastDietReport.getFat(),'Fiber (g)':lastDietReport.getFiber(),'VitaminA(%)':lastDietReport.getVitaminA(),'VitaminC(%)':lastDietReport.getVitaminC(),'Sodium(mg)':lastDietReport.getSodium(),'Potassium(g)':lastDietReport.getPotassium(),'Calcium(g)':lastDietReport.getCalcium(),'Iron(g)':lastDietReport.getIron()})
				
				elif (type=="medicine"): 
					with open(insertedReports, 'a', newline='') as f:	
						fieldnames = ['UserID','Date','Statin','Esomeprazole','Antiplatelet','Aripiprazole','Montelukast','Antipsychotic','Antifungal','List of Side Effects','List of Reacts']
						writer = csv.DictWriter(f,fieldnames=fieldnames)
						writer.writerow({'UserID':lastMedicationReport.getID(),'Date':lastMedicationReport.getDate(),'Statin':lastMedicationReport.getStatin(),'Esomeprazole':lastMedicationReport.getEsomeprazole(),'Antiplatelet':lastMedicationReport.getAntiplatelet(),'Aripiprazole':lastMedicationReport.getAripiprazole(),'Montelukast':lastMedicationReport.getMontelukast(),'Antipsychotic':lastMedicationReport.getAntipsychotic(),'Antifungal':lastMedicationReport.getAntifungal(),'List of Side Effects':lastMedicationReport.getListOfSideEffects(),'List of Reacts':lastMedicationReport.getListOfReacts()})
				
				elif (type=="exam"):
					with open(insertedReports, 'a', newline='') as f:	
						fieldnames = ['UserID','Date','cmp','hdl','ldl','urineColor','urineClarity','specificGravity','pH','protein','glucose','ketones','crystals','bacteria','blood',
                                                              'lft','uANDe','totBilrubin','alt','ast','ggt','Albumin','fiveNeuclotidase','ceruloplasmin','afp','serumGlucose','lactateDehyfrogenase',
                                                              'carotene','vitaminA','vitaminB1','vitaminB2','vitaminB3','vitaminB5','vitaminB6','vitaminB12','vitaminD25Hydroxy','vitaminE','vitaminK','folicAcid',
                                                              'tsh','t3','t4','freeT4',
                                                              'cpr','esr','cbc','inr','wbc','rbc','hmc','plt']
						writer = csv.DictWriter(f,fieldnames=fieldnames)
						data = report.getAll()
						writer.writerow({'UserID':lastMedicalReport.getID(),'Date':lastMedicalReport.getDate(),'cmp':data[0],'hdl':data[1],
                                                                 'ldl':data[2],'urineColor':data[3],'urineClarity':data[4],'specificGravity':data[5],'pH':data[6],'protein':data[7],'glucose':data[8],
                                                                 'ketones':data[9],'crystals':data[10],'bacteria':data[11],'blood':data[12],'lft':data[13],'uANDe':data[14],'totBilrubin':data[15],
                                                                 'alt':data[16],'ast':data[17],'ggt':data[18],'Albumin':data[19],'fiveNeuclotidase':data[20],'ceruloplasmin':data[21],'afp':data[22],
                                                                 'serumGlucose':data[23],'lactateDehyfrogenase':data[24],'carotene':data[25],'vitaminA':data[26],'vitaminB1':data[27],'vitaminB2':data[28],
                                                                 'vitaminB3':data[29],'vitaminB5':data[30],'vitaminB6':data[31],'vitaminB12':data[32],'vitaminD25Hydroxy':data[33],'vitaminE':data[34],
                                                                 'vitaminK':data[35],'folicAcid':data[36],'tsh':data[37],'t3':data[38],'t4':data[39],'freeT4':data[40],'cpr':data[41],'esr':data[42],
                                                                 'cbc':data[43],'inr':data[44],'wbc':data[45],'rbc':data[46],'hmc':data[47],'plt':data[48]})
				
			if (type=="diet"):
				lastDietReport=report
			elif(type=="medicine"):
				lastMedicationReport=report
			elif(type=="exam"):
				lastMedicalReport=report
		
		
		elif case=="old":
			if (type=="diet"):
				for i in range(len(listOfDietReports)):
					if (listOfDietReports[i].getDate()==report.getDate())&(listOfDietReports[i].getID()==report.getID()):
						listOfDietReports[i]==report
						lastDietReport = report
						
			elif (type=="medicine"):
				for i in range(len(listOfMedicationReports)):
					if (listOfMedicationReports[i].getDate()==report.getDate())&(listOfMedicationReports[i].getID()==report.getID()):
						listOfMedicationReports[i]==report
						lastMedicationReport = report

			elif (type=="exam"):
				for i in range(len(listOfMedicalReports)):
					if (listOfMedicalReports[i].getDate()==report.getDate())&(listOfMedicalReports[i].getID()==report.getID()):
						listOfMedicalReports[i]==report
						lastMedicalReport = report
						
				
	# Screen print methods			
	
	def printIntro():	
		printBorder()
		
		for i in range(30):
			
			if (i==11):
				print ("|                    Way2Health                      |")
			elif (i==28):
				print ("|               Loading please wait..                |")
			else:
				printEmptyLines(1)
		
		printBorder()

		
	def printLoginRegister():
		
		printBorder()
		
		for i in range(28):
			
			if (i==6):
				print ("|                    Way2Health                      |")
			
			elif (i==8)|(i==18):
				print ("|         -------------------------------            |")
			
			elif (i==9)|(i==17):
				print ("|        |                               |           |")
			
			elif (i==10)|(i==12)|(i==14)|(i==16):
				print ("|        |    -----------------------    |           |")
			
			elif (i==11):
				print ("|        |   |        Login          |   |           |")
			
			elif (i==13):
				print ("|        |              or               |           |")
			
			elif (i==15):
				print ("|        |   |       Register        |   |           |")
			
			elif (i==26): 
				print ("|           What would you like to do?               |")
			
			elif (i==27): 
				print ("|           1.login , 2.register, 3.exit             |")
			
			else:
				printEmptyLines(1)
	
	
	def printRegister(mode):
	
		if (mode==0):
		
			print("=====================Registration=====================")
		
			for i in range(10):
			
				if (i==4):
					print ("|           Would you like to register as            |")
				
				
				elif (i==5):
					print ("|              patient or as  doctor?                |")

				else:
					printEmptyLines(1)
		
		if (mode==1):
			
			for i in range(18):
			
				if (i==15):
					print ("|         Redirecting to the proper page...          |")
					
				else:
					printEmptyLines(1)
	
	
	def printLogin(mode):
		
		if (mode==0):
		
			print("=========================Login========================")
			
			for i in range(10):
			
				if (i==4):
					print ("|             Would you like to login as             |")
				
				elif (i==5):
					print ("|              patient or as  doctor?                |")

				else:
					printEmptyLines(1)
		
		if (mode==1):
			
			for i in range(18):
			
				if (i==15):
					print ("|         Redirecting to the proper page...          |")
					
				else:
					printEmptyLines(1)
	
	def printMainMenu(healthStatus,m1,m2,m3):
		
		printBorder()
		
		for i in range(6):
			
			if (i==2):
				print ("|                                 ----------------   |")
			
			elif (i==3):
				print ("|         Overal Health:         |   Vital Signs  |  |")
				
			elif (i==4):
				print ("|                                |                |  |")
			
			elif(i==5):
				print ("|                                 ----------------   |")
			
			else:
				printEmptyLines(1)
				
		healthStatus.sendMessage(m1,m2,m3)
		
		for i in range(9):
			
			if (i==2)|(i==4): 
				print ("|           ---------------------------              |")
			
			elif (i==3):
				print ("|           |       Insert Data       |              |")
			
			elif (i==6): 
				print ("|           What would you like to do?               |")
			
			elif (i==7): 
				print ("|         1.insert_data , 2.see_vital_signs          |")
			
			elif (i==8): 
				print ("|        3.view_calendar, 4.view_inbox, 5.exit       |")
			
			else:
				printEmptyLines(1)
	
	def printDocMainMenu():
	
		printBorder()
		
		for i in range(29):
			
			if (i==3):
				print ("|            Way2Health: Doctor's Edition            |")
			
			elif (i==7)|(i==13)|(i==19):
				print ("|	  __                                         |")
			
			elif (i==8):
				print ("|       /    \         Calendar                      |")
			elif(i==14):
				print ("|       /    \         Inbox                         |")
			
			elif(i==20):
				print ("|       /    \         Notification                  |")
			
			elif(i==9)|(i==15)|(i==21):
				print ("|       \    /                                       |")
			
			elif (i==10)|(i==16)|(i==22):
				print ("|         ¯̅                                         |")
			
			elif (i==26):
				print ("|            What would you like to do?              |")
			
			elif(i==27):
				print ("|          1.view_calendar, 2.send_message,          |")
				
			elif(i==28):
				print ("|           3.send_notification, 4.exit              |")
			else:
				printEmptyLines(1)
				
	
	def printInsertMenu():
		
		printBorder()
		
		for i in range(36):
			
			if (i==4):
				print ("|           Select the Type of Data                  |")
				
				
			elif (i==5):
				print ("|              you want to Insert                    |")
				
			elif (i==9):
				print ("|                    Workout                         |")
					
			elif(i==10):
				print ("|        	        __                           |")
				
			elif(i==11):
				print ("|                     /    \                         |")
				
			elif(i==12):
				print ("|                     \    /                         |")
				
			elif(i==13):
				print ("|                       ¯̅                           |")
				
			elif(i==16):
				print ("|      Medical                         Medicine      |")
				
			elif(i==17):
				print ("|      Report                           Report       |")
				
			elif(i==18):
				print ("|        __                               __         |")
				
			elif(i==19):
				print ("|      /    \             X             /    \       |")
				
			elif(i==20):
				print ("|      \    /                           \    /       |")
				
			elif(i==21):
				print ("|        ¯̅                               ¯̅         |")
				
			elif(i==24):
				print ("|                       Food                         |")
				
			elif(i==25):
				print ("|            		 __                          |")
				
			elif(i==26):
				print ("|                      /    \                        |")
				
			elif(i==27):
				print ("|                      \    /                        |")
				
			elif(i==28):
				print ("|                        ̅¯                          |")
				
			elif(i==32):
				print ("|               Type the type of Data                |")
				
			elif(i==33):	
				print ("|                 you want to insert                 |")
				
			elif(i==34):
				print ("|         1.diet, 2.medicine, 3.exam, 4.exit         |")
				
			else:
				printEmptyLines(1)
				
	
	
	# Window print methods	
		
	def printEmptyLines(emptyLines):
		for i in range(emptyLines):
			print ("|                                                    |")
	
	def printBorder():
		print("======================================================")#footer


	def onClickOnName(pat_list):
		clickOn = -1
		while clickOn not in range(1, len(pat_list) + 1):
			try:
				clickOn = int(input("Choose Patient:"))
			except ValueError:
				print("Invalid Input")
				continue
		return pat_list[clickOn - 1]


	def showPatientData(patient):
		print("Name: ", patient.name)
		print("Surname: ", patient.surname)
		print("Gender: ", patient.gender)
		print("Birth Date: ", patient.birth)
		print("Email: ", patient.email)
		print("Phone: ", patient.phone)
		print("City: ", patient.city)
		print("Weight: ", patient.weight)
		print("Height: ", patient.height)

	def printName(p):
		print("Name:", p.name, "Surname:", p.surname)


	def showPatientName(in_list):
		num = 1
		for p in in_list:
			print("Patient", num, ": ")
			printName(p)
			num = num + 1


	def onSearchByName(doctor):
		print("Enter Name and Surname:")
		name = input("Name:")
		surname = input("Surname:")
		full_name = [name, surname]
		pat_list = doctor.searchPatient(full_name)
		if pat_list:
			showPatientName(pat_list)
			selected_patient = onClickOnName(pat_list)
			showPatientData(selected_patient)

	def messageReadingError():
		print("Not able to read new values!")


	def VitalSigns(current, bloodSensor, generalSensor, respiratorySensor, cardiacSensor, envSensor, sensor):
		q = True
		counter = 0;

		#while q and counter < 5:
		if current.checkAllReadAbility(generalSensor, cardiacSensor, respiratorySensor, bloodSensor):
			current.getNewValues(bloodSensor, generalSensor, respiratorySensor, cardiacSensor, envSensor, sensor)
			current = CurrentStatus(bloodSensor, generalSensor, respiratorySensor, cardiacSensor, envSensor)
			showVitalSigns(bloodSensor, generalSensor, respiratorySensor, cardiacSensor)
			counter += 1
		else:
			messageReadingError()
			return 0


	def showVitalSigns(bloodSensor, generalSensor, respiratorySensor, cardiacSensor):
		print ("======================Vital Signs=====================")
		printEmptyLines(2)
		print ("| General Measurments:                               |")
		generalSensor.printValues()
		print ("| Cardiac Measurements:                              |")
		cardiacSensor.printValues()
		print ("| Respiratory Measurements:                          |")
		respiratorySensor.printValues()
		print ("| Blood Measurements:                                |")
		bloodSensor.printValues()
		print ("|           Keep 'q' pressed to go back              |")
		printBorder()

	
	def currentStats(bs,gs,rs,cs,es):
	
		array = np.zeros([20])

		#Environment Stats -------------------
		array[0] = es.temp
		array[1] = es.humidity 
		array[2] = es.co 
		array[3] = es.co2 
		array[4] = es.radon 
		array[5] = es.formaldehyde 
		array[6] = es.airMold 
		array[7] = es.asbesto 
		array[8] = es.airParticles
		array[9] = es.light 
		
		#Blood Stats -------------------------
		array[10] = bs.bol 
		array[11] = bs.bg 
		
		#General Stats -----------------------
		array[12] = gs.bt  
		array[13] = gs.skinPerspiration 

		#Respiration Stats -------------------
		array[14] = rs.rp 
		array[15] = rs.respirationSounds 
		
		#Cardiac Stats -----------------------
		array[16] = cs.ecg 
		array[17] = cs.hr 
		array[18] = cs.sysBP 
		array[19] = cs.diaBP 	

		return array
	


	
	#0. Intro screen print 	
	printIntro()
	time.sleep(5)

	## register flag 
	regFlag=0
	regFlag2=0

	## Null items 
	pat=None
	doc=None 
	health=None
	calendar=None
	calendar2=None
	m1 = "0"
	m2 = 1
	m3 = "0"


	#login/register screen while 
	while (1):
		
		
		optFlag=0
		
		#1. Login/Register screen print 
		printLoginRegister()
		
		option = input("|      Option: ")
		option = option.lower()
		
		while optFlag==0:
			
			if (option != "login" and option != "register" and option != "exit"):
				print("|          Please enter correct option!              |")
				
				option = input("|      Option: ")
				option = option.lower()
			else:
				printEmptyLines(1)
				optFlag=1 
	
		printEmptyLines(1)
	
	
		if (option == "login"):
			
			printLogin(0)
		
			opt3Flag=0
		
			option = input("|      Option: ")
			option = option.lower()
		
			while opt3Flag==0:
		
				if (option != "patient" and option != "doctor" and option != "exit"):
					print("|          Please enter correct option!              |")
			
					option = input("|      Option: ")
					option = option.lower()
				else:
					printEmptyLines(1)
					opt3Flag=1 
	
			printRegister(1)
			printEmptyLines(1)
			printBorder()
		
			if option=="patient":
			
				if regFlag==0:
					printEmptyLines(1)
					print("|        Please register first to proceed!           |")
					printEmptyLines(1)
				else:

					while (1):

						opt2Flag = 0
					
						#global m1
						#global m2
						#global m3 
						print(m1)
						print(m2)
						print(m3)
						printMainMenu(health,m1,m2,m3)
	
						option = input("|      Option: ")
						option = option.lower()
	
						while opt2Flag==0:
		
							if (option != "insert_data" and option != "see_vital_signs" and option != "exit" and option!="view_calendar" and option!="view_inbox" and option!="exit"):
								print("|          Please enter correct option!              |")
			
								option = input("|      Option: ")
								option = option.lower()
							else:
								printEmptyLines(1)
								opt2Flag=1 
	
	
	
						printEmptyLines(1)
	
						if (option == "insert_data"):
	
							while(1):
		
								opt3Flag = 0
			
								printInsertMenu()
				
								option = input("|      Option: ")
								option = option.lower()
	
								while opt3Flag==0:
		
									if (option != "diet" and option != "medicine" and option != "exam" and option != "exit"):
										print("|          Please enter correct option!              |")
			
										option = input("|      Option: ")
										option = option.lower()
			
									else:
										printEmptyLines(1)
										opt3Flag=1 
							
								#global pat 
								
								if (option == "diet"):
									tempDiet = pat.insert_diet()
									insertItem(tempDiet,"diet")
									#global m1
									m1 = lastDietReport.getDietReportCode()
				
				
								elif (option == "medicine"):
									tempMed = pat.insert_medicine()
									insertItem(tempMed,"medicine")
									#global m3
									m3 = lastMedicationReport.getMedicationReportCode()
	
								elif (option == "exam"):
									tempExam = pat.insert_medical_report()
									insertItem(tempExam,"exam")
									#global m2 
									m2 = lastMedicalReport.getMessage()
	
								elif (option == "exit"):
									break
	
		
							printBorder()
		
						elif (option == "see_vital_signs"):
			
							while (running == 1):
		
								sleep(0.8)
								sensor.setAll(bloodSensor,generalSensor,respiratorySensor,cardiacsensor,environmentalSensor)
								currentStatus = CurrentStatus(bloodSensor,generalSensor,respiratorySensor,cardiacsensor,environmentalSensor)
	
								VitalSigns(currentStatus,bloodSensor,generalSensor ,respiratorySensor,cardiacsensor,environmentalSensor,sensor)
	
								if (counter < 30):
			
									currentStatsAr = currentStats(bloodSensor,generalSensor,respiratorySensor,cardiacsensor,environmentalSensor)
									sensor.refreshCache(counter,currentStatsAr)

								elif (counter == 30):
			
									sensor.generateCacheAv()			
									cacheRefreshCount = cacheRefreshCount + 1

								elif (counter == 31):

									sensor.setAll(bloodSensor,generalSensor,respiratorySensor,cardiacsensor,environmentalSensor)
									currentStatsAr = currentStats(bloodSensor,generalSensor,respiratorySensor,cardiacsensor,environmentalSensor)

								#if there is more than 20 percent difference between any stat			
								if (sensor.inputCacheDifCalc(currentStatsAr)[sensor.inputCacheDifCalc(currentStatsAr) > 20.0].size > 0):
									sensor.difSave(cacheRefreshCount,currentStatsAr)

								counter = 0
						

								if (cacheRefreshCount == 10):
			
									sensor.cacheAvSavePersixH(cacheRefreshCount)
									cacheRefreshCount = 0

								try:  # used try so that if user pressed other than the given key error will not be shown
									if keyboard.is_pressed('q'):  # if key 'q' is pressed 
										break  # finishing the loop
									else:
										pass
								except:
									break
		
								counter = counter + 1	
		
						elif (option == "view_calendar"): 	
		
							viewCalendar(calendar)
		
							printBorder()
		
						elif (option == "view_inbox"):
							#global doc 
						
							if (doc==None):
								print("|          No doctors has been registered!           |")
						
							elif (doc!=None):
								#global pat
								pat.listOfDoctors.append(doc)
								pat.selectReceiver()
							
						elif (option == "exit"):
		
							printBorder()
							break 
				
				
		
			elif option=="doctor":
			
				if regFlag2==0:
					printEmptyLines(1)
					print("|        Please register first to proceed!           |")
					printEmptyLines(1)
			
				else:
				
					while(1):
					
						exitFlag=0 
					
						opt4Flag = 0
				
						printDocMainMenu()
			
						option = input("|      Option: ")
						option = option.lower()
						printEmptyLines(2)
							
							
						while opt4Flag==0:
							#global doc 
						
							if (option != "view_calendar" and option != "send_message" and option != "send_notification" and option != "exit"):
								print("|          Please enter correct option!              |")
			
								option = input("|      Option: ")
								option = option.lower()
			
							else:
								printEmptyLines(1)
								opt4Flag=1 
				
							if (option == "view_calendar"):
								
								viewCalendar(calendar2)
								printBorder()
				
				
							elif (option == "send_message"):
								#global pat
							
								if (pat==None):
									print("|         No patients has been registered!           |")
								elif (pat!=None):
									doc.listOfPatients.append(pat)
									doc.selectReceiver()
							
							elif (option == "send_notification"):
						
								doc.completeNotification()
	
							elif (option == "exit"):
								exitFlag=1
								break
	
						
						if (exitFlag==1):
							break
				
				
					
				
				
				
				
				
				
			
			elif option=="exit":
				printBorder()
				break 
		
		
				
		elif (option == "register"):
			
			printRegister(0)
		
			opt3Flag=0
		
			option = input("|      Option: ")
			option = option.lower()
		
		
		
			while opt3Flag==0:
		
				if (option != "patient" and option != "doctor" and option != "exit"):
					print("|          Please enter correct option!              |")
			
					option = input("|      Option: ")
					option = option.lower()
				else:
					printEmptyLines(1)
					opt3Flag=1 
	
			printRegister(1)
			printEmptyLines(1)
			printBorder()
		
			if option=="patient":
				#global pat
				pat = patientRegistration()
				health = HealthStatus()
				calendar = Calendar("Calendar","General calendar",pat)
				regFlag=1
		
			elif option=="doctor":
				#global doc 
				doc = doctorRegistration()
				calendar2 = Calendar("Calendar","General calendar",doc)
				regFlag2=1
			
			elif option=="exit":
				printBorder()
				sys.exit(0)
		
		elif (option == "exit"):
			
			sys.exit(0) 
	
	printBorder()