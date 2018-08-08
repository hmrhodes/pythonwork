from random import *

rouletteWheel = (
	("0", "GR"),
	("28","BL"),
	("9","RD"),
	("26","BL"),
	("30","RD"),
	("11","BL"),
	("7","RD"),
	("20","BL"),
	("32","RD"),
	("17","BL"),
	("5","RD"),
	("22","BL"),
	("34","RD"),
	("15","BL"),
	("3","RD"),
	("24","BL"),
	("36","RD"),
	("13","BL"),
	("1","RD"),
	("00","GR"),
	("27","RD"),
	("10","BL"),
	("25","RD"),
	("29","BL"),
	("12","RD"),
	("8","BL"),
	("19","RD"),
	("31","BL"),
	("18","RD"),
	("6","BL"),
	("21","RD"),
	("33","BL"),
	("16","RD"),
	("4","BL"),
	("23","RD"),
	("35","BL"),
	("14","RD"),
	("2","BL")
	)

black = (2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)
red = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)

bets = (
(1, "0", 35),
(2, "00", 35),
(3, "Any single number", 35),
(4, "0 or 00", 17),
(5, "Any two adjoining numbers", 17),
(6, "Any three adjoining numbers - 1,2,3 or 4,5,6, etc.", 11),
(7, "1 through 12", 1),
(8, "13 through 24", 1),
(9, "25 through 36", 1),
(10, "Odd", 1),
(11, "Even", 1),
(12, "Red", 1),
(13, "Black", 1),
(14, "1 to 18", 1),
(15, "19 to 36", 1),
)

def printWheel(rouletteWheel):
	columnWidth = 2
	for pair in rouletteWheel:
		print (pair[0].rjust(columnWidth), end = '|')
	print("\n")
	for pair in rouletteWheel:
		print (pair[1].rjust(columnWidth), end = '|')
	print("\n")

def getBets(bets,red,black):
	bet = []
	betNum = int(input("Select the number associated with your bet:"))
	if betNum == 1:
		bet.append(0)
	if betNum == 2:
		bet.append(37)
	if betNum == 3:
		getBet = int(input("Please pick a number between 1 and 36:"))
		bet.append(getBet)
	if betNum == 4:
		bet.append(0)
		bet.append(37)
	if betNum == 5:
		getBet = int(input("Please pick the first of two consecutive numbers between 1 and 35:"))
		bet.append(getBet)
		bet.append(getBet+1)
	if betNum == 6:
		getBet = int(input("Please pick the first of three consecutive numbers between 1 and 34:"))
		bet.append(getBet)
		bet.append(getBet+1)
		bet.append(getBet+2)
	if betNum == 7:
		for i in range(1,13):
			bet.append(i)
	if betNum == 8:
		for i in range(13,25):
			bet.append(i)
	if betNum == 9:
		for i in range(25,37):
			bet.append(i)
	if betNum == 10:
		for i in range(1,36,2):
			bet.append(i)
	if betNum == 11:
		for i in range(2,37,2):
			bet.append(i)
	if betNum == 12:
		for i in red:
			bet.append(i)
	if betNum == 13:
		for i in black:
			bet.append(i)
	if betNum == 14:
		for i in range(1,19):
			bet.append(i)
	if betNum == 15:
		for i in range(19,37):
			bet.append(i)
	betSize = float(input("How much are you betting? "))
	return betNum, bet, betSize


def ballspin(rouletteWheel):
	winner = (randint(0,37))
	return winner

def checkWin(bets, betNum, betChoice, wheelSpin, cashBet):
	winFlag = False
	for i in betNum:
		if wheelSpin == i:
			winFlag = True
			payout = bets[betChoice-1][2]*cashBet
			print("Congratulations! You won",payout)
	if winFlag == False:
		print("Sorry, you did not win.")

print("\nThe numbers on the wheel, with colors below:\n")
printWheel(rouletteWheel)

print("The available bets are:")
for bet in bets:
	print(bet[0],":",bet[1])

betChoice, betNum, cashBet = getBets(bets,red,black)

wheelSpin = ballspin(rouletteWheel)
print("The winner is:",wheelSpin)

checkWin(bets, betNum, betChoice, wheelSpin, cashBet)
