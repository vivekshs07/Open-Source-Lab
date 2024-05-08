import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Preprocess the input text
def preprocess_text(text):
    # Tokenize the text
    tokens = nltk.word_tokenize(text.lower())
    
    # Lemmatize the tokens
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join the lemmatized tokens back into a string
    preprocessed_text = ' '.join(lemmatized_tokens)
    
    return preprocessed_text

# Define the chatbot function
def chatbot():
    # Define a list of predefined responses
    responses = [
        "Hello!",
        "How can I help you?",
        "Sorry, I don't understand.",
        "Please provide more information.",
        "Thank you!",
        "Goodbye!"
    ]
    
    # Get user input
    user_input = input("User: ")
    
    # Preprocess the user input
    preprocessed_input = preprocess_text(user_input)
    
    # Calculate the TF-IDF vectors for the predefined responses
    vectorizer = TfidfVectorizer()
    response_vectors = vectorizer.fit_transform(responses + [preprocessed_input])
    
    # Calculate the cosine similarity between the user input and the predefined responses
    similarity_scores = cosine_similarity(response_vectors[-1], response_vectors[:-1]).flatten()
    
    # Find the index of the most similar response
    most_similar_index = similarity_scores.argmax()
    
    # Get the most similar response
    response = responses[most_similar_index]
    
    # Print the response
    print("Chatbot:", response)

# Run the chatbot
while True:
    chatbot()