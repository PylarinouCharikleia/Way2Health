eventTypes = ["Simple", "Dietary", "Medication", "Exercise", "Examination", "Appointment", "Period"]
colors = ["No Color", "Blue", "Red", "Yellow", "Green", "Orange", "Grey", "Pink"]
exerciseTypes = ["No select","Endurance", "Strength", "Balance", "Flexibility"]
severityOptions = ["No select", "Low", "Moderate", "High", "Super High"]

import datetime 

#Calendar methods
def viewCalendar(myCal):
    openCalendar(myCal)

def openCalendar(myCal):
	current = datetime.date.today()
	print("======================={0}=======================".format(myCal.title))
	print("|  Description: {0}                     |".format(myCal.description))
	print("|   Today is: {0}                             |".format(current))
	myCal.textCalendar.prmonth(current.year, current.month, w=0, l=0)
    
	print("|  Enter x to exit or enter s to select desired date.|")
	select = input()
	if select == 'x':
		return
	elif select == 's':
		date = selectDate()
		viewSelectedDate(myCal, date)
	else:
		return


def selectDate():
	print("Choose Date:")
	flag = 1
	while flag:
		try:
			in_year = int(input("|   Enter Year: "))
			in_month = int(input("|   Enter Month: "))
			in_day = int(input("|   Enter Day: "))
			c_date = datetime.date(in_year, in_month, in_day)
			flag = 0
		except ValueError:
			print("|            Invalid Date! Enter again!              |")
			flag = 1
			continue
	print("|   Date:", c_date,"                               |")
	return c_date


def viewSelectedDate(myCal, date):
	current = datetime.date.today()
	print("======================={0}=======================".format(myCal.title))
	print("|  Description: {0}                     |".format(myCal.description))
	print("|   Today is: {0}                             |".format(current))
	myCal.textCalendar.prmonth(date.year, date.month, w=0, l=0)
	print("|  Selected Day: {0}                          |".format(date))
	eventList = myCal.loadDateData(date)
	print("========================Events========================")
	showDateData(eventList)
	if not eventList:
		print("|             No events for this date!               |")
		print("|                                                    |")
   
	print("|        Enter + to add an event, x to exit          |")
	print("|       or anything to return to current date        |")
	print("|                                                    |")
	add = input("| Option:")
	if add == "+":
		myCal.addEvent(date)
	elif add == "q":
		print ("|                 Exiting Calendar                   |")
		return 0
	else:
		openCalendar(myCal)

def showDateData(data):
	e = 1;
	for d in data:        
		print("\nEvent", e, ":")
		d.printEventData()
		e = e + 1

def showEventMenu(myCal):
	
	print("|                  Event Types                       |")
	print("|                                                    |")
	if myCal.user.gender == "male":
		for c in range(0, len(eventTypes) - 1):
			print ("|",c, eventTypes[c],"                                      |")
	elif myCal.user.gender == "female":
		for c in range(0, len(eventTypes)):
			print("|",c, eventTypes[c],"                                      |")

def checkInput(data):
	if not data:
		return False
	else:
		return True

def checkDataFields(data):
	c = True
	for d in data:
		ret = checkInput(d)
		c = c and ret
	return c

def showForm(myCal):
	for c in range(0, len(colors)):
		print(c, colors[c])
	in_col = -1
	while in_col not in range(0, len(colors)):
		try:
			in_col = int(input("| Choose Prefered Highlighting Color: "))
		except ValueError:
			print("|                Invalid Input!                      |")
			continue


	in_color = colors[in_col]
	in_title = input("|	Enter Title: ")
	in_description = input("|	Enter Description: ")

	data = [in_title, in_description]

	allData = [in_color, in_title, in_description]
	if checkDataFields(data) == False:
		myCal.messageNotCompletedFields()
		return 0
	else:
		return allData