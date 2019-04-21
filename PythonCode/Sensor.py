
class Sensor:
	def __init__(self,user,sensID):
		self.user=user
		self.sensID = sensID

	def inputSamplig():
	def refreshCache():
	def generateCacheAv():
	def cacheAvSavePerSixH():
	def inputCacheDifCalc():
	def difSave():
	
class BodySensor(Sensor):
	def __init__(self,user,sensID):
		Sensor.__init__(self,user,sensID):

class BloodSensor(BodySensor):
	def __init__(self,bol,bolStat,bg,bgStat,spO2,spO2Stat,user,sensID):
		BodySensor.__init__(self,user,sensID):
		self.bol=bol
		self.bolStat=bolStat
		self.bg=bg
		self.bgStat=bgStat
		self.spO2=spO2
		self.spO2Stat=spO2Stat

	def readValues():

class GeneralSensor(BodySensor):
	def __init__(self,bt,btStat,skinRespiration,skinRespStat,user,sensID):
		BodySensor.__init__(self,user,sensID):
		self.bt=bt
		self.btStat=btStat
		self.skinRespiration=skinRespiration
		self.skinRespStat

	def readValues():


class RespiratorySensor(BodySensor):
	def __init__(self,rp,rpStat,respirationSounds,respiSoundsStat,user,sensID):
		BodySensor.__init__(self,user,sensID):
		self.rp=rp
		self.rpStat=rpStat
		self.respirationSounds=respirationSounds
		self.respiSoundsStat=respiSoundsStat

	def readValues():

class CardiacSensor(BodySensor):
	def __init__(self,ecg,ecgStat,hr,hrStat,sysBP,sysBPStat,diaBP,diaBPStat,user,sensID):
		BodySensor.__init__(self,user,sensID):
		self.ecg=ecg
		self.ecgStat=ecgStat
		self.hr=hr
		self.hrStat=hrStat
		self.sysBP=sysBP
		self.sysBPStat=sysBPStat
		self.diaBP=diaBP
		self.diaBPStat=diaBPStat

	def readValues():


class EnvironmentalSensor(Sensor):
	def __init__(self,user,sensID,temp,humidity,co,co2,radon,formaldehyde,airMold,asbesto,airParticles,light):
		Sensor.__init__(self,user,sensID):
		self.temp=temp
		self.humidity=humidity
		self.co=co
		self.co2=co2
		self.radon=radon
		self.formaldehyde=formaldehyde
		self.airMold=airMold
		self.asbesto=asbesto
		self.airParticles=airParticles
		self.light=light


class CurrentStatus:
	def __init__(bloodSensor,skinSensor,respiratorySensor,cardiacSensor):
		self.bloodSensor=bloodSensor
		self.skinSensor=skinSensor
		self.respiratorySensor=respiratorySensor
		self.cardiacSensor=cardiacSensor

	def getNewValues():
