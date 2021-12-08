""" Hand Class. Utilizes a deck"""
# Provides methods for computing the Tuple (Set, Score)
# where sets is a list of sets and scores is the corresponding value # to each set

import sys
sys.path.append("./envs")
from deck import Deck #pylint: disable=E0401,C0413

class Hand(Deck):
    """Hand class"""

    def get_sets(self):
        """Gets all sets from a hand"""
        num_sets = self.get_num_sets(self)
        run_sets = self.get_run_sets(self)
        # remove overlapped sets
        # we prioritize num sets over run sets
        dictionary = {}
        for arr in num_sets:
            for item in arr:
                dictionary[item] = 1
        indexs_to_erase = []
        for idx, arr in enumerate(run_sets):
            for item in arr:
                if item in dictionary:
                    indexs_to_erase.append(idx)
                    break
        # iterate backwards as we want to remove largest indexs first
        for i in reversed(indexs_to_erase):
            run_sets.pop(i)
        return num_sets, run_sets

    def get_set_scores(self):
        """Gets score for a set"""
        num_set, run_sets = self.get_sets()
        scores = []
        sets = []
        for arr in num_set:
            scores.append(self.get_set_score(arr))
            sets.append(arr)
        for arr in run_sets:
            scores.append(self.get_set_score(arr))
            sets.append(arr)
        return scores, sets

    @staticmethod
    def get_set_score(my_set):
        """Gets score for a set, callable without an inst"""
        score_map = {'A': 15, 'K': 10, 'Q': 10, 'J': 10, 'T': 10, \
        '9':9, '8':8, '7':7, '6':6, '5':5, '4': 4, '3':3, '2':2}
        score = 0
        for item in my_set:
            score += score_map[item[0]]
        return score

    @staticmethod
    def get_num_sets(sets):
        """Gets all numbered sets, makes this callable without an inst"""
        num_map = {12: 'A', 0:'2', 1:'3', 2:'4', 3:'5', 4:'6',\
        5:'7', 6:'8',  7:'9', 8:'T', 9:'J', 10:'Q', 11:'K'}
        suite_map = {0:'Hearts', 1:'Diamonds', 2:'Spades', 3:'Clubs'}
        mat = sets.to_numpy()
        # Iterate over numbers
        total_sets = []
        for i in range(mat.shape[1]):
            count = 0
            cur_set = []
            for j in range(mat.shape[0]):
                if mat[j][i] == 1:
                    count += 1
                    cur_set.append(num_map[i]+suite_map[j])
            if count >= 3:
                total_sets.append(cur_set)
        return total_sets

    @staticmethod
    def get_run_sets(sets):
        """Not as easy since we need to find when there are three or more ones in a row."""
        num_map = {0:'2', 1:'3', 2:'4', 3:'5', 4:'6', 5:'7', \
        6:'8',  7:'9', 8:'T', 9:'J', 10:'Q', 11:'K', 12: 'A'}
        suite_map = {0:'Hearts', 1:'Diamonds', 2:'Spades', 3:'Clubs'}
        mat = sets.to_numpy()
        total_sets = []
        for i in range(mat.shape[0]):
            count = 0
            cur_set = []
            for j in range(mat.shape[1]):
                if mat[i][j] == 1:
                    count += 1
                    cur_set.append(num_map[j] + suite_map[i])
                else:
                    if count >= 3:
                        total_sets.append(cur_set)
                    count = 0
                    cur_set = []
            if count >= 3:
                total_sets.append(cur_set)
        return total_sets
