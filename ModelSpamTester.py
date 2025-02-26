import pandas as pd
import openai
from openai import OpenAI
import os


# Load the Excel file (update the filename as needed)
input_excel = "testDataSet.xlsx"  # Ensure this file contains 'Label' and 'Text' columns
output_excel = "outputResults.xlsx"

os.environ["OPENAI_API_KEY"] = "Insert your own personal API Key"
client = OpenAI()

# Load the dataset
df = pd.read_excel(input_excel)

# Initialize OpenAI client
client = OpenAI()

# Store results
results = []
correct = 0

for _, row in df.iterrows(): # Iterate through the entire test dataset (Mine contained only ~200)
    text = row['Text']
    actual_label = row['Label']
    
    # Call the fine-tuned model
    response = client.chat.completions.create(
        model="Insert your model here",
        messages=[
            {"role": "system", "content": "You are a bot that exclusively determines whether text is spam or 'ham' (legitimate)"},
            {"role": "user", "content": f"Determine whether this text is spam or ham: {text}"} # Changing this allows you to customize the responses. ie) Make the model explain why
        ],
        response_format={"type": "text"},
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    predicted_label = response.choices[0].message.content.strip().lower()
    
    # Track accuracy
    if predicted_label == actual_label.lower():
        correct += 1
    
    results.append([actual_label, text, predicted_label])

# Save results to a new Excel file, including the model's response
df_results = pd.DataFrame(results, columns=["Actual Label", "Text", "Predicted Label"])
df_results.to_excel(output_excel, index=False)

# Print the model's accuracy
accuracy = correct / len(df) * 100
print(f"Model Accuracy: {correct}/{len(df)} ({accuracy:.2f}%)")
