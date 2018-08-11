'''
@author : Mounika2010
Exercise: Assignment-1              
The first step is to implement some code that allows us to calculate
the score for a single word. The function get_word_score should accept as INPUT
a string of lowercase letters (a word) and return the integer score for that word,
using the game's scoring rules.
'''

def get_word_score(word, n_inp):
    '''
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see scrabble_letter_values)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    '''

    scrabble_letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    b_wrd = list(word)
    score = 0
    length = len(word)
    for key in b_wrd:
        if key in scrabble_letter_values:
            score = score + scrabble_letter_values[key]
    score = score * length
    if length == 7:
        return score + 50
    else:
        return score

def main():
    '''
    Main function for the given problem
    '''

    print(get_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()