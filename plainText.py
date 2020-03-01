import sys
import nltk
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "Test")



text_file = sc.textFile("oneSolution.txt")

counts.saveAsTextFile("plainText1.txt")

text_file = sc.textFile("twoSolution.txt")

counts.saveAsTextFile("plainText2.txt")


text_file = sc.textFile("threeSolution.txt")

counts.saveAsTextFile("plainText3.txt")

