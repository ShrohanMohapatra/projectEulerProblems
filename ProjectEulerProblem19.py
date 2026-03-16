# ProjectEulerProblem19.py

import unittest

class test_ProjectEulerProblem19(unittest.TestCase):
	# I assume the counter starts from 1 Jan 1900 Monday
	origCounter = 0
	dictWeekDayCode = {
		1: "Monday",
		2: "Tuesday",
		3: "Wednesday",
		4: "Thursday",
		5: "Friday",
		6: "Saturday",
		0: "Sunday"
		}
	seqOfMonth = [
		"January", "February", "March",
		"April", "May", "June",
		"July", "August", "September",
		"October", "November", "December"
		]
	dictDaysInAMonthRegularYear = {
		"January": 31, "February": 28, "March": 31,
		"April": 30, "May": 31, "June": 30,
		"July": 31, "August": 31, "September": 30,
		"October": 31, "November": 30, "December": 31
		}
	dictDaysInAMonthLeapYear = {
		"January": 31, "February": 29, "March": 31,
		"April": 30, "May": 31, "June": 30,
		"July": 31, "August": 31, "September": 30,
		"October": 31, "November": 30, "December": 31
		}
	def loopYearBool(self, yearNumber):
		leapYearFlag = False
		if yearNumber % 4 == 0:
			if yearNumber % 100 == 0:
				if yearNumber % 400 == 0:
					leapYearFlag = True
				else:
					leapYearFlag = False
			else:
				leapYearFlag = True
		else:
			leapYearFlag = False
		return leapYearFlag
	def weekDayCounter(self, dateDictionary):
		# dateDictionary is a dictionary of the form
		# dateDictionary = {
		# 	"day": finalDayCounter,
		# 	"month": finalMonthCounter,
		# 	"year": finalYearCounter
		# 	}
		monthCounter = 1
		yearCounter = 1900
		finalDayCounter = dateDictionary["day"]
		finalMonthCounter = dateDictionary["month"]
		finalYearCounter = dateDictionary["year"]
		dayNumberCounter = self.origCounter
		# First we count in years
		while yearCounter < finalYearCounter:
			if self.loopYearBool(yearCounter): dayNumberCounter += 366
			else: dayNumberCounter += 365
			yearCounter = yearCounter + 1
		while monthCounter != finalMonthCounter:
			if self.loopYearBool(finalYearCounter):
				dayNumberCounter += self.dictDaysInAMonthLeapYear[self.seqOfMonth[monthCounter-1]]
			else:
				dayNumberCounter += self.dictDaysInAMonthRegularYear[self.seqOfMonth[monthCounter-1]]
			monthCounter = monthCounter + 1
		dayNumberCounter = dayNumberCounter + finalDayCounter
		return dayNumberCounter % 7
	def sundayCounterTwentiethCentury(self):
		monthCounter = 1
		setOfMonths = [self.seqOfMonth[k] for k in range(12)]
		sundayCounter = 0 
		for year in range(1901, 2001):
			for monthIndex in range(1, 13):
				dateDictStruct = {"day": 1, "month": monthIndex, "year": year}
				dayOfTheWeekFlag = self.weekDayCounter(dateDictStruct)
				if dayOfTheWeekFlag == 0:
					sundayCounter = sundayCounter + 1
		return sundayCounter
	def test_LoopYearCheckCase1(self):
		self.assertFalse(self.loopYearBool(1900))
	def test_LoopYearCheckCase2(self):
		self.assertFalse(self.loopYearBool(1983))
	def test_LoopYearCheckCase3(self):
		self.assertTrue(self.loopYearBool(1984))
	def test_LoopYearCheckCase4(self):
		self.assertTrue(self.loopYearBool(2024))
	def test_LoopYearCheckCase5(self):
		self.assertFalse(self.loopYearBool(1974))
	def test_LoopYearCheckCase6(self):
		self.assertTrue(self.loopYearBool(1600))
	def test_LoopYearCheckCase7(self):
		self.assertTrue(self.loopYearBool(2000))
	def test_LoopYearCheckCase8(self):
		self.assertFalse(self.loopYearBool(2100))
	def test_dateCheckVerif1(self):
		dateDictStruct = {"day": 15, "month": 8, "year": 1947}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Friday"
			)
	def test_dateCheckVerif2(self):
		dateDictStruct = {"day": 17, "month": 8, "year": 1947}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Sunday"
			)
	def test_dateCheckVerif3(self):
		dateDictStruct = {"day": 2, "month": 1, "year": 1948}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Friday"
			)
	def test_dateCheckVerif4(self):
		dateDictStruct = {"day": 1, "month": 7, "year": 1948}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Thursday"
			)
	def test_dateCheckVerif5(self):
		dateDictStruct = {"day": 21, "month": 11, "year": 1996}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Thursday"
			)
	def test_dateCheckVerif6(self):
		dateDictStruct = {"day": 15, "month": 3, "year": 2026}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Sunday"
			)
	def test_dateCheckVerif7(self):
		dateDictStruct = {"day": 16, "month": 3, "year": 2026}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Monday"
			)
	def test_dateCheckVerif8(self):
		dateDictStruct = {"day": 17, "month": 3, "year": 2026}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Tuesday"
			)
	def test_dateCheckVerif9(self):
		dateDictStruct = {"day": 18, "month": 3, "year": 2026}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Wednesday"
			)
	def test_dateCheckVerif10(self):
		dateDictStruct = {"day": 19, "month": 3, "year": 2026}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Thursday"
			)
	def test_dateCheckVerif11(self):
		dateDictStruct = {"day": 20, "month": 3, "year": 2026}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Friday"
			)
	def test_dateCheckVerif12(self):
		dateDictStruct = {"day": 26, "month": 1, "year": 1950}
		self.assertTrue(
			self.dictWeekDayCode[self.weekDayCounter(dateDictStruct)] == "Thursday"
			)
	def test_SundayCounterVerif(self):
		self.assertTrue(self.sundayCounterTwentiethCentury() == 171)

if __name__ == "__main__":
	unittest.main()
