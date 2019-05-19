import numpy as np
import random
import csv

class Sensor:
	def __init__(self, user, sensID):
		self.user = user
		self.sensID = sensID
		self.cacheMem = np.zeros([20, 30])
		self.cacheAv = np.zeros([20])
		self.enabled = True;

	def inputSampling(self, mcenter, mrange, option):
		if option == 1:
			# Normal distribution
			return np.random.normal(mcenter, mrange)

		elif option == 2:
			# Uniform distribution
			return np.random.uniform(mcenter, mrange)
		else:
			return random.randint(mcenter, mrange)

	def refreshCache(self, counter, array):
		self.cacheMem[:, counter] = array

	def generateCacheAv(self):
		self.cacheAv = np.mean(self.cacheMem, axis=1)

	def cacheAvSavePersixH(self,count):
		row = [count,self.user,self.cacheAv[0],self.cacheAv[1],self.cacheAv[2],self.cacheAv[3],
		self.cacheAv[4],self.cacheAv[5],self.cacheAv[6],self.cacheAv[7],self.cacheAv[8],
		self.cacheAv[9],self.cacheAv[10],self.cacheAv[11],self.cacheAv[12],self.cacheAv[13],
		self.cacheAv[14],self.cacheAv[15],self.cacheAv[16],self.cacheAv[17],self.cacheAv[18],
		self.cacheAv[19],"Sampled Average"]

		with open('sensorsData.csv', 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(row)
		csvFile.close()


	def inputCacheDifCalc(self, a):

		result = np.zeros([a.size])

		for x in range(a.size):
			if a[x] > self.cacheAv[x]:
				
				if (float(self.cacheAv[x] != 0)):	result[x] = ((a[x] - self.cacheAv[x]) * 100) / float(self.cacheAv[x])
				else :	result[x] = ((a[x] - self.cacheAv[x]) * 100) / float(1)
			else :
		
				if (float(a[x] != 0)):	result[x] = ((self.cacheAv[x] - a[x]) * 100) / float(a[x])
				else :	result[x] = ((self.cacheAv[x] - a[x]) * 100) / float(1)
		return result

	def checkReadAbility(self):
		return self.enabled;

	def difSave():
		row1 = [count,self.user,self.cacheAv[0],self.cacheAv[1],self.cacheAv[2],self.cacheAv[3],
			self.cacheAv[4],self.cacheAv[5],self.cacheAv[6],self.cacheAv[7],self.cacheAv[8],
			self.cacheAv[9],self.cacheAv[10],self.cacheAv[11],self.cacheAv[12],self.cacheAv[13],
			self.cacheAv[14],self.cacheAv[15],self.cacheAv[16],self.cacheAv[17],self.cacheAv[18],
			self.cacheAv[19],"Difference Detected - Current Cache Average"]
		row2 = [count,self.user,currentInput[0],currentInput[1],currentInput[2],currentInput[3],
			currentInput[4],currentInput[5],currentInput[6],currentInput[7],currentInput[8],
			currentInput[9],currentInput[10],currentInput[11],currentInput[12],currentInput[13],
			currentInput[14],currentInput[15],currentInput[16],currentInput[17],currentInput[18],
			currentInput[19],"Current Input"]

		with open('sensorsData.csv', 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(row1)
			writer.writerow(row2)
		csvFile.close()

	def setAll(self,bs, gs, rs, cs, es):

		#Environments Stats ------------------
		es.temp = self.inputSampling(20,10,1) #Celsius
		es.humidity = self.inputSampling(0,100,2)
		es.co = self.inputSampling(7,2,1) #ppm
		es.co2 = self.inputSampling(550,200,1) #ppm
		es.radon = self.inputSampling(0,1,3) #0 = no radon, 1 = existing radon
		es.formaldehyde = self.inputSampling(0,1,2) #ppm
		es.airMold = self.inputSampling(200,50,1) #spores
		es.asbesto = self.inputSampling(80,60,1) #fibres/1000litre of air
		es.airParticles = self.inputSampling(0,50,3) #pm2.5
		es.light = self.inputSampling(0,32000,3) #Lux

		#Blood Stats -------------------------
		bs.bol = round(self.inputSampling(95,5,1)) #mm Hg
		bs.bg = self.inputSampling(6,1,1) #mmol/L

		#General Stats -----------------------
		gs.bt = self.inputSampling(36.5,1,1) #Celsius
		gs.skinPerspiration = self.inputSampling(0, 1, 3) #0 dry ,1 sweaty

		#Respiration Stats -------------------
		rs.rp = round(self.inputSampling(15,3,1)) #Breaths/min
		rs.respirationSounds = self.inputSampling(1,6,3) #1-2 low sound,3-4 normal sound,5-6 loud sound

		#Cardiac Stats -----------------------
		cs.ecg = self.inputSampling(1,6,3) #1-2 normal,3-4 irregular rythm,5-6 axis deviation
		cs.hr = self.inputSampling(50,190,2) #Beats/min
		cs.sysBP = self.inputSampling(70,200,2) #mm Hg
		cs.diaBP = self.inputSampling(40,100,2) #mm Hg


class BodySensor(Sensor):
	def __init__(self, user, sensID):
		Sensor.__init__(self, user, sensID)


class BloodSensor(BodySensor):
	def __init__(self, user, sensID):
		BodySensor.__init__(self, user, sensID)
		self.bol = None
		self.bolStat = None
		self.bg = None
		self.bgstat = None

	def printValues(self):
		print("BOL (Blood Oxygen Level):", self.bol, "%")
		print("BG (Blood Glucose): ", self.bg, "mmol/L")


class GeneralSensor(BodySensor):
	def __init__(self, user, sensID):
		BodySensor.__init__(self, user, sensID)
		self.bt = None
		self.btStat = None
		self.skinPerspiration = None
		self.skinPerpStat = None

	def printValues(self):
		print("BT (Body Temperature):", self.bt, "C")
		print("Skin Perspiration: ", self.skinPerspiration, "g/min * m2")


class RespiratorySensor(BodySensor):
	def __init__(self, user, sensID):
		BodySensor.__init__(self, user, sensID)
		self.rp = None
		self.rpStat = None
		self.respirationSounds = None
		self.respiSoundsStat = None

	def printValues(self):
		print("RP (Respiration Rate):", self.rp, "breaths/min")
		print("Respiration Sounds: ", self.respiSoundsStat)


class CardiacSensor(BodySensor):
	def __init__(self, user, sensID):
		BodySensor.__init__(self, user, sensID)
		self.ecg = None
		self.ecgstat = None
		self.hr = None
		self.hrstat = None
		self.sysBP = None
		self.sysBPStat = None
		self.diaBP = None
		self.diaBPStat = None

	def checkBloodPressureStatus(self):
		if self.sysBPStat == 1 and self.diaBPStat == 1:
			return "Normal"
		else:
			return "Abnormal"

	def printValues(self):
		print("ECG:", self.ecg)
		print("HR (Heart Rate): ", self.hr, "beats/min")
		print("BP (Blood Pressure): ", self.checkBloodPressureStatus())
		print("		Systolic mm Hg (upper number): ", self.sysBP)
		print("		Diastolic mm Hg (lower number): ", self.diaBP)


class EnvironmentalSensor(Sensor):
	def __init__(self, user, sensID):
		Sensor.__init__(self, user, sensID)
		self.temp = None
		self.humidity = None
		self.co = None
		self.co2 = None
		self.radon = None
		self.formaldehyde = None
		self.airMold = None
		self.asbesto = None
		self.airParticles = None
		self.light = None

	def printValues(self):
		print("TEMP:", self.temp, "C")
		print("HUMIDITY: ", self.humidity)
		print("CO: ", self.co, "ppm")
		print("CO2: ", self.co2, "ppm")
		print("RABON: ", self.radon)
		print("FORMALDEHYDE: ", self.formaldehyde, "ppm")
		print("SPORES: ", self.airMold, "spores")
		print("ASBESTO: ", self.asbesto, "fibres/1000 litre of air")
		print("AIR PARTICLES: ", self.airParticles, "pm2.5")
		print("LIGHT: ", self.light, "Lux")


class CurrentStatus:
	def __init__(self, bs, gs, rs, cs, es):
		#normal = 1, abnormal = 0
		#Blood Stats -------------------------
		bs.bolStat = 1 if (bs.bol > 90) and (bs.bol<105) else 0
		bs.bgstat = 1 if (bs.bg > 4) and (bs.bg < 7.8) else 0

		# General Stats -----------------------
		gs.btStat = 1 if (gs.bt > 35.9) and (gs.bt < 37.6) else 0
		if (gs.skinPerspiration == 1) and (cs.hr > 114 or es.temp > 25):
			gs.skinPerpStat = 1
		elif (gs.skinPerspiration == 1) and (cs.hr < 100 or es.temp < 25):
			gs.skinPerpStat = 0
			
		# Respiration Stats -------------------
		rs.rpStat = 0 if ((rs.rp > 18 and bs.bol < 90) or (rs.rp < 12 and bs.bol > 105)) else 1
		rs.respiSoundsStat = 1 if (rs.respirationSounds < 5) else 0

		# Cardiac Stats -----------------------
		cs.ecgstat = 1 if cs.ecg < 3 else 0
		cs.hrstat = 1 if (cs.hr > 114 and cs.sysBP > 120 and cs.sysBP < 200) or (cs.hr < 100 and cs.sysBP < 125) else 0
		cs.sysBPStat = 1 if (cs.hr< 100 and (cs.sysBP > 90 and cs.sysBP<120) and (cs.sysBP - cs.diaBP) < 30) or (cs.hr>114 and cs.sysBP > 120 and cs.sysBP < 200 and cs.diaBP>60 and cs.diaBP<80) else 0
		cs.diaBPStat = cs.sysBPStat

	def checkAllReadAbility(self, generalSensor, cardiacSensor, respiratorySensor, bloodSensor):
		if bloodSensor.checkReadAbility() and generalSensor.checkReadAbility() and cardiacSensor.checkReadAbility() and respiratorySensor.checkReadAbility():
			return True
		else:
			return False

	def getNewValues(self, bs, gs, rs, cs, es, sensor):
		sensor.setAll(bs, gs, rs, cs, es)