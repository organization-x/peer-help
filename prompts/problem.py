import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def problem_model(input):
    try:
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = "The following text is a problem statement that is meant to be a brief, but clear description of an issue that needs to be addressed. Score the text from 1-100 on how well it does its job. Explain why the score was given. Provide specific feedback on what could be improved and where. \n\ {}".format(input),
            temperature = 0.2,
            max_tokens = 512,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        return response["choices"][0]["text"]
    except Exception as e:
        return "problem error" # placeholder for now

""" 
# for internal testing

test_input = ""

print(problem_model(test_input)) """
