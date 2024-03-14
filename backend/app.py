# backend/app.py

from flask import Flask, request
import spacy
import pymongo
import psycopg2

app = Flask(__name__)

# Initialize MongoDB and PostgreSQL connections
mongo_client = pymongo.MongoClient('mongodb://mongodb:27017/')
mongo_db = mongo_client['file_data']
mongo_collection = mongo_db['files']

postgres_conn = psycopg2.connect(
    host='postgresql',
    user='postgres',
    password='password',
    database='extracted_data'
)
postgres_cursor = postgres_conn.cursor()

# Load NLP model (e.g., spaCy)
nlp = spacy.load('en_core_web_sm')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    # Store raw file data in MongoDB
    file_id = mongo_collection.insert_one({'filename': file.filename, 'data': file.read()}).inserted_id

    # Perform NLP tasks (e.g., extract text from PDF)
    text = extract_text_from_pdf(file)

    # Extract relevant information using NLP
    extracted_data = process_nlp(text)

    # Store extracted data in PostgreSQL
    store_data_in_postgres(extracted_data)

    return 'File uploaded and processed successfully'

def extract_text_from_pdf(file):
    # Add code to extract text from PDF (e.g., using PyPDF2 or pdfplumber)
    # Return extracted text
    pass

def process_nlp(text):
    # Add code to process text using NLP model (e.g., spaCy)
    # Return extracted data
    pass

def store_data_in_postgres(data):
    # Add code to store extracted data in PostgreSQL
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)