import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Define your training data
sentences = [
    "I am going to the",
    "She is reading a",
    "He likes to play",
    "We went to the",
    "They are having a"
]
next_words = [
    "store",
    "book",
    "soccer",
    "park",
    "party"
]

# Create a vocabulary of unique words
words = set()
for sentence in sentences:
    words.update(sentence.split())
word_to_index = {word: i for i, word in enumerate(words)}
index_to_word = {i: word for i, word in enumerate(words)}

# Convert sentences and next_words to numerical sequences
X = np.zeros((len(sentences), len(words)), dtype=np.bool)
y = np.zeros((len(sentences), len(words)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, word in enumerate(sentence.split()):
        X[i, word_to_index[word]] = 1
    y[i, word_to_index[next_words[i]]] = 1

# Build the RNN model
model = Sequential()
model.add(LSTM(128, input_shape=(len(words),), return_sequences=True))
model.add(Dense(len(words), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(X, y, epochs=100, batch_size=32)

# Generate predictions
input_sentence = "I am"
input_sequence = np.zeros((1, len(words)), dtype=np.bool)
for t, word in enumerate(input_sentence.split()):
    input_sequence[0, word_to_index[word]] = 1
predictions = model.predict(input_sequence)[0]
next_word_index = np.argmax(predictions)
next_word = index_to_word[next_word_index]

print(f"The next word after '{input_sentence}' is '{next_word}'")