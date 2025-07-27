import pandas as pd
# it will transfer text data into numerical data
from sklearn.feature_extraction.text import CountVectorizer
# using Naive Bayes algorithm for text classification(train the model)
from sklearn.naive_bayes import MultinomialNB

import pickle  # For saving the trained model and vectorizer

file = pd.read_csv("textData.csv").dropna()  # Load the CSV file and drop any rows with missing values
text = file['Text']  # Extract the 'text' column
labels = file['Label']  # Extract the 'label' column

# Convert text data into numerical data using CountVectorizer
vectorizer = CountVectorizer() # This will convert text into a matrix of token counts
# It will create a vocabulary of all unique words in the text data
text_vectorized = vectorizer.fit_transform(text)

# Train the Naive Bayes(algorithm) model using the vectorized text data and labels
model = MultinomialNB()  # Create an instance of the Multinomial Naive Bayes classifier
model.fit(text_vectorized, labels)  # Fit the model to the training data

#--------------------------------------------------------------------
with open("vectorizer.pkl","wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)  # Save the vectorizer to a file

with open("model.pkl","wb") as model_file:
    pickle.dump(model, model_file)  # Save the trained model to a file   

with open("vectorizer.pkl","rb") as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)  # Load the vectorizer from the file

with open("model.pkl","rb") as model_file:
    loaded_model = pickle.load(model_file)  # Load the trained model from the file  

#-------------------------------------------------------------------------------      

# Function to predict the label of a new text input
# def predict_label(new_text):
#     new_text_vectorized = vectorizer.transform([new_text])  # Transform the new text into the same vectorized format
#     prediction = model.predict(new_text_vectorized)  # Predict the label using the trained model
#     return prediction[0]  # Return the predicted label


def predict_label(new_text):
    new_text_vectorized = loaded_vectorizer.transform([new_text])  # Transform the new text into the same vectorized format using the loaded vectorizer
    prediction = loaded_model.predict(new_text_vectorized)  # Predict the label using the loaded model
    return prediction[0]  # Return the predicted label

prediction = predict_label("enjoyed movie")  # Example usage of the predict_label function
print(f"Predicted label: {prediction}")  # Print the predicted label for the input