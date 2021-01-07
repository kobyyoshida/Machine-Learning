# https://deeplearningcourses.com/c/unsupervised-machine-learning-hidden-markov-models-in-python
# https://udemy.com/unsupervised-machine-learning-hidden-markov-models-in-python

from __future__ import print_function, division
from future.utils import iteritems
from builtins import range

#numpy only used to generate random number for selecting a starting value
import numpy as np
import string

starting_words = {} # first words of a phrase
second_word_dictionary = {}
transitions = {}

#inserts key/value to one of the dictionaries above
def add2dict(dictionary, key, value):
    if key not in dictionary:
        #Create new dictionary entry that holds an empty list
        dictionary[key] = []
    #Append the value to the list we just created
    dictionary[key].append(value)

for line in open('nursery_rhymes.txt'):
    
    line = line.translate(str.maketrans('','',string.punctuation)) #I dont know why i had to separate this, but it wouldnt work without it
    line_of_words = line.lower().strip().split()

    for i in range(len(line_of_words)):
        current_word = line_of_words[i]
        #First word 
        if i == 0:
            # measure the distribution of the first word
            starting_words[current_word] = starting_words.get(current_word, 0.) + 1
        else:
            prev_word = line_of_words[i-1]
            if i == len(line_of_words) - 1:
                # measure probability of ending the line
               add2dict(transitions, (prev_word, current_word), 'END') #Takes the last word of a line like another word
            #since we are reading in from a single line, this offers more realistic words towards the end of sentences
            if i == 1:
                # measure probability of second word given only first word
                add2dict(second_word_dictionary, prev_word, current_word)
            else:
                #Set prev_word2 to the new word, 2 words back
                prev_word2 = line_of_words[i-2]
                add2dict(transitions, (prev_word2, prev_word), current_word) #calculate probability of word with 2 previous words


# normalize counts to probabilities
total_starting_words = sum(starting_words.values()) #sum to convert starting_words dict to probabilites
for current_word, count in iteritems(starting_words):
    #print("CURRENT WORD:", current_word)
    #print("COUNT: ", count)
    starting_words[current_word] = count / total_starting_words

#translates to probabilities
def toProbs(vals):

    dictionary = {}
    total = len(vals)
    for t in vals:
        dictionary[t] = dictionary.get(t, 0.) + 1
    #iteritems iterates through a dictionary key/value pairs from header file __future__
    for word, count in iteritems(dictionary):
        dictionary[word] = count / total #divide each element by the total to convert to probability
    return dictionary

for prev_word, vals in iteritems(second_word_dictionary):
    # replace list with dictionary of probabilities
    second_word_dictionary[prev_word] = toProbs(vals) 


for key, vals in iteritems(transitions):
    transitions[key] = toProbs(vals)

def generate_word(dictionary):
    #we select a rand num here to ensure that our probabilities are indeed being used properly with lower probabilities appearing less often
    rand_num = np.random.random() 
    cumulative = 0 #count probabilities so far
    #we track the sum of the probabilities for each term
    for term, prob in iteritems(dictionary):
        cumulative += prob
        if rand_num < cumulative:
            return term

def generate():
    #print(transitions)
    for i in range(30):
        sentence =[]
        count = 0

        # generate a starting_words word randomly (not based off probability)
        word0 = generate_word(starting_words)
        sentence.append(word0)

        # generate second word randomly
        word1 = generate_word(second_word_dictionary[word0])
        sentence.append(word1)

        while True:
            # generate the rest of the words based on the previous 2 word probabilities
            word2 = generate_word(transitions[(word0, word1)]) #pass in the first 2 words compared with the probabilites of all other words based on that word pair
            #print("WORD 2: ", word2)
            #This 'END' check looks for a pair of words that occur at the end of a line
            #End allows us to get more realistic words towards the end of a line
            if word2 == 'END':# and word_count == 20
                break
            sentence.append(word2)
            word0 = word1 #set words up for next iteration 
            word1 = word2
        print(' '.join(sentence))

generate()