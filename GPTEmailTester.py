import openai

openai.api_key = "Insert your own personal API key here"

def classify_email(subject, body):
    prompt = f"""Classify the following email as 'Spam' or 'Ham':
    
    Subject: "{subject}"
    Body: "{body}"
    
    Answer:
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response["choices"][0]["message"]["content"].strip()

test_subject = "Win a Free iPhone!" # Results in "Spam". Change this up and see how the models respond!
test_body = "Congratulations! Click the link to claim your prize now."
print(classify_email(test_subject, test_body))
