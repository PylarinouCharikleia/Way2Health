from datetime import timedelta,date
import datetime 
import time 
import pandas as pd
import math 
import numpy as np

class Diet:
	def __init__(self,name,quantity):
		self.name=name
		self.quantity=quantity
		
	def setDiet(self,type,calories,protein,carbonhydrate,sugars,fat,fiber,vitamins,electrolytes,minerals):
		
		
		print ("|               Diet item to macros...               |")
		self.type=type
		self.calories=calories
		self.protein=protein
		self.carbonhydrate=carbonhydrate
		self.sugars=sugars
		self.fat=fat
		self.fiber=fiber
		self.vitamins=vitamins
		self.electrolytes=electrolytes
		self.minerals=minerals
		
		Diet.printEmptyLines(1)
		print ("| Calories:{0}kcal ,  Protein:{1}g ,  Carbs:{2}g  ".format(self.calories,self.protein,self.carbonhydrate))
		print ("|      Fat:{0}g  ,  Sugars:{1}mg  ,  Fiber:{2}mg     ".format(self.fat,self.sugars,self.fiber))
		print ("|        Vitamins:{0} %  ".format(self.vitamins))
		print ("|  		 Electrolytes:{0} mg  ".format(self.electrolytes))
		print ("|	     Minerals: {0} mg           ".format(self.vitamins,self.electrolytes,self.minerals))
		Diet.printEmptyLines(3)
		
	def getDiet(self):
		print(self.type)
		print(self.calories)
		print(self.protein)
		print(self.carbonhydrate)
		print(self.sugars)
		print(self.fat)
		print(self.fiber)
		print(self.vitamins)
		print(self.electrolytes)
		print(self.minerals)
		
	def setID(self,userID):
		self.userID = userID
	
	def getID(self):
		return self.userID
		
	def getName(self):
		return self.name
		
	def getQuantity(self):
		return self.quantity

	def printEmptyLines(emptyLines):
		for i in range(emptyLines):
			print ("|                                                    |")
		
		
class DietReport:
	
	def __init__(self,date):
		self.date=date
		
	def setDietReport(self,case,id,diet):
	# Method that sets the dietReport instances attributes with values
		
		if (case == "new"):	
			
			#0.Variables 
			
			##a. Initialize dietReport variables 
			
			self.setID(id)
			
			###attributes initialization 
			self.calories = 0
			self.protein = 0
			self.carbonhydrates = 0 
			self.sugars = 0
			self.fat = 0
			self.fiber = 0
			
			self.meals=0
			self.beverages=0
			self.supplements=0
			
			##b. Initialize check stats calories variables 
			#"calories"(0),"protein"(1),"fat"(2),"carbs"(3),"fiber"(4)
			#"sugars"(5),"sodium"(6),"potassium"(7),"calcium"(8),"iron"(9)
			#"vitaminADailyIntake"(10),"vitaminCDailyIntake"(11)
			self.dietReportStatus = [0] * 12
			self.dietReportCode = 0
			self.dietReportMessage = ""
			
			### statCodes -> "calories"(0),"protein"(1),"fat"(2),"carbs"(3),"fiber"(4)
			self.missing = [0] * 5  ###missing stat 
			self.exceeded = [0] * 5 ###exceeded stat
			self.balance = [0] * 5  ###balance variable
			
	
		##count the amount of diet insertions types
		if   (diet.type=="meal"):
			self.meals = diet.quantity + self.meals
		elif (diet.type=="beverage"):
			self.beverages = diet.quantity + self.beverages
		elif (diet.type=="supplement"):
			self.supplements = diet.quantity + self.supplements
		
		##set diet stats
		self.calories = diet.calories*diet.quantity + self.calories
		self.protein = diet.protein*diet.quantity + self.protein
		self.carbonhydrates = diet.carbonhydrate*diet.quantity + self.carbonhydrates  
		self.sugars = diet.sugars*diet.quantity + self.sugars  
		self.fat = diet.fat*diet.quantity + self.fat  
		self.fiber = diet.fiber*diet.quantity + self.fiber 
		
		self.setVitamins(case,diet.vitamins,diet.quantity)
		self.setElectrolytes(case,diet.electrolytes,diet.quantity)
		self.setMinerals(case,diet.minerals,diet.quantity)
		
		self.checkReport()
		
	def setVitamins(self,case,vitamins,quantity):
	# Method that parses and sets vitamins from the vitamins string of the diet instance
		if (case == "new"):
			
			#attributes initialization
			self.vitaminADailyIntake = 0
			self.vitaminCDailyIntake = 0
		
		if vitamins!="No":
			tempListOfVitamins = vitamins.split(',')
		
			for i in range (len(tempListOfVitamins)):
				tempVitamin = tempListOfVitamins[i].split(':')[0]
				tempPrice = tempListOfVitamins[i].split(':')[1]
			
				if tempVitamin=="A":
					self.vitaminADailyIntake = float(tempPrice)*quantity + self.vitaminADailyIntake
				elif tempVitamin=="C":
					self.vitaminCDailyIntake = float(tempPrice)*quantity + self.vitaminCDailyIntake

	def setElectrolytes(self,case,electrolytes,quantity):
	# Method that parses and sets electrolytes from the electrolytes string of the diet instance
		
		if (case == "new"):	
			#attributes initialization
			self.sodium = 0
			self.potassium = 0
		
		if electrolytes!="No":
			tempListOfElectrolytes = electrolytes.split(',')	
			
			for i in range(len(tempListOfElectrolytes)):

				tempElectrolyte = tempListOfElectrolytes[i].split(':')[0]
				tempPrice = tempListOfElectrolytes[i].split(':')[1]

				if tempElectrolyte=="Sodium":
					self.sodium = float(tempPrice)*quantity + self.sodium
				elif tempElectrolyte=="Potassium":
					self.potassium = float(tempPrice)*quantity + self.potassium

	def setMinerals(self,case,minerals,quantity):
	# Method that parses and sets minerals from the minerals string of the diet instance
	
		if (case == "new"):
			#attributes initialization
			self.calcium = 0
			self.iron = 0
			
		if minerals!="No":
			tempListOfMinerals = minerals.split(',')
		
			for i in range(len(tempListOfMinerals)):
				tempMineral = tempListOfMinerals[i].split(':')[0]
				tempPrice = tempListOfMinerals[i].split(':')[1]

				if tempMineral=="Calcium":
					self.calcium = float(tempPrice)*quantity + self.calcium
				elif tempMineral=="Iron":
					self.iron = float(tempPrice)*quantity + self.iron	
					
	def checkReport(self):
	# Method that creates the diet report status
	
		#1. Get daily intake stats 
		
		## daily intake = [calorieIntake,proteinIntake,fiberIntake,carbsIntake,fatIntake,ironIntake]
		dialyIntake = self.getDailyIntake()
		
		#2. Get time thresholds
		
		lower,upper = self.checkTime(0)
		
		#3. Check stats based on calories for that timezome
		
		
		print ("|          Calculating timezone Intakes...           |")
		time.sleep(1)
		Diet.printEmptyLines(1)
		
		##statCodes -> "calories"(0),"protein"(1),"fat"(2),"carbs"(3),"fiber"(4)
		for i in range(5):
			
			checkStat = {
						0:self.calories,
						1:self.protein,
						2:self.fat,
						3:self.carbonhydrates,
						4:self.fiber
					   }[i]
		
			self.checkCalorieStat(dialyIntake[i],i,checkStat,lower,upper)	
	
		Diet.printEmptyLines(3)
		
		#4. Check other stats
		
		##statCodes -> "sugars"(5),"sodium"(6),"potassium"(7),"calcium"(8),"iron"(9)
		for i in range(5,10):
			
			checkStat = {
						5:self.sugars,
						6:self.sodium,
						7:self.potassium,
						8:self.calcium,
						9:self.iron
					   }[i]
		
			self.checkOtherStat(dialyIntake[i],i,checkStat)
		
		#5. Check vitamins 

		##statCodes -> "vitaminADailyIntake"(10),"vitaminCDailyIntake"(11)
		
		if (self.vitaminADailyIntake < 70):
			self.dietReportStatus[10] = -1

		elif (self.vitaminADailyIntake > 70):
			self.dietReportStatus[10] = 1
			
		if (self.vitaminCDailyIntake < 70):
			self.dietReportStatus[11] = -1

		elif (self.vitaminCDailyIntake > 70):
			self.dietReportStatus[11] = 1
			
			
		#6. Create dietReportStatus code 
		
		self.createCode()
			
			
	def checkTime(self,mode):
	# Method that returns upper and lower limits of each timezone
	
		#1. Setting time thresholds 
		currentTime = datetime.datetime.now()
	
		##Time thresholds 
		breakfastThreshold = currentTime.replace(hour = 10, minute=30, second=0, microsecond=0)
		snackThreshold = currentTime.replace(hour = 12, minute=30, second=0, microsecond=0)
		lunchThreshold = currentTime.replace(hour = 15, minute=30, second=0, microsecond=0)
		snack2Threshold = currentTime.replace(hour = 19, minute=0, second=0, microsecond=0)
		dinnerThreshold = snack2Threshold
	
		#2. Checking stats intake for each period of time of the day
	
		##Check if breakfast 
		if (currentTime < breakfastThreshold):
			if mode==0:
				return 18.18,20
			elif mode==1:
				return "10.30am"
			
		##Check if snack
		if (currentTime > breakfastThreshold)&(currentTime < snackThreshold):
			if mode==0:
				return 6.66,9.09
			elif mode==1:
				return "12.30am"
				
		##Check if  lunch
		if (currentTime > snackThreshold) & (currentTime < lunchThreshold):
			if mode==0:
				return 31.81,33.3
			elif mode==1:
				return "3.30pm"
			
		##Check if snack
		if (currentTime > lunchThreshold) & (currentTime < snack2Threshold):
			if mode==0:
				return 6.66,9.09
			elif mode==1:
				return "7.00pm"
				
		#Check if dinner
		if (currentTime > dinnerThreshold):
			if mode==0:
				return 31.81,33.3
			elif mode==1:
				return "after 7.00pm"

	def getDailyIntake(self):
	# Method that returns normal calories intake for the day
		
		#0. Daily intakes vector
		dailyIntake=[]
		
		#1. Get the certain patients body specifications
	
		df = pd.read_csv('insertedPatients.csv',sep=",")
		result = df[df['UserID'] == self.id]
		
		##Getting the values from the csv "database" file 
		tempGender = result.values[0,3]
	
		tempBirth = result.values[0,4]
		tempBirth = time.strptime(tempBirth, '%d/%m/%Y')
		tempDateNow = date.today()#.strftime("%d/%m/%Y")
		
		
		tempAge =  tempDateNow.year - tempBirth.tm_year - ((tempDateNow.month,tempDateNow.day)<(tempBirth.tm_mon,tempBirth.tm_mday))

		
		tempHeight = int(result.values[0,5])
		tempHeight = tempHeight/100 
		tempWeight = float(result.values[0,6])
	
		#2. Setting body mass index to qualify if the weight of the patient is healthy
		tempBMI = tempWeight/tempHeight**2
		tempBMIStatus = None

	
		if (tempBMI<18):
			tempBMIStatus = "underweight"

		elif (tempBMI>18)&(tempBMI<25):
			tempBMIStatus = "normal"
	
		elif (tempBMI>25):
			tempBMIStatus = "overweight"

		##Weight goal for the certain height and gender
		if (tempBMIStatus != "normal"):
			tempWeightGoal = 30.5*tempHeight**2
		else:
			tempHeight = tempHeight*100
			tempWeightGoal = tempWeight
		
		calorieIntake = 0
		
		#3. Setting normal calorie intake for weight goal # Revised Harris-Benedict Equation
		
		if (tempGender=="female"):
			calorieIntake = 9.247*tempWeightGoal + 3.098*tempHeight - 4.330*tempAge + 447.593

		elif (tempGender=="male"):
			calorieIntake = 13.397*tempWeightGoal + 4.799*tempHeight - 5.677*tempAge + 88.362
		
		## Appending the calorie intake in the dailyIntake vector
		dailyIntake.append(calorieIntake)
		
		
		#4. Setting normal protein intake 
		if (tempGender=="female"):
			proteinCalories = 12*calorieIntake/100 # Protein must be 12% - 20% of daily calories 
			proteinIntake = proteinCalories/4 #Protein calories -> protein grams 
			
		elif (tempGender=="male"):
			proteinCalories = 20*calorieIntake/100 # Protein must be 12% - 20% of daily calories 
			proteinIntake = proteinCalories/4 #Protein calories -> protein grams
		
		## Appending the protein intake in the dailyIntake vector
		dailyIntake.append(proteinIntake)
		
		#5. Setting normal fat intake 
		fatCalories = 30*calorieIntake/100 # Fat must be 50% - 60% of daily calories 
		fatIntake = fatCalories/9 #Fat calories -> Fat grams 
		
		## Appending the fat intake in the dailyIntake vector
		dailyIntake.append(fatIntake)
		
		
		#6. Setting normal carbonhydrate intake 
		if (tempGender=="female"):
			carbsCalories = 50*calorieIntake/100 # Carbonhydrate must be 50% - 60% of daily calories 
			carbsIntake = carbsCalories/4 #Carbonhydrate calories -> Carbonhydrate grams 
			
		elif (tempGender=="male"):
			carbsCalories = 60*calorieIntake/100 # Carbonhydrate must be 50% - 60% of daily calories 
			carbsIntake = carbsCalories/4 #Carbonhydrate calories -> Carbonhydrate grams
		
		## Appending the carbonhydrate intake in the dailyIntake vector
		dailyIntake.append(carbsIntake)
		
		
		#7. Setting the fiber intake codes for later check
		fiberIntake = 14*calorieIntake/1000
		
		## Appending the fiber intake in the dailyIntake vector
		dailyIntake.append(fiberIntake)
		
		

		#8. Setting normal sugars intake 
		## Normal sugar intake is 38grams -> checkMeal() method
		dailyIntake.append(38)
		
		#9. Setting normal sodium intake 
		## Normal sodium intake is 1000mg -> checkMeal() method
		dailyIntake.append(1000)
		
		#10. Setting normal potassium intake 
		## Normal potassium intake is 3500mg -> checkMeal() method
		dailyIntake.append(3500)
		
		#11. Setting normal calcium intake 
		## Normal calcium intake is 500mg -> checkMeal() method
		dailyIntake.append(500)
		
		#12. Setting normal iron intake 
		
		if(tempAge>1)&(tempAge<3):
			ironIntake = 7
		
		elif(tempAge>4)&(tempAge<8):
			ironIntake = 10		
		
		if (tempGender=="female"):
			if(tempAge>9)&(tempAge<13):
				ironIntake = 8
			elif(tempAge>14)&(tempAge<18):
				ironIntake = 15
			elif(tempAge>19)&(tempAge<50):
				ironIntake = 18
			elif(tempAge>51):
				ironIntake = 8
			 
		elif (tempGender=="male"):
			if(tempAge>9)&(tempAge<13):
				ironIntake = 8
			elif(tempAge>14)&(tempAge<18):
				ironIntake = 11
			elif(tempAge>19):
				ironIntake = 8 
		
		## Appending the iron intake in the dailyIntake vector
		dailyIntake.append(ironIntake)

		#12. Print daily intakes 
		print ("|             Computing Daily Intakes...             |")
		time.sleep(1)
		Diet.printEmptyLines(1)
		print ("| Calories:{0}kcal ,  Protein:{1}g ,  Carbs:{2}g  ".format(round(calorieIntake,2),round(proteinIntake,2),round(carbsIntake,2)))
		print ("|      Fat:{0}g  ,  Sugars:38mg  ,  Fiber:{1}mg   ".format(round(fatIntake,2),round(fiberIntake,2)))
		print ("|  	     Sodium:1000mg  ,  Potassium:3500mg        ")
		print ("|	        Calcium:500mg  ,  Iron:{0}mg              ".format(round(ironIntake,2)))
		Diet.printEmptyLines(3)
		
		#13. Return the daily intakes vector 
		
		##daily intake = [calorieIntake,proteinIntake,fiberIntake,carbsIntake,fatIntake,ironIntake]
		return dailyIntake
		
			
	def checkCalorieStat(self,dailyIntake,stat,checkStat,lower,upper):
	# Method that checks stats status
		
		## Setting stat name for print 
		
		name = self.getType(stat)
		time = self.checkTime(1)
		
		## Setting balance 
		if self.missing[stat] > 0: 
			self.balance[stat] = self.missing[stat]
		
		elif self.exceeded[stat] > 0:
			self.balance[stat] = - self.exceeded[stat]
		
		## Setting meal calories thresholds 
		upperThreshold = upper*( dailyIntake + self.balance[stat] )/100
		lowerThreshold = lower*( dailyIntake + self.balance[stat] ) /100 
		
		if (checkStat < lowerThreshold):
			self.dietReportStatus[stat] = -1
			self.missing[stat] = lowerThreshold - checkStat
			print ("|   You still have {0}/{1}{2} till {3}            ".format(round(self.missing[stat],2),round(lowerThreshold,2),name,time))
			
		elif (checkStat > lowerThreshold)&(checkStat < upperThreshold) :
			self.dietReportStatus[stat] = 0
			self.missing[stat] = 0
			self.exceeded[stat] = 0
			print ("|   You consumed the {0}{1} till {2}            ".format(round(checkStat,2),name,time))
			
		elif (checkStat > upperThreshold):
			self.dietReportStatus[stat] = 1
			self.exceeded[stat] = checkStat - upperThreshold
			print ("|  You consumed {0}/{1}{2} more than normal till {3} ".format(round(self.exceeded[stat],2),round(upperThreshold,2),name,time))


	def checkOtherStat(self,dailyIntake,stat,checkStat):
	# Method that checks the rest of the stats 
		
		threshold = (10 * dailyIntake)/100 
		
		if checkStat < dailyIntake - threshold :  
			self.dietReportStatus[stat] = -1
			
		elif (checkStat > dailyIntake - threshold) & (checkStat < dailyIntake + threshold) :
			self.dietReportStatus[stat] = 0

		elif (checkStat > dailyIntake + threshold):
			self.dietReportStatus[stat] = 1	
	
	

	def createCode(self):
	# Method to get the dietReportStatus code
	
		#0. Variables

		##Diet message that will be shown at the end of the day
		tempMessage = [] 
		
		## dietReportStatus code that will be send it HealthStatus
		## 0. Normal , 1. Increased fat consumption, 2. Low levels of vitamins,electrolytes and minerals
		## 3. Increased sugars consumption, 4. Increased calories consumption, 5. Low fibers levels
		tempCode = [] 
		
		
		## positions in the dietReportStatus vector
		
		###"calories"(0),"protein"(1),"fat"(2),"carbs"(3),"fiber"(4)
		###"sugars"(5),"sodium"(6),"potassium"(7),"calcium"(8),"iron"(9)
		###"vitaminADailyIntake"(10),"vitaminCDailyIntake"(11)
		
		## variables for each stats code 
		
		### calories based variables
		caloriesCode = self.dietReportStatus[0] 
		proteinCode = self.dietReportStatus[1] 
		fatCode = self.dietReportStatus[2] 
		carbsCode = self.dietReportStatus[3] 
		fiberCode = self.dietReportStatus[4] 
		sugarsCode = self.dietReportStatus[5]
		
		### electrolytes
		sodiumCode = self.dietReportStatus[6]
		potassiumCode = self.dietReportStatus[7]
		
		### minerals
		calciumCode = self.dietReportStatus[8]
		ironCode = self.dietReportStatus[9]
		
		### vitamins
		vitaminACode = self.dietReportStatus[10]
		vitaminCCode = self.dietReportStatus[11]
		#1. Getting the code of the calories related variables
		
		## -1: low , 0: OK  , 1: high 
		
		if  (caloriesCode == -1):
			tempMessage.append("Calories of the time zone not reached!")
			
			if   (proteinCode == -1):
			
				if   (carbsCode == -1):
									
					if (fatCode == 1):
						tempMessage.append("Increased fat consumption!") 
						tempCode.append(1)
				
				elif (carbsCode == 0):
					
					if   (fatCode == -1):
						tempMessage.append("Increase protein and fat consumption!")
						
					elif (fatCode == 0):
						tempMessage.append("Increase protein consumption!")
						
					elif (fatCode == 1):
						tempMessage.append("Increase protein consumption and reduce fat!")
						tempCode.append(1)
					
				elif (carbsCode == 1):
				
					if   (fatCode == -1):
						tempMessage.append("Reduce carbs consumption and increase fat!")
					
					elif (fatCode == 0):
						tempMessage.append("Reduce carbs consumption!")
					
					elif (fatCode == 1):
						tempMessage.append("Reduce carbs and fat consumption!")
						tempCode.append(1)
						
			elif (proteinCode == 0):
			
				if   (carbsCode == -1):
				
					if   (fatCode == -1):
						tempMessage.append("Increase carbs and fat consumption!" )
						
					elif (fatCode == 0):
						tempMessage.append("Increase carbs consumption!")
						
					elif (fatCode == 1):
						tempMessage.append("Increase carbs consumption and reduce fat!")
						tempCode.append(1)
				
				elif (carbsCode == 0):
				
					if   (fatCode == -1):
						tempMessage.append("Increase fat consumption!")
				
				elif (carbsCode == 1):
			
					if   (fatCode == -1):
						tempMessage.append("Reduce carbs consumption and increase fat!")
			
			elif (proteinCode == 1):
				
				if   (carbsCode == -1):
				
					if   (fatCode == -1):
						tempMessage.append("Increase carbs and fat consumption!")
						
					elif (fatCode == 0):
						tempMessage.append("Increase carbs consumption!")
				
				elif (carbsCode == 0):
				
					if   (fatCode == -1):
						tempMessage.append("Increase fat consumption!")
				
				elif (carbsCode == 1):
				
					if   (fatCode == -1):
						tempMessage.append("Reduce carbs consumption and increase fat!") 
		
		elif(caloriesCode == 0):
			
			tempMessage.append("Calories of the time zone reached!")
			
			if   (proteinCode == -1):
				
				if   (carbsCode == -1):
									
					if (fatCode == 1):
						tempMessage.append("Increase protein and carbs consumption and reduce fat!")
						tempCode.append(1)
						
				elif (carbsCode == 0):
									
					if (fatCode == 1):
						tempMessage.append("Increase protein consumption and reduce fat!")
						tempCode.append(1)
						
				elif (carbsCode == 1):
				
					if   (fatCode == -1):
						tempMessage.append("Increse protein and fat consumption and reduce carbs")
					
					elif (fatCode == 0):
						tempMessage.append("Increse protein consumption and reduce carbs")
				
			elif (proteinCode == 0):
				
				if   (carbsCode == -1):
				
					if (fatCode == 1):
						tempMessage.append("Increase carbs consumption and reduce fat!")
						tempCode.append(1)
									
				elif (carbsCode == 1):
				
					if   (fatCode == -1):
						tempMessage.append("Reduce carbs consumption and increase fat!")
			
			elif (proteinCode == 1):
				
				if   (carbsCode == -1):
				
					if   (fatCode == -1):
						tempMessage.append("Increase carbs and fat consumption!")
						
					elif (fatCode == 0):
						tempMessage.append("Increase carbs consumption!")
					
					elif (fatCode == 1):
						tempMessage.append("Increase carbs and reduce fat !")
						tempCode.append(1)
						
				elif (carbsCode == 0):
				
					if   (fatCode == -1):
						tempMessage.append("Increase fat consumption!")
				
				elif (carbsCode == 1):
				
					if   (fatCode == -1):
						tempMessage.append("Increase fat consumption!")
						
		elif(caloriesCode == 1):
			
			tempMessage.append("Calories of the time zone exceeded!")
			tempCode.append(4)
			
			if   (proteinCode == -1):
			
				if   (carbsCode == -1):
					
					if (fatCode == 1):
						tempMessage.append("Increase protein and carbs consumption and reduce fat!")
						tempCode.append(1)
						
				elif (carbsCode == 0):
					
					if (fatCode == 1):
						tempMessage.append("Increase protein consumption and reduce fat!")
						tempCode.append(1)
				
				elif (carbsCode == 1):
				
					if   (fatCode == -1):
						tempMessage.append("Increase protein and fat consumption and reduce carbs!")
						
					elif (fatCode == 0):
						tempMessage.append("Increase protein consumption and reduce carbs!")
						
					elif (fatCode == 1):
						tempMessage.append("Increase protein consumption and reduce carbs and fat!")
						tempCode.append(1)
						
			elif (proteinCode == 0):
			
				if   (carbsCode == -1):
				
					if (fatCode == 1):
						tempMessage.append("Increase carbs consumption and reduce fat!")
						tempCode.append(1)
						
				elif (carbsCode == 0):

					if (fatCode == 1):
						tempMessage.append("Decrease fat consumption!")
						tempCode.append(1)
				
				elif (carbsCode == 1):
				
					if   (fatCode == -1):
						tempMessage.append("Decrease carbs consumption and increase fat!")
						
					elif (fatCode == 0):
						tempMessage.append("Decrease carbs consumption!")
						
					elif (fatCode == 1):
						tempMessage.append("Decrease carbs and fat consumption!")
						tempCode.append(1)
						
			elif (proteinCode == 1):
				
				if   (carbsCode == -1):
				
					if   (fatCode == -1):
						tempMessage.append("Increase carbs and fat consumption!")
						
					elif (fatCode == 0):
						tempMessage.append("Increase carbs consumption!")
						
					elif (fatCode == 1):
						tempMessage.append("Increase carbs consumption and reduce fat!")
				
				elif (carbsCode == 0):
				
					if   (fatCode == -1):
						tempMessage.append("Increase fat consumption!")
						
					elif (fatCode == 1):
						tempMessage.append("Decrease fat consumption!")
						tempCode.append(1) 
						
				elif (carbsCode == 1):
				
					if   (fatCode == -1):
						tempMessage.append("Decrease carbs consumption and increase fat!")
						
					elif (fatCode == 0):
						tempMessage.append("Decrease carbs consumption!")
						
					elif (fatCode == 1):
						tempMessage.append("Increase fat consumption and reduce fat!")
						tempCode.append(1)
		
		
		#2. Getting the code of the sugars and fibers
		
		## -1: low , 0: OK  , 1: high
		
		## fiber 
		if fiberCode == -1: 
			tempMessage.append("Low fiber levels!")
			tempCode.append(5)
		
		## sugars
		if sugarsCode == 1:
			tempMessage.append("High sugars levels!")
			tempCode.append(3)
			
			
		#3. Getting the code of the electrolytes,vitamins and minerals
		
		## -1: low , 0: OK  , 1: high
		
		flag = 0 
		
		## electrolytes 
		if sodiumCode == -1 | potassiumCode == -1 | (sodiumCode == -1 & potassiumCode == -1):
			tempMessage.append("Low levels of electrolytes")
			tempCode.append(2)
			flag = 1 
	
		## vitamins
		if vitaminACode == -1 | vitaminCCode == -1 | (vitaminACode == -1 & vitaminCCode == -1):
			tempMessage.append("")
			
			if flag==0:
				tempMessage.append("Low levels of vitamins")
				tempCode.append(2)
			
			elif flag==1:
				tempMessage.append(",vitamins")
		
			flag=1 
				
		## minerals
		if calciumCode == -1 | ironCode == -1 | (calciumCode == -1 & ironCode == -1):
			tempMessage.append("")
			
			if flag==0:
				tempMessage.append("Low levels of minerals")
				tempCode.append(2)
				
			elif flag==1:
				tempMessage.append(",minerals")
		
			flag=1 	
		
		if flag==1:
			tempMessage.append("!")
		
		## code to str for join function
		for i in range(len(tempCode)):
			tempCode[i] = str(tempCode[i])
		
		self.dietReportCode = ''.join(tempCode)
		self.dietReportMessage = ''.join(tempMessage)
		
		self.printDietReportMessage()
		self.printBorder()
		
	def printDietReportMessage(self):
	
		print ("|        Creating DietReport message...              |")
		self.printEmptyLines(1)
		tempListOfMessages = self.dietReportMessage.split('!')
		
		for i in range (len(tempListOfMessages)-1):
			print("|  "+tempListOfMessages[i] + "!")
		
		self.printEmptyLines(1)
	
	
	def getAll(self):
		
		print(self.meals)
		print(self.beverages)
		print(self.supplements)
		print(self.calories)
		print(self.protein)
		print(self.carbonhydrates)
		print(self.sugars)
		print(self.fat)
		print(self.fiber)
		print(self.vitaminADailyIntake)
		print(self.vitaminCDailyIntake)
		print(self.sodium)
		print(self.potassium)
		print(self.calcium)
		print(self.iron)
		
	def getType(self,input):
	# Method that retuns stat type based on input	
		name = {
					0:"kcal Calories",
					1:"g Protein",
					2:"g Fat",
					3:"g Carbs",
					4:"g Fiber"
				}[input]
	
		return name 
		
	def getMeals(self):
		return self.meals
		
	def getBeverages(self):
		return self.beverages
		
	def getSupplements(self):	
		return self.supplements
	
	def getCalories(self):
		return self.calories
	
	def getProtein(self):
		return self.protein
		
	def getCarbonhydrates(self):
		return self.carbonhydrates
		
	def getSugars(self):
		return self.sugars
	
	def getFat(self):
		return self.fat
	
	def getFiber(self):
		return self.fiber
		
	def getVitaminA(self):
		return self.vitaminADailyIntake
	
	def getVitaminC(self):
		return self.vitaminCDailyIntake
	
	def getSodium(self):
		return self.sodium
		
	def getPotassium(self):
		return self.potassium
		
	def getCalcium(self):	
		return self.calcium
	
	def getIron(self):
		return self.iron			
	
	def setID(self,id):
		self.id = id
	
	def getID(self):
		return self.id
		
	def getDate(self):
		return self.date
	
	def getDietReportCode(self):
		return self.dietReportCode
	
	def getdietReportStatus(self):
		return self.dietReportStatus 
		
	def printEmptyLines(self,emptyLines):
		for i in range(emptyLines):
			print ("|                                                    |")
	
	def printBorder(self):
		print("======================================================")#footer	
		