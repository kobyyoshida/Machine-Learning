Koby Yoshida
2329586
koyoshida@chapman.edu

Known bugs
Does not generate 20 words per line

References
Erin Lee, Michael Lewson, Elmer Camargo
https://www.udemy.com/course/unsupervised-machine-learning-hidden-markov-models-in-python/

# H1 Explanation
I was struggling with this assignment and found a Udemy course that teaches a similar program.
I will list the differences here to explain the methodology behind this program and show my understanding.

**End of Line Probability**
One difference in my program is that in order to calculate where a line should end in our generated poem, it takes the last pair of words
at the end of a line and pairs it to a key/value that looks like this: ('word1', 'word2'): {'END': probability of ending}.
It looks for that pair of words and generates the likelihood that those words are used at the end of a sentence, essentially treating
the end of a line like a word, as well as a stopping point to prevent the for loop from moving the current_word variable to point out of bounds.

Later in the program when generating words, if a key (word pair) is selected from our transitions dictionary that has a value of END, that particular line
will end in our generated poem. This allows for dynamically sized lines of text, and for more realistic sentences with proper words to end a sentence. 
This is also why it does not generate 20 words per line.


# H1 Understanding of Markov
The markov model in this nursery rhyme assignment predicts the selection of words based on the probabilities of the two preceeding word before it.
This can be shown in the generate_word(d) function where we sum the probabilities of the words passed in, and return a term based off the cumulative probabilities.
