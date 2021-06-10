#!/usr/bin/python3
from configparser import ConfigParser
import sys


if len(sys.argv) > 1:
    inifile = sys.argv[1]
else:
    inifile = "words.ini"

# Read .ini file
config_object = ConfigParser()
config_object.read(inifile)
try:
    allwords = config_object["English"]
except KeyError:
    allwords = []

# Read words to test
wordsA = {}
wordsB = {}
if len(allwords):
    for word1, word2 in allwords.items():
        wordsA[word1] = word2
        wordsB[word2] = word1
else:
    print("No words found in", inifile)

# Quiz start ...
if len(wordsA):
    print(wordsA)
    print("\n")
    print(wordsB)

# end of code
