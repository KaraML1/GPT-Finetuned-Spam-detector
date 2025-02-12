# GPT-Finetuned-Spam-detector
  Utilizes OpenAI's API and opensourced datasets to detect whether or not an email is "Spam" or "Ham" (legitimate). By leveraging LLMs, the system can analyze email content and improve detection accuracy beyond traditional spam filters.

## Installation & Setup
1. Clone the Repository

    First, download the project files by cloning the repository:
    
    git clone https://github.com/KaraML1/GPT-Finetuned-Spam-detector.git
    cd GPT-Finetuned-Spam-Detector

2. Install Dependencies

      Ensure you have Python installed and install the required dependencies using requirements.txt:
      
      pip install -r requirements.txt
      
      This will install essential libraries such as:
      
          openai – For interacting with OpenAI's API
          pandas – For handling datasets

3. Set Up OpenAI API Key

    To use OpenAI’s API, you need an API key. This is a variable for your convenience.

## Running the Email Classification Script
  The main script, GPTEmailTester.py, takes an email as input (subject + body of the email) and classifies it as Spam or Ham using OpenAI's ChatGPT 4o model. Change the variables located at the bottom of the script and run the program.
