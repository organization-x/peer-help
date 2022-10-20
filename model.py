import openai
from notion_extraction import extract_product_spec_text, parse_product_spec_text, extract_id_from_url
import requests
import os
from dotenv import load_dotenv
#from text.peer import notion_token

# unused labels = ['', '', '', 'Success Criteria', 'Success Metrics', '', '', '', '']
    
# until the backend is implemented

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

import aiohttp
import asyncio
# bearer_token = os.environ['openai_api_key']

def get_prompts(parsed_product_spec):

    prompts = []

    label_to_prompt = {
        'Problem Statement' : {
            'prompt' : "The following paragraph is the problem statement section of a product specification. First, respond with feedback on how well the problem statement has been written. Next, explain why this feedback was given along with specific feedback on what can be improved. You must write several in-depth sentences.",
            'temperature' : 0.1,
            'max_tokens' : 512,
            'top_p' : 1,
            'frequency_penalty' : 0,
            'presence_penalty' : 0
        },
        'Solution Statement' : {
            'prompt' : "The following paragraph is the solution statement section of a product specification. First, respond with feedback on how well the solution statement has been written. Next, explain why this feedback was given along with specific feedback on what can be improved. You must write several in-depth sentences.",
            'temperature' : 0.1,
            'max_tokens' : 512,
            'top_p' : 1,
            'frequency_penalty' : 0,
            'presence_penalty' : 0
        },
        'Who Has This Problem?' : {
            'prompt' : "The following paragraph is explaining the audience or target userbase of a product specification. First, respond with feedback on how well the audience is decribed. Next, explain why this feedback was given along with specific feedback on what can be improved. You must write several in-depth sentences.",
            'temperature' : 0.2,
            'max_tokens' : 512,
            'top_p' : 1,
            'frequency_penalty' : 0,
            'presence_penalty' : 0
        },
        'Milestones' : {
            'prompt' : "The following paragraph is the milestones section of a product specification. First, respond with feedback on how well the milestones have been written. Next, explain why this feedback was given along with specific feedback on what can be improved. You must write several in-depth sentences.",
            'temperature' : 0.1,
            'max_tokens' : 512,
            'top_p' : 1,
            'frequency_penalty' : 0,
            'presence_penalty' : 0
        },
        'Schedule of Deliverables' : {
            'prompt' : "The following paragraph is the schedule section of a product specification. First, respond with feedback on how well the schedule has been planned. Next, explain why this feedback was given along with specific feedback on what can be improved. You must write several in-depth sentences.",
            'temperature' : 0.1,
            'max_tokens' : 512,
            'top_p' : 1,
            'frequency_penalty' : 0,
            'presence_penalty' : 0
        },
        'Tech Stack' : {
            'prompt' : "The following paragraph is the technology stack section of a product specification. First, respond with feedback on how well the technolgy stack has been written. Next, explain why this feedback was given along with specific feedback on what can be improved. You must write several in-depth sentences.",
            'temperature' : 0.2,
            'max_tokens' : 512,
            'top_p' : 1,
            'frequency_penalty' : 0,
            'presence_penalty' : 0
        },
        'Happy Path' : {
            'prompt' : "The following paragraph is the happy path section of a product specification. First, respond with feedback on how well the happy path conveys the general path needed to be taken in this project. Next, explain why this feedback was given along with specific feedback on what can be improved. You must write several in-depth sentences.",
            'temperature' : 0.1,
            'max_tokens' : 512,
            'top_p' : 1,
            'frequency_penalty' : 0,
            'presence_penalty' : 0
        }
    }

    for section in parsed_product_spec:
        if section in label_to_prompt:
            prompt = label_to_prompt[section]

            prompt['prompt'] += f"\n\n{parsed_product_spec[section]}"

            prompts.append(prompt)
    return prompts

async def get_text(session, url, params):

    async with session.post(url, json = params) as resp:
        prompt_text = await resp.json()
        return prompt_text['choices'][0]['text']

async def main(url):

    prompts = get_prompts(parse_product_spec_text(extract_product_spec_text(extract_id_from_url(url))))
    
    
    async with aiohttp.ClientSession(headers = {'authorization' : f'Bearer {openai_api_key_vc}'}) as session:

        tasks = []
        for prompt in prompts:
            url = 'https://api.openai.com/v1/engines/text-davinci-002/completions'
            tasks.append(asyncio.ensure_future(get_text(session, url, prompt)))

        feedbacks = await asyncio.gather(*tasks)
       
    total_feedback = '\n'.join(feedbacks)
    return total_feedback
    

    # for feedback in feedbacks:
    #     print(feedback)

    
    # feedback_summary = requests.post('https://api.openai.com/v1/engines/text-davinci-002/completions',
        
    #     headers = {'authorization' : f'Bearer {openai_api_key_vc}'},
    #     json = {
    #         'prompt' : f"The following text is written feedback of a product specification. Write a 150 WORD SUMMARY of the feedback and include key details.\n\nFEEDBACK\n\n{total_feedback}",
    #         'temperature' : 0.3,
    #         'max_tokens' : 512,
    #         'top_p' : 1,
    #         'frequency_penalty' : 0,
    #         'presence_penalty' : 0
    #     }
    # ).json()
 
    # return feedback_summary['choices'][0]['text']
























































































openai_api_key_vc = "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"