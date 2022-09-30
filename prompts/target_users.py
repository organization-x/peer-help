import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def target_users_model(string):
    """ To evaluate how well the product spec explains its target userbase

    Args:
        string (str): section of text extracted from Notion

    Returns:
        str: GPT's evaluation of the input
    """
    try:
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = f"The following paragraph is a solution statement. Provide a number from a scale of 1-100 that rates how well and effectively it is able to convey the intended clients and users of their product, alongside why the product is relevant to them. After providing a score, explain why the score was given and what could potentially be improved upon if anything. It should only focus on who the solution is for. \n {string}",
            temperature = 0.2,
            max_tokens = 512,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        return response["choices"][0]["text"]
    except Exception as e:
        return f"target_users: {e}" # placeholder for now

"""
# for internal testing

TEST_INPUT = ""
print(target_users_model(TEST_INPUT))
"""
