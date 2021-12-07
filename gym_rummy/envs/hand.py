# Hand Class. Utilizes a deck
# Provides methods for computing the 
# Tuple (Set, Score)
# where sets is a list of sets and scores is the corresponding value # to each set

from deck import Deck

class Hand(Deck):
    def getSets(self):
        numSets = self.getNumSets(self)
        runSets = self.getRunSets(self)
        # remove overlapped sets
        # we prioritize num sets over run sets
        dictionary = {}
        for arr in numSets:
            for item in arr:
                dictionary[item] = 1
        indexsToErase = []
        for idx, arr in enumerate(runSets):
            for item in arr:
                if item in dictionary:
                    indexsToErase.append(idx)
                    break;
        # iterate backwards as we want to remove largest indexs first
        for i in reversed(indexsToErase):
            runSets.pop(i)
        return numSets, runSets
    
    def getSetScores(self):
        numSet, runSets = self.getSets()
        scores = []
        sets = []
        for arr in numSet:
            scores.append(self.getSetScore(arr))
            sets.append(arr)
        for arr in runSets:
            scores.append(self.getSetScore(arr))
            sets.append(arr)
        return scores, sets

    @staticmethod
    def getSetScore(mySet):
        scoreMap = {'A': 15, 'K': 10, 'Q': 10, 'J': 10, 'T': 10, '9':9, '8':8, '7':7, '6':6, '5':5, '4': 4, '3':3, '2':2}
        score = 0
        for item in mySet:
            score += scoreMap[item[0]]
        return score

    # Gets all numbered sets. Make this callable without an inst
    @staticmethod
    def getNumSets(s):
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

    @staticmethod
    def getRunSets(s):
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
