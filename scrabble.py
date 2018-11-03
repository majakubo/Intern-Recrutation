import sys
class ScrabbleRules:
    def __init__(self, scrabbles_scores, dict_file):
        self.dictionary = open("dict_file", "r")
        self.letter_scores = {letter: score for score, letters in scrabbles_scores 
                                            for letter in letters.split()}

    def score_for_letter(self, letter):
        return letter_scores[letter]

    
    def get_dictionary(self):
        return self.dictionary


class Referee:
    def __init__(self, scrabble_scores, dict_file):
        self.Rules = ScrabbleRules(scrabble_scores, dict_file)

    def calculate_word_score(self, word):
        pass

    def calculate_file_scores(self, f):
        pass

    def calculate_file_best(self, f):
        pass


if __name__ == '__main__':


