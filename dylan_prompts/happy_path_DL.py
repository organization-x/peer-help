import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def happy_path_model(string):
    """ To evaluate a product's intended happy path

    Args:
        string (str): section of text extracted from Notion

    Returns:
        str: GPT's evaluation of the text
    """
    try:
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = f"The following paragraph is the happy path section of a product specification. First, evaluate the happy path and provide a score from 1-10. After, give specific feedback on what can be improved.\n\n\n{string}\n\n\nSCORE:",
            temperature = 0.5,
            max_tokens = 512,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        return f'SCORE:{response["choices"][0]["text"]}'
    except Exception as e:
        return f"happy_path: {e}" # placeholder for now

# for internal testing

PEER = "1. Prompt-engineering GPT-3 to numerically evaluate sections to determine the prompt that is given to the GPT-3 model for feedback generation.\
2. Prompt-engineering GPT-3 to generate feedback based on numerical scores given by the scoring method.\
3. Extracting and parsing text from Notion product specs into individual sections (problem statement, solution, etc.)\
4. Backend to feed sections to the scoring method to the GPT-3 model using a bot command and generating an embed."
EMAILGEN = "1. Email comes in from customer with a subject line, the sender’s name, and an adequate description of their question/problem.\
2. The user inputs the email and any relevant information into the WebApp\
3. The WebApp interfaces with the GPT-3 Model and outputs the response\
4. The user proofreads the response and will finds it adequate.\
5. The User pastes the email into their inbox and sends it."

print(happy_path_model(EMAILGEN))
