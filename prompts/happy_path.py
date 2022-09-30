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
            prompt = f"The following is a part of a bigger product spec and is meant to describe the path that a team must take to achieve a result. Score the text from 1-100 on how well it does its task. Explain why the score was given and provide specific feedback on what could be improved. \n {string}",
            temperature = 0.2,
            max_tokens = 512,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        return response["choices"][0]["text"]
    except Exception as e:
        return f"happy_path: {e}" # placeholder for now

"""
# for internal testing

TEST_INPUT = ""
print(happy_path_model(TEST_INPUT)) 
"""
