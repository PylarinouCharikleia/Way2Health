import pandas
from datetime import date
from Diet import *
from User import *
import pandas as pd
import csv
import time

class MedicalReport:

	def __init__(self,date):
		self.date = date

		#Initializations		
		self.cmp = 0	
		self.hdl = 0
		self.ldl = 0
		self.urineColor = 0
		self.urineClarity = 0	
		self.specificGravity = 0	
		self.pH = 0
		self.protein = 0
		self.glucose = 0	
		self.ketones = 0 	
		self.crystals = 0
		self.bacteria = 0
		self.blood = 0
		self.lft = 0
		self.uANDe = 0
		self.totBilrubin = 0
		self.alt = 0
		self.ast = 0
		self.ggt = 0
		self.Albumin = 0
		self.fiveNeuclotidase = 0
		self.ceruloplasmin = 0
		self.afp = 0
		self.serumGlucose = 0
		self.lactateDehyfrogenase = 0
		self.carotene = 0
		self.vitaminA = 0
		self.vitaminB1 = 0
		self.vitaminB2 = 0	
		self.vitaminB3 = 0
		self.vitaminB5 = 0
		self.vitaminB6 = 0
		self.vitaminB12 = 0
		self.vitaminD25Hydroxy = 0
		self.vitaminE = 0
		self.vitaminK = 0
		self.folicAcid = 0
		self.tsh = 0
		self.t3 = 0
		self.t4 = 0
		self.freeT4 = 0
		self.cpr = 0
		self.esr = 0
		self.cbc = 0
		self.inr = 0
		self.wbc = 0
		self.rbc = 0
		self.hmc = 0
		self.plt = 0		

	
	def getMessage(self):

		#Thyroid Check
		#1 = ok ,2 = hyperthyroidism,3 hypothyriodism
		if (self.tsh> 0.5 and (self.tsh<5.0 or self.tsh == 5.0)):
			thyroid = 1	
		elif (self.tsh<0.4):
			thyroid = 2
		elif (self.tsh>5.0):
			thyroid = 3
			
		#LDL Check
		#1 = ok, 2 = high
		if (self.ldl> 2.0 and self.ldl<2.5):
			ldl = 1	
		elif (self.ldl>2.5):
			ldl = 2		

		#HDL Check
		#1 = ok, 2 = low
		if (self.hdl>1.6):
			ldl = 1	
		elif (self.hdl<1.6 and self.hdl>0.9):
			ldl = 2	

		
		if (thyroid == 1 and ldl == 1 and hdl == 1):
			self.message = 1

		elif (thyroid == 2):
			self.message = 2
		
		elif (thyroid == 3):
			self.message = 3
		
		elif (ldl == 2):
			self.message = 4
		
		elif (hdl == 2):
			self.message = 5
	


	def setMedicalReport(self,id,exam):
	# Method that sets the medicalReport instances attributes with values
	
		if (exam.name == "metabolism"):
			values = exam.getMetabolism()
			self.setMetabolism(values)
			
		elif (exam.name == "heart"):
			values = exam.getHeart()
			self.setHeart(values[0],values[1])

		elif (exam.name == "urinary"):
			values = exam.getUrinarySystem()
			self.setUrinarySystem(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9])

		elif (exam.name == "liver"):
			values = exam.getLiver()
			self.setLiver(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11])

		elif (exam.name == "vitamins"):
			values = exam.getVitamins()
			self.setVitamins(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11])

		elif (exam.name == "thyroid"):
			values = exam.getThyroid()
			self.setThyroid(values[0],values[1],values[2],values[3])

		elif (exam.name == "immune"):
			values = exam.getImmuneSystem()
			self.setImmuneSystem(values[0],values[1])

		elif (exam.name == "generalblood"):
			values = exam.getGeneralBlood()
			self.setGeneralBlood(values[0],values[1],values[2],values[3],values[4],values[5])
		
		self.setID(id)


	def setID(self,id):
		self.id = id		
	
	
	def setMetabolism(self,cmp):
		self.cmp = cmp	
 
	def setHeart(self,hdl,ldl):
		self.hdl = hdl
		self.ldl = ldl

	def setUrinarySystem(self,urineColor,urineClarity,specificGravity,pH,protein,glucose,ketones,crystals,bacteria,blood):
	
		self.urineColor = urineColor
		self.urineClarity = urineClarity	
		self.specificGravity = specificGravity	
		self.pH = pH
		self.protein = protein
		self.glucose = glucose	
		self.ketones = ketones 	
		self.crystals = crystals
		self.bacteria = bacteria
		self.blood = blood

	def setLiver(self,lft,uANDe,totBilrubin,alt,ast,ggt,Albumin,fiveNeuclotidase,ceruloplasmin,afp,serumGlucose,lactateDehyfrogenase):

		self.lft = lft
		self.uANDe = uANDe
		self.totBilrubin = totBilrubin
		self.alt = alt
		self.ast = ast
		self.ggt = ggt
		self.Albumin = Albumin
		self.fiveNeuclotidase = fiveNeuclotidase
		self.ceruloplasmin = ceruloplasmin
		self.afp = afp
		self.serumGlucose = serumGlucose
		self.lactateDehyfrogenase = lactateDehyfrogenase

	def setVitamins(self,carotene,vitaminA,vitaminB1,vitaminB2,vitaminB3,vitaminB5,vitaminB6,vitaminB12,vitaminD25Hydroxy,vitaminE,vitaminK,folicAcid):

		self.carotene = carotene
		self.vitaminA = vitaminA
		self.vitaminB1 = vitaminB1
		self.vitaminB2 = vitaminB2	
		self.vitaminB3 = vitaminB3
		self.vitaminB5 = vitaminB5
		self.vitaminB6 = vitaminB6
		self.vitaminB12 = vitaminB12
		self.vitaminD25Hydroxy = vitaminD25Hydroxy
		self.vitaminE = vitaminE
		self.vitaminK = vitaminK
		self.folicAcid = folicAcid

	def setThyroid(self,tsh,t3,t4,freeT4):
		
		self.tsh = tsh
		self.t3 = t3
		self.t4 = t4
		self.freeT4 = freeT4

	def setImmuneSystem(self,cpr,esr):
	
		self.cpr = cpr
		self.esr = esr
		
	def setGeneralBloodTest(self,cbc,inr,wbc,rbc,hmc,plt):

		self.cbc = cbc
		self.inr = inr
		self.wbc = wbc
		self.rbc = rbc
		self.hmc = hmc
		self.plt = plt
	
	def setID(self,id):
		self.id = id	
	
	def getAll(self):
		return self.cmp,self.hdl,self.ldl,self.urineClarity,self.specificGravity,self.pH,self.protein,self.glucose,self.ketones,self.crystals,self.bacteria,self.blood,self.lft,self.uANDe,self.totBilrubin,self.alt,self.ast,self.ggt,self.Albumin,self.fiveNeuclotidase,self.ceruloplasmin,self.afp,self.serumGlucose,self.lactateDehyfrogenase,self.carotene,self.vitaminA,self.vitaminB1,self.vitaminB2,self.vitaminB3,self.vitaminB5,self.vitaminB6,self.vitaminB12,self.vitaminD25Hydroxy,self.vitaminE,self.vitaminK,self.folicAcid,self.tsh,self.t3,self.t4,self.freeT4,self.cpr,self.esr,self.cbc,self.inr,self.wbc,self.rbc,self.hmc,self.plt

class Exam:

	def __init__(self,name):
		self.name = name
	
	def setID(self,id):
		self.id = id 
		
	def getID(self):
		return self.id
	
	def getName(self):
		return self.name


class Metabolism(Exam):

	def __init__(self,name):
		Exam.__init__(self,name)

	def setMetabolism(self,cmp):
		self.cmp = cmp	
	
	def getMetabolism(self):
		return self.cmp	


class Heart(Exam):
	
	def __init__(self,name):
		Exam.__init__(self, name)

	def setHeart(self,hdl,ldl):
		self.hdl = hdl
		self.ldl = ldl
	
	def getHeart(self):
		return self.hdl, self.ldl

class UrinarySystem(Exam):

	def __init__(self,name):
		Exam.__init__(self, name)
	
	def setUrinarySystem(self,urineColor,urineClarity,specificGravity,pH,protein,glucose,ketones,crystals,bacteria,blood):
	
		self.urineColor = urineColor
		self.urineClarity = urineClarity	
		self.specificGravity = specificGravity	
		self.pH = pH
		self.protein = protein
		self.glucose = glucose	
		self.ketones = ketones 	
		self.crystals = crystals
		self.bacteria = bacteria
		self.blood = blood
	
	def getUrinarySystem(self):
		return self.urineColor,self.urineClarity,self.specificGravity,self.pH,self.protein,self.glucose,self.ketones,self.crystals,self.bacteria,self.blood

class Liver(Exam):
	
	def __init__(self,name):
		Exam.__init__(self, name)


	def setLiver(self,lft,uANDe,totBilrubin,alt,ast,ggt,Albumin,fiveNeuclotidase,ceruloplasmin,afp,serumGlucose,lactateDehyfrogenase):

		self.lft = lft
		self.uANDe = uANDe
		self.totBilrubin = totBilrubin
		self.alt = alt
		self.ast = ast
		self.ggt = ggt
		self.Albumin = Albumin
		self.fiveNeuclotidase = fiveNeuclotidase
		self.ceruloplasmin = ceruloplasmin
		self.afp = afp
		self.serumGlucose = serumGlucose
		self.lactateDehyfrogenase = lactateDehyfrogenase
	
	def getLiver(self):
		return self.lft,self.uANDe,self.totBilrubin,self.alt,self.ast,self.ggt,self.Albumin,self.fiveNeuclotidase,self.ceruloplasmin,self.afp,self.serumGlucose,self.lactateDehyfrogenase
	
class Vitamins(Exam):

	def __init__(self,name):
		Exam.__init__(self, name)
	
	def setVitamins(self,carotene,vitaminA,vitaminB1,vitaminB2,vitaminB3,vitaminB5,vitaminB6,vitaminB12,vitaminD25Hydroxy,vitaminE,vitaminK,folicAcid):

		self.carotene = carotene
		self.vitaminA = vitaminA
		self.vitaminB1 = vitaminB1
		self.vitaminB2 = vitaminB2	
		self.vitaminB3 = vitaminB3
		self.vitaminB5 = vitaminB5
		self.vitaminB6 = vitaminB6
		self.vitaminB12 = vitaminB12
		self.vitaminD25Hydroxy = vitaminD25Hydroxy
		self.vitaminE = vitaminE
		self.vitaminK = vitaminK
		self.folicAcid = folicAcid
	
	def getVitamins(self):
		return self.carotene,self.vitaminA,self.vitaminB1,self.vitaminB2,self.vitaminB3,self.vitaminB5,self.vitaminB6,self.vitaminB12,self.vitaminD25Hydroxy,self.vitaminE,self.vitaminK,self.folicAcid

class Thyroid(Exam):

	def __init__(self,name):
		Exam.__init__(self, name)

	def setThyroid(self,tsh,t3,t4,freeT4):
		
		self.tsh = tsh
		self.t3 = t3
		self.t4 = t4
		self.freeT4 = freeT4
	
	def getThyroid(self):
		return self.tsh,self.t3,self.t4,self.freeT4

class ImmuneSystem(Exam):
	
	def __init__(self,name):
		Exam.__init__(self, name)

	def setImmuneSystem(self,cpr,esr):
	
		self.cpr = cpr
		self.esr = esr

	def getImmuneSystem(self):
		return self.cpr,self.esr

class GeneralBloodTest(Exam):

	def __init__(self,name):
		Exam.__init__(self, name)

	def setGeneralBloodTest(self,cbc,inr,wbc,rbc,hmc,plt):

		self.cbc = cbc
		self.inr = inr
		self.wbc = wbc
		self.rbc = rbc
		self.hmc = hmc
		self.plt = plt		
	
	def getGeneralBloodTest(self,cbc,inr,wbc,rbc,hmc,plt):
		return self.cbc,self.inr,self.wbc,self.rbc,self.hmc,self.plt

