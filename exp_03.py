import nltk
from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import defaultdict
nltk.download('reuters')
nltk.download('punkt')

print("This is Vivek Singh Program")

# Load the Reuters corpus
# Create a dictionary to store the frequency of word sequences
model = defaultdict(lambda: defaultdict(lambda: 0))

# Iterate over each sentence in the Reuters corpus
for sentence in reuters.sents():
    # Convert the sentence to lowercase
    sentence = [word.lower() for word in sentence]
    # Generate the word sequences (bigrams and trigrams)
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(w1, w2)][w3] += 1

# Function to predict the next word given a sequence of words
def predict_next_word(words):
    # Convert the input words to lowercase
    words = [word.lower() for word in words]
    # Get the most likely next word based on the frequency
    next_word = max(model[tuple(words)].items(), key=lambda x: x[1])[0]
    return next_word
# Example usage
input_words = ['this', 'is']
next_word = predict_next_word(input_words)
print(f"The next word after '{' '.join(input_words)}' is '{next_word}'.")