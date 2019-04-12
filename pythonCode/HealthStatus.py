class HealthStatus:
	def __init__(self):
	self.status=""
	self.historyStatus=""
	self.medicalReportStatus=""
	self.medicationStatus=""
	self.exerciseStatus=""
	self.dietStatus=""

class DietReport:
	def __init__(self):


class Meal:
	def __init__(self,name):
		self.name=name


class Beverage:
	def __init__(self,name,bevType):
		self.name=name
		self.bevType=bevType

class Supleement:
	def __init__(self,name,supType):
		self.name=name
		self.supType=supType

class MedicationReport:
	def __init__(self):
		self.listOfMedicine={}
		self.listOfSideEffects={}
	

class Medicine:
	def __init__(self,name,dosage):
		self.name=name
		self.dosage=dosage

class ExerciseReport:
	def __init__(self)
		self.listOfExercises={}

class Exercise:
	def __init__(self,name,duration,weightFlag,weight):
		self.name=name
		self.duration=duration
		self.weightFlag=weightFlag
		self.weight


class MedicalReport:
	def __init__(self):
		self.heartReport=None
		self.liverReport=None
		self.generalBloodTest=None
		self.immuneSystemReport=None
		self.thyroidReport=None
		self.metabolismReport=None
		self.urinaryReport=None
		self.vitaminsReport=None
	

class ImmuneSystem:
	def __init__(self,cpr,esr):
		self.status=""
		self.cpr=cpr
		self.esr=esr

class Liver:
	def __init__(self,lft,uANDe,totBillrubin,alt,ast,ggt,albumin,fiveNeucleotidase, ceruloplasmin,afp,serumGlocose,lactateDehyfrogenase):
		self.status=""
		self.lft=lft
		self.uANDe=uANDe
		self.totBillrubin=totBillrubin
		self.alt=alt
		self.ast=ast
		self.ggt=ggt
		self.albumin=albumin
		self.fiveNeucleotidase=fiveNeucleotidase
		self.ceruloplasmin=ceruloplasmin
		self.afp=afp
		self.serumGlocose=serumGlocose
		self.lactateDehyfrogenase

class Thyroid:
	def __init__(self,tsh,t3,t4,freeT4):
		self.status=""
		self.tsh=tsh
		self.t3=t3
		self.t4=t4
		self.freeT4=freeT4


class UrinarySystem:
	def __init__(self,urineColor,urineClarity,specificGravity.pH,protein,glucose,ketones,crystals,bacteria,blood):
		self.status=""
		self.urineColor=urineColor
		self.urineClarity=urineClarity
		self.specificGravity=specificGravity
		self.pH=pH
		self.protein=protein
		self.glucose=glucose
		self.ketones=ketones
		self.crystals=crystals
		self.bacteria=bacteria
		self.blood=blood

class Heart:
	def __init__(self,hdl,ldl):
		self.status=""
		self.hdl
		self.ldl

class Metabolism:
	def __init__(self,cmp):
		self.status=""
		self.cmp=cmp

class GeneralBloodTest:
	def __init__(self,cbc,inr,wbc,rbc,hmc,plt):
		self.status=""
		self.cbc=cbc
		self.inr=inr
		self.wbc=wbc
		self.rbc=rbc
		self.hmc=hmc
		self.plt=plt

class Vitamins:
	def __init__(self,carotene,vitaminA,vitaminB1,vitaminB2,vitaminB3,vitaminB5,vitaminB6,vitaminB12,vitaminD25Hydroxy,vitaminE,vitaminK,folidAid):
		self.status=""
		self.carotene=carotene
		self.vitaminA=vitaminA
		self.vitaminB1=vitaminB1
		self.vitaminB2=vitaminB2
		self.vitaminB3=vitaminB3
		self.vitaminB5=vitaminB5
		self.vitaminB6=vitaminB6
		self.vitaminB12=vitaminB12
		self.vitaminD25Hydroxy=vitaminD25Hydroxy
		self.vitaminE=vitaminE
		self.vitaminK=vitaminK
		self.folicAcid=folicAcid

