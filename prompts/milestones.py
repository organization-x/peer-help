import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def milestones_model(string):
    """ To evaluate a product's milestones

    Args:
        string (str): section of text extracted from Notion

    Returns:
        str: GPT's evaluation of the input
    """
    try:
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = f"The following text is meant to describe the milestones of a team that is working to build a product. Score the text from 1-100 on how clear and realistic the milestones may be. After providing a score, write a few sentences explaining why this score was given. \n {string}",
            temperature = 0.2,
            max_tokens = 512,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        return response["choices"][0]["text"]
    except Exception as e:
        return f"milestones: {e}" # placeholder for now

"""
# for internal testing

TEST_INPUT = ""
print(milestones_model(TEST_INPUTS))
"""
