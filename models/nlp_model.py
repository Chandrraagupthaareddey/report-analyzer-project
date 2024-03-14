import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Preprocess text (example)
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

# Sample medical report data (example)
reports = [
    {"text": "Patient presents with fever and cough. Diagnosis: pneumonia."},
    {"text": "Blood test results: Hemoglobin 12 g/dL, White Blood Cell Count 10,000/uL."},
    # Add more report examples
]

# Preprocess and vectorize report text
corpus = [preprocess_text(report["text"]) for report in reports]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Train machine learning model to classify report types (example)
y = ["respiratory" if "fever" in report["text"] else "blood test" for report in reports]
classifier = LogisticRegression()
classifier.fit(X, y)

# Sample query (example)
query = "What is the diagnosis of the patient with fever and cough?"

# Preprocess query text
processed_query = preprocess_text(query)

# Predict report type based on query
query_vector = vectorizer.transform([processed_query])
predicted_type = classifier.predict(query_vector)[0]

# Generate response based on predicted type
if predicted_type == "respiratory":
    response = "The patient is diagnosed with pneumonia."
elif predicted_type == "blood test":
    response = "The blood test results show Hemoglobin levels of 12 g/dL and White Blood Cell Count of 10,000/uL."

print("Response:", response)