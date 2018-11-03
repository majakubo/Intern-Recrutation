"""This module help to calculate scores in Scrabble Game.

There are three options to use it as script:
- calculate score of specific word --word or -w <word>
- from dictionary find word that has specific score --score or -s <score>
- from dictionary find word with highest score --top -t
"""
import sys
import random


class ScrabbleRules:
    """Holds data about score rules, and dictionary with words."""

    def __init__(self, scrabbles_scores, dict_file):
        self.dictionary = open(dict_file, "r")
        self.dictionary = [word[:-1] for word in self.dictionary]   # remove \n character from words
        self.letter_scores = {letter: score for score, letters in scrabbles_scores   # create dict with mapping
                              for letter in letters.split()}                         # letter: score

    def score_for_letter(self, letter):
        return self.letter_scores[letter]

    def get_dictionary(self):
        return self.dictionary


class Referee:
    def __init__(self, scrabble_scores, dict_file):
        self.Rules = ScrabbleRules(scrabble_scores, dict_file)

    def word_score(self, word):
        word = word.upper()
        score = 0
        for letter in word:
            score += self.Rules.score_for_letter(letter)

        return score

    def dictionary_scores(self):
        dictionary = self.Rules.get_dictionary()
        words_scores = []

        for word in dictionary:
            word_score = self.word_score(word)
            words_scores.append((word, word_score))

        return words_scores

    def dictionary_top_n(self, n):
        words_scores = self.dictionary_scores()
        words_scores.sort(key=lambda x: x[1]) # sort by score that letter has

        return words_scores[-n]

    def words_with_score(self, given_score):
        words_scores = self.dictionary_scores()
        words = [word for word, score in words_scores if score == int(given_score)]
        return words

    def word_with_score(self, given_score):
        words = self.words_with_score(given_score)
        if words:
            return random.choice(words)


if __name__ == '__main__':

    mode = sys.argv[1]
    scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"), (4, "F H V W Y"), (5, "K"), (8, "J X"),
                       (10, "Q Z")]

    Ref = Referee(scrabble_scores, 'dictionary.txt')

    if mode == '--word' or mode == '-w':
        user_word = sys.argv[2]
        user_score = Ref.word_score(user_word)
        print("'{}' is worth {} points.".format(user_word, user_score))

    elif mode == '--top' or mode == '-t':
        top_word = Ref.dictionary_top_n(1)
        print("{} has the biggest score = {}".format(top_word[0], top_word[1]))

    elif mode == '--score' or mode == '-s':
        user_score = sys.argv[2]
        user_word = Ref.word_with_score(user_score)
        if user_word:
            print("{} has score equal to given ( {} )".format(user_word, user_score))

    else:
        raise NotImplementedError("There is no such mode, check docstr")
