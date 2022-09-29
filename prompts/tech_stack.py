import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("API_KEY")

def tech_stack_model(input):
    try:
        response = openai.Completion.create(
            model = "text-davinci-002",
            prompt = "The following information is a tech stack consisting of the programming languages, frameworks, a database, front-end tools, back-end tools, and applications connected via APIs that a company will use to build a product. Score the following information from 1-100 based on the quality of tech stack items and explain why the score was given. \n\ {}".format(input),
            temperature = 0.2,
            max_tokens = 512,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        return response["choices"][0]["text"]
    except:
        return "tech_stack error" # placeholder for now

"""
# for internal testing

test_input = ""
print(tech_stack_model(test_input))
"""