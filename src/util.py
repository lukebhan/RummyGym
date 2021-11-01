# A set of util methods

# Checks if a given set is all the same number. All cards must be member of num
def checkNum(s):
    if(len(s) > 4 or len(s) < 3):
        return False
    else:
        for idx, card in enumerate(s):
            if idx == 0:
                num = card[0]
            if card[0] != num:
                return False
        return True

# Checks if a given set is all the same suite and consists of a run. Unfortunately takes nlogn time. All cards must be members of run
def checkRun(s):
    if(len(s) < 3):
        return False
    else:
        arr = []
        miniMap = {"2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J": 11, "Q": 12, "K": 13, "A": 14}
        # check suite
        for idx, card in enumerate(s):
            if idx == 0:
                suite = card[1:]
            if card[1:] != suite:
                return False
            else:
                arr.append(miniMap[card[0]])
        arr = sorted(arr)
        # check ordering
        prevVal = arr[0]
        for i in range(1, len(arr)):
            # Handle aces as low
            if arr[i]-1 == prevVal or (arr[i] == 14 and arr[0] == 2):
                prevVal = arr[i]
            else: 
                return False
        return True 
