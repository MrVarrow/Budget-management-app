import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Read the first CSV file into a DataFrame
df = pd.read_csv('DataSetFood/combined_dataset.csv')

X_train, X_test, y_train, y_test = train_test_split(df['Words'], df['is_food'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_vectorized, y_train)

y_pred = model.predict(X_test_vectorized)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

new_word = "taco"
new_word_vectorized = vectorizer.transform([new_word])
prediction = model.predict(new_word_vectorized)
if prediction[0] == 1:
    print(f"{new_word} is a food.")
else:
    print(f"{new_word} is not a food.")