from scrabble import Referee

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"), (4, "F H V W Y"), (5, "K"), (8, "J X"),
                   (10, "Q Z")]

Ref = Referee(scrabble_scores, 'dictionary.txt')


def test_short_word_score():
    word = "ala"
    assert Ref.word_score(word) == 3


def test_mid_word_score():
    word = "alania"
    assert Ref.word_score(word) == 6


def test_long_word_score():
    word = "redundancy"
    assert Ref.word_score(word) == 17


def test_highest_score_from_dictionary():
    word, score = Ref.dictionary_top_n(1)
    assert word == 'oxyphenbutazone'
    assert score == 41


def test_find_word_with_score_no_such_word():
    word = Ref.word_with_score(0)
    assert word is None


def test_find_word_with_score_no_such_word_two():
    word = Ref.word_with_score(1000000)
    assert word is None


def test_find_word_with_score_some_word():
    word = Ref.word_with_score(12)
    assert Ref.word_score(word) == 12

