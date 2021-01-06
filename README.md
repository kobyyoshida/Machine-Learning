Koby Yoshida
2329586
koyoshida@chapman.edu

Known bugs
Does not generate 20 words per line

References
Erin Lee, Michael Lewson
https://www.udemy.com/course/unsupervised-machine-learning-hidden-markov-models-in-python/

# H1 Explanation
I was struggling with this assignment and found this Udemy course that shows a similar program, but has a few key differences.
I will list the differences here to explain the methodology behind this program and show my understanding.

**End of Line Probability**
One major difference is in order to calculate where a line should end in our generated poem, it takes the last pair of words
at the end of each line and pairs it to a key/value that looks like this: ('word1', 'word2'): {'END': probability of ending}.
It looks for that pair of words and generates the likelihood that those words are used at the end of a sentence.
(I feel its fair to lose a bit of points here since I couldnt figure out how to restructure the dictionary for when the EOL was read, 
instead of storing 'END' and the probability of that word being the end, to just continue to the next line. This is why it doesnt 
generate 20 words per line)

**No 3D array (No Array of arrays of arrays)**
Another major difference between my program and the direction of the program we worked on in class is this:

From my understanding in class, we wanted to populate a 3D array similar to the DNA sequence to hold the counts. I was having trouble dynamically populating the array, and chose this method instead using a dictionary of dictionaries to hold the counts/probabilities.

Instead of using a 3D array to track the trajectory of words and their probabilites, every word pair is stored in a dictionary 
as a key, with the value being another dictionary holding the third word as a key and the value being the probability of the 3-word-combination.

Example of objects in the dictionary (from the transitions dictionary)
('his', 'bright'): {'sword': 1.0}

If there are multiple third-word possibliites to a pair of words, the other third word possiblilities are stored like this:

Example of multiple possiblities
('the', 'hart'): {'END': 0.5, 'he': 0.5}

Here the program has found "the hart" in two places in the program, once followed by EOL and once by 'he'

# H1 Understanding of Markov
The markov model in this nursery rhyme assignment predicts the selection of words based on the probabilities of the two preceeding word before it.
This can be shown in the generate_word(d) function where we sum the probabilities of the words passed in, and return a term based off the cumulative probabilities.
