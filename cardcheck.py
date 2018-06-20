def checkLength(cardNum):
	numString=str(cardNum)
#	print("The number length is",cardNum)
	if 15 <= len(numString) <= 16:
		return True
	else:
		return False

def checkType(cardNum):
	numString=str(cardNum)
	brand = ""
	if numString[0] == 4:
		brand += "Visa"
	elif numString[0:2:1] in ("51","52","53","54","55"):
		brand += "Mastercard"
	elif numString[0:2:1] in ("34","37"):
		brand += "Amex"
	elif numString[0] == 6:
		brand += "Discover"
	else:
		brand += "Fraud"
#	print("The brand is",brand)
	return(brand)

def checkLuhn(cardNum):
	numString=str(cardNum)
	numSize = len(numString)
#	print(numSize)
	numList = []
	newList = []
	for i in range(0,numSize):
		numList.append(int(numString[i]))
#	print(numList)
	j = (numSize-1)
	while j >= 0:
		numList[j] = 2*numList[j]
		j -= 2
#	print(numList)
	for k in numList:
		if k > 9:
			newList.append(1)
			newList.append(k-10)
		else:
			newList.append(k)
#	print(newList)
#	print(sum(newList))
#	print(sum(newList)%10)
	if (sum(newList))%10 == 0:
		return True
	else:
		return False


def cardCheck():
	cardNum = int(input("Please enter a credit card number:"))
	if checkLength(cardNum):
		if checkType(cardNum) != "Fraud":
			if checkLuhn(cardNum):
				print(cardNum,"is a valid",brand,"card")
			else:
				print(cardNum,"isn't a valid card.")
		else:
			print(cardNum,"isn't a valid card.")
	else:
		print(cardNum,"isn't a valid card.")

cardCheck()





















