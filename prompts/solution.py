import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def solution_model(input):
    try:
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = "The following information is attempting to describe who may have a certain problem. Score this information from 1-100 based on how specific it is about who has this problem. Explain why the score was given. Do not score this information about how specific the actual problem is. \n\ {}".format(input),
            temperature = 0.2,
            max_tokens = 512,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        return response["choices"][0]["text"]
    except Exception as e:
        return "solution error" # placeholder for now
        
"""
# for internal testing

test_input = ""
print(solution_model(test_input))
"""
