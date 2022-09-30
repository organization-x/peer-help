import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def solution_model(string):
    """ To evaluate a product's solution statement

    Args:
        string (str): section of text extracted from Notion

    Returns:
        str: GPT's evaluation of the input
    """
    try:
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = f"The following information is attempting to describe who may have a certain problem. Score this information from 1-100 based on how specific it is about who has this problem. Explain why the score was given. Do not score this information about how specific the actual problem is. \n {string}",
            temperature = 0.2,
            max_tokens = 512,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        return response["choices"][0]["text"]
    except Exception as e:
        return f"solution: {e}" # placeholder for now

"""
# for internal testing

TEST_INPUT = ""
print(solution_model(TEST_INPUT))
"""
