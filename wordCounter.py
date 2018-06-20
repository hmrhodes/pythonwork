def wordCleaner(word):
	newWord = ""
	word = word.lower()
	for i in word:
		if "a" <= i <= "z":
			newWord += i
	return(newWord)

def makeDict(theList):
	tempDict = {}
	for i in theList:
		if i in tempDict:
			tempDict[i] += 1
		else:
		 	tempDict[i] = 1
	return(tempDict)

def sortDict(theDict):
	theList = []
	pair = []
	sortedList = []
	for a, b in theDict.items():
		pair = a,b
		theList.append(pair)
	sortedList = sorted(theList, key=lambda wordcount: wordcount[1], reverse = True)
	return(sortedList)


def wordCounter():

	with open("sample_text.rtf") as wordFile:
		words = wordFile.read()
		data = words.split()
		wordList = []
		wordDict = {}
		sortList = []
		for i in data:
			if wordCleaner(i) != "":
				wordList.append(wordCleaner(i))
		wordDict = makeDict(wordList)
		sortList = sortDict(wordDict)

		print("The top 10 words, with freqency, are:")
		for i in range (0,10):
			print(sortList[i][0],"\t", sortList[i][1])


wordCounter()