def getword():
	theword = list(str(input("Player 1 - please input a word:")).upper())
	wordlength = len(theword)
	return theword, wordlength

def getletter(thelist, answer, thecount):
	print("The word is:",thelist)
	letter = str(input("guess a letter: ")).upper()
	if letter in answer:
		for i,j in enumerate(answer):
			if j == letter:
				thelist[i] = letter
		print("correct!")
		return thelist, thecount
	else:
		print("incorrect")
		thecount += 1
	return thelist, thecount

def status(theparts, thecount, progress):
	progress = theparts[thecount]
	return thecount, progress


thescaffold = ["Scaffold", "Head", "Body", "Left Arm", "Right Arm","Left Leg","Right Leg", "Dead!"]
tries = 0
thebody = thescaffold[tries]
theword, thelength = getword()
wordholder = list(("_"*thelength))

while wordholder != theword:
	if "Dead!" in thebody:
		print("Sorry, you're dead! The word is:", theword)
		break
	else:
		print("The word:", wordholder)
		print("Your status:", thebody)
		wordholder, tries = getletter(wordholder,theword,tries)
		tries, thebody = status(thescaffold, tries, thebody)
		if "_" not in wordholder:
			print("Success! The word is:", theword)
			break
