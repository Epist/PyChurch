"""
This program reads in Scheme/Church data formatted as a string with nested parentheses and outputs
a Python nested list of lists in the same format as a cPickled binary file.

Invoke this from the command line using the filename of the Scheme/Church data you want read
There is also a second optional command line argument to specify the name of the output file.
If no filename is specified, this defaults to "pickledData.p"

Ex:  python PythonListTranslator.py commSamplingData.txt commSamplingData.p

To read the resultant pickled file in Python, simply use:
import cPickle as pickle
data = pickle.load(open("path_to_file", "rb" ))
"""
import sys
import cPickle as pickle
fileName = sys.argv[1]
if len(sys.argv)>2: #If an output filename is supplied
    outputFileName = sys.argv[2]
else:
    outputFileName = "pickledData.p" #Otherwise, use the default
f = open(fileName, 'r')
rawInput = f.read()
import re

inputString = re.split('([()\s])', rawInput)

def removeSpaces (li): #Remove the extra whitespace elements from the list of atoms and parentheses
    newList=[]
    for elem in li:
        if not((elem==" ") or (elem=="")):
            newList.append(elem)
    return newList
    
global inputList #Make the instruction list available to the entire program
inputList=removeSpaces(inputString)

def truncFromBeg (li): #Remove the first element from the instruction list
    if len(li) > 0 : 
        return li[1:len(li)]
    else :
        raise NameError('Not enough closing parentheses')

def buildLists (outputLists=[]): #Build the Python nested lists as per the instructions

  global inputList #Access the global version of this variable
  sameLevel = 1
  while sameLevel == 1 :
    if len(inputList)>0:
        currentLit = inputList[0]
    else:
        return outputLists
    if currentLit=="(" :
        innerList=[]
        inputList = truncFromBeg(inputList)
        outputLists.append(buildLists(innerList))
    elif currentLit == ")" :
        inputList = truncFromBeg(inputList)
        return outputLists
    else :
        inputList = truncFromBeg(inputList)
        outputLists.append(currentLit)
    
tooManyParens = buildLists() #Remove the outer parentheses
outputData = tooManyParens[0]
#print output
outFile = open(outputFileName, "wb" )
pickle.dump(outputData, outFile) #Save the file
outFile.close()