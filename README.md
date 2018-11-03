#BACK-END Scrable:



###PL
Napisz skrpyt który policzy wynik z gry Scrabble na podstawie LETTER_SCORES.
Powinny być trzy tryby (dostępne przez linie komend):
* zwraca najwyższy wynik z pliku dictionary.txt
* liczy wynik dla słowa podanego jako argument z linii komend
* zwróć słowo o podanej wartości:
    * jeśli istnieje wiele słów, wybierz losowe
    * jeśli nie istnieje takie słowo, nie wyświetlaj niczego


Wymagania:
- Python3.7
- można uśywać modułówktóre są dostępne w standardowej bibliotece
- OOP
- dodatkowepunkty za testy
##
###ENG
Write a script that will tell score from scrabble game based on LETTER_SCORES.
There should be three options (available from command line):
* return highest score from dictionary.txt file
* return score of given word
* return word with given score:
   * if there is more than one word, choose randomly
   * if there is no such word, don't return/print anything


Requirements:
- Python3.7
- You can use modules from standard library
- OOP
- extra points for tests
##



```

SCRABBLES_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                    (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

LETTER_SCORES = {letter: score for score, letters in SCRABBLES_SCORES
                               for letter in letters.split()}
                               
```