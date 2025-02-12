import pandas as pd
import openai
import re
import os

# Load the dataset
df = pd.read_csv("spam_ham_dataset.csv")

# Key
OPENAI_API_KEY = "INSERT YOUR OWN PERSONAL API KEY HERE"

# Function to clean email text
def clean_text(text):
    # Clean email text by removing HTML, special characters, and extra spaces
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower().strip()
    return text

# Apply cleaning to the email body column 
df["text"] = df["text"].apply(clean_text)

openai.api_key = OPENAI_API_KEY
def classify_email(subject, body):
    """Classify an email as Spam or Ham using OpenAI's API."""
    prompt = f"""Classify the following email as 'Spam' or 'Ham':
    
    Subject: "{subject}"
    Body: "{body}"
    
    Answer:
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# Text to Test
test_subject = "Win a Free iPhone!"
test_body = "Congratulations! Click the link to claim your prize now." # This example results in "Spam". Use your own personal emails and they will result in "Ham"!
print(classify_email(test_subject, test_body))
