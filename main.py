def countWords(text:str)->int:
	return len(text.split())

def countCharacters(text:str)->dict:
	letterStatistics = dict()
	for character in text.lower():
		if character in letterStatistics:
			letterStatistics[character]+=1
		else:
			letterStatistics[character]=1
	return letterStatistics

def main():
	filePath = "book/frankenstein.txt"
	bookContent:str = ""
	with open(filePath) as f:
		bookContent = f.read()
	totalWords:int = countWords(bookContent)
	letterStats = countCharacters(bookContent)
	print(f"--- Begin Report of {filePath} ---")
	print(f"The document contains {totalWords}")
	print("Character statistics:")
	for k in letterStats:
		print(f"The character {k} was found {letterStats[k]} times")	
	print("--- End report ---")
main()
