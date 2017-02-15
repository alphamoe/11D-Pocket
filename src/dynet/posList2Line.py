import sys
import random

def readTags(input_file):
	words=[]
	tags=[]
	for line in open(input_file):
		line = line.strip()
		if len(line) > 1:
			if len(line.split()) !=3:
				continue
			word, word2, tag = line.split()
			words.append(word)
			tags.append(tag)
		else:
			if len(words) != len(tags):
				print "Missing tags .."
				break
			newline=""
			for item in words:
				newline += item + " "
			newline +=  "||| "
			for item in tags:
				#newline += item +" "
				newline += "* "
			print newline.strip()
			words=[]
			tags=[]

if __name__ =="__main__":
	input_file = sys.argv[1]
	
	readTags(input_file)
