# Improved version of wordcount.py
import sys
import argparse
from collections import Counter

def countwords(words):
    global totalwords
    global wordcount

    totalwords += len(words)
    wordcount.update(words)

# create parser
parser = argparse.ArgumentParser(description="Count words in a file.")
parser.add_argument("filename", help="The file to count the words in.")
args = parser.parse_args()

totalwords = 0
wordcount = Counter()

# open the file
with open(args.filename, "r") as file:
    # read the file line by line
    for line in file:
        # split the line into words
        words = line.split()
        # count the words
        #countwords(words.lower())
        countwords([word.lower() for word in words])

# append "-count.txt" to the filename excluding the extension
resultfilename = args.filename.split(".")[0]+"-count.txt"

# open the result file
with open(resultfilename, "w") as resultfile:
    # write the total number of words
    resultfile.write("Total number of words: "+str(totalwords)+"\n")
    # write the number of unique words
    resultfile.write("Number of unique words: "+str(len(wordcount))+"\n\n")

    # write the word count
    for word, count in wordcount.most_common():
        resultfile.write(f"{word}: {count}\n")

print("Done! All word counts written to "+resultfilename)

'''
import sys

totalwords = 0
uniquewords = 0
wordcount = {}

def countwords(word):
    global totalwords
    global uniquewords
    global wordcount

    totalwords += 1
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1
        uniquewords += 1

# accept the file name as argument
filename = sys.argv[1]

# open the file
file = open(filename, "r")

# read the file line by line
for line in file:
    # split the line into words
    words = line.split()
    # count the words
    for word in words:
        countwords(word)

# close the file
file.close()


# print the total number of words
#print("Total number of words: "+str(totalwords))
# print the number of unique words
#print("Number of unique words: "+str(uniquewords))
# print the word count
#print("Word count: "+str(wordcount))


# append "-count.txt" to the filename excluding the extension
resultfilename = filename.split(".")[0]+"-count.txt"
resultfile = open(resultfilename, "w")

# write the total number of words
resultfile.write("Total number of words: "+str(totalwords)+"\n")
# write the number of unique words
resultfile.write("Number of unique words: "+str(uniquewords)+"\n\n")

# write the most used word and its count first to the file and then remove it from the wordcount dictionary
# repeat this process until the wordcount dictionary is empty
while len(wordcount) > 0:
    maxcount = 0
    maxword = ""
    for word in wordcount:
        if wordcount[word] > maxcount:
            maxcount = wordcount[word]
            maxword = word
    resultfile.write(maxword+": "+str(maxcount)+"\n")
    del wordcount[maxword]      

# close the file
resultfile.close()
'''