# A set of util methods
import numpy as np

# Gets all numbered sets
def checkNum(s):
    numMap = {12: 'A', 0:'2', 1:'3', 2:'4', 3:'5', 4:'6', 5:'7', 6:'8',  7:'9', 8:'T', 9:'J', 10:'Q', 11:'K'}
    suiteMap = {0:'Hearts', 1:'Diamonds', 2:'Spades', 3:'Clubs'}
    mat = s.toNumpy() 
    # Iterate over numbers
    totalSets = []
    for i in range(mat.shape[1]):
        count = 0
        curSet = []
        for j in range(mat.shape[0]):
            if mat[j][i] == 1:
                count += 1
                curSet.append(numMap[i]+suiteMap[j])
        if count >= 3:
            totalSets.append(curSet)
    return totalSets

def checkRun(s):
    # not as easy since we need to find when there are three or more ones in a row. 
    numMap = {0:'2', 1:'3', 2:'4', 3:'5', 4:'6', 5:'7', 6:'8',  7:'9', 8:'T', 9:'J', 10:'Q', 11:'K', 12: 'A'}
    suiteMap = {0:'Hearts', 1:'Diamonds', 2:'Spades', 3:'Clubs'}
    mat = s.toNumpy() 
    totalSets = []
    for i in range(mat.shape[0]):
        count = 0
        curSet = []
        for j in range(mat.shape[1]):
            if mat[i][j] == 1:
                count += 1
                curSet.append(numMap[j] + suiteMap[i])
            else:
                if count >= 3:
                    totalSets.append(curSet)
                count = 0
                curSet = []
        if count >= 3:
            totalSets.append(curSet)
    return totalSets
