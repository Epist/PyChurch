import sys
fileName = sys.argv[1]
f = open(fileName, 'r')
rawInput = f.read()
import re
#rawInput = '(asd a b (f) g)'
inputString = re.split('([()\s])', rawInput)

def removeSpaces (li):
    newList=[]
    for elem in li:
        if not((elem==" ") or (elem=="")):
            newList.append(elem)
    return newList
    
global inputList
inputList=removeSpaces(inputString)
#inputList = ["(","cfd","d","(","da","f",")","dr","f","(","d","f","(","d",")","r",")",")"] #This actually needs to be a list of literals
#inputList = ["(","a","b","(","c",")","d",")"]

def truncFromBeg (li):
    if len(li) > 0 : 
        return li[1:len(li)]
    else :
        raise NameError('Not enough closing parentheses')

def buildLists (outputLists=[]):

  global inputList
  if len(inputList)>0:
    currentLit = inputList[0]
  else:
      return outputLists
  #print outputLists
  #print inputList
  if currentLit=="(" :
    innerList=[]
    inputList = truncFromBeg(inputList)
    outputLists.append(buildLists(innerList))
    return buildLists(outputLists)
  if currentLit == ")" :
    inputList = truncFromBeg(inputList)
    return outputLists
  else :
    outputLists.append(currentLit)
    inputList = truncFromBeg(inputList)
    return buildLists(outputLists)
    #Insert data in current loc, move the pointer ahead one
    
tooManyParens = buildLists()
output = tooManyParens[0]
print output