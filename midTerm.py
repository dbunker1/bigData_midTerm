#! /usr/bin/python


import sys
import nltk
import string
import CryptoTools

from pyspark import SparkContext, SparkConf
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

sc = SparkContext("local", "Midterm")

encrypted1 = sc.textFile("Encrypted-1.txt")     #This is a linux Dictionary
encrypted2 = sc.textFile("Encrypted-2.txt")     #An Englishmans Travels in America
encrypted3 = sc.textFile("Encrypted-3.txt")     #The Great Gatsby

alphabet = 'abcdefghijklmnopqrstuvwxyz'

#This code uses the crypto library to solvel the cipher

f = open("Encrypted-1.txt","r")

if f.mode == 'r':
    letters = f.read()
    letters = CryptoTools.format_list(letters, 1)
    psiValue = CryptoTools.psi_test(letters)

    letters = CryptoTools.bestCaesarCipher(letters)
    print(psiValue)

    f1 = open("oneSolution.txt", "w")

    for i in letters:
        f1.write(i)

f = open("Encrypted-2.txt","r")

if f.mode == 'r':
    letters = f.read()
    letters = CryptoTools.format_list(letters, 1)
    psiValue = CryptoTools.psi_test(letters)

    letters = CryptoTools.bestCaesarCipher(letters)
    print(psiValue)

    f1 = open("twoSolution.txt", "w")

    for i in letters:
        f1.write(i)

f = open("Encrypted-3.txt","r")

if f.mode == 'r':
    letters = f.read()
    letters = CryptoTools.format_list(letters, 1)
    psiValue = CryptoTools.psi_test(letters)

    letters = CryptoTools.bestCaesarCipher(letters)
    print(psiValue)

    f1 = open("threeSolution.txt", "w")

    for i in letters:
        f1.write(i)


#This section uses spark to seperate the words and characters and take a count of each occurence
#The output is then saved to each corresponding directory. 

lines1 = encrypted1.map(lambda line: str(line))

words1 = lines1.flatMap(lambda str: str.split(" "))
chars1 = lines1.flatMap(lambda str: list(str))

wordCount1 = words1.map(lambda word: (word.lower(),1)).reduceByKey(lambda nw1,nw2: nw1+nw2)
charCount1 = chars1.map(lambda char: (char.lower(),1)).reduceByKey(lambda c1,c2: c1+c2)

wordCount1.saveAsTextFile("wordCounts1")
charCount1.saveAsTextFile("charCounts1")


lines2 = encrypted2.map(lambda line: str(line))

words2 = lines2.flatMap(lambda str: str.split(" "))
chars2 = lines2.flatMap(lambda str: list(str))

wordCount2 = words2.map(lambda word: (word.lower(),1)).reduceByKey(lambda nw1,nw2: nw1+nw2)
charCount2 = chars2.map(lambda char: (char.lower(),1)).reduceByKey(lambda c1,c2: c1+c2)

wordCount2.saveAsTextFile("wordCounts2")
charCount2.saveAsTextFile("charCounts2")



lines3 = encrypted3.map(lambda line: str(line))

words3 = lines3.flatMap(lambda str: str.split(" "))
chars3 = lines3.flatMap(lambda str: list(str))

wordCount3 = words3.map(lambda word: (word.lower(),1)).reduceByKey(lambda nw1,nw2: nw1+nw2)
charCount3 = chars3.map(lambda char: (char.lower(),1)).reduceByKey(lambda c1,c2: c1+c2)

wordCount3.saveAsTextFile("wordCounts3")
charCount3.saveAsTextFile("charCounts3")

