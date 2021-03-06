'''
    @author : Mounika2010
    Document Distance - A detailed description is given in the PDF
'''

import re
import math

def combine_dictionaries(dictionary_one, dictionary_two):
    '''
    two dictionaries are comibined
    '''
    dictionary = {}
    for word in dictionary_one:
        if word in dictionary_two:
            dictionary[word] = [dictionary_one[word], dictionary_two[word]]
    for word in dictionary_one:
        if word not in dictionary:
            dictionary[word] = [dictionary_one[word], 0]
    for word in dictionary_two:
        if word not in dictionary:
            dictionary[word] = [0, dictionary_two[word]]
    return dictionary


def calculate_similarity(dictionary_values):
    '''
    calculates similarity
    '''
    numerator = sum([k[0] * k[1] for k in dictionary_values.values()])
    den_one = math.sqrt(sum([k[0] ** 2 for k in dictionary_values.values()]))
    den_two = math.sqrt(sum([k[1] ** 2 for k in dictionary_values.values()]))
    return numerator/(den_one*den_two)

def create_dictionary(words_list):
    '''
    returns dictionary takes input as word list
    '''
    dictionary = {}
    stopwords = load_stopwords("stopwords.txt")
    for word in words_list:
        word = word.strip()
        if word not in stopwords and len(word) > 0:
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word] += 1
    return dictionary

def clean_given_text(text_input):
    '''
    removes special characters
    '''
    words = text_input.lower().strip().replace('\'', '')
    regex = re.compile('[^a-z]')
    words = regex.sub(" ", words).split(" ")
    return words

def similarity(text_input_one, text_input_two):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary_one = create_dictionary(clean_given_text(text_input_one))
    dictionary_two = create_dictionary(clean_given_text(text_input_two))
    dictionary = combine_dictionaries(dictionary_one, dictionary_two)
    return calculate_similarity(dictionary)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename_n:
        for line in filename_n:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
