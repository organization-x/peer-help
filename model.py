from notion_extraction import extract_product_spec_text, parse_product_spec_text, extract_id_from_url
from prompts import happy_path, milestones, problem, schedule, solution, success_criteria, target_users, tech_stack
import requests
import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY1')

def main(url):

    prompts = parse_product_spec_text(extract_product_spec_text(extract_id_from_url(url)))
    prompts = {key : value for key, value in prompts.items() if len(value) > 0}
    
    feedbacks = []
    
    if 'Problem Statement' in prompts:
        feedbacks.append(happy_path.happy_path_model(prompts['Problem Statement']))
    if 'Solution Statement' in prompts:
        feedbacks.append(solution.solution_model(prompts['Solution Statement']))
    if 'Who Has This Problem?' in prompts:
        feedbacks.append(target_users.target_users_model(prompts['Who Has This Problem?']))
    if 'Success Criteria' in prompts:
        feedbacks.append(success_criteria.success_criteria(prompts['Success Criteria']))
    if 'Milestones' in prompts:
        feedbacks.append(milestones.milestones_model(prompts['Milestones']))
    if 'Schedule of Deliverables' in prompts:
        feedbacks.append(schedule.schedule_model(prompts['Schedule of Deliverables']))
    if 'Tech Stack' in prompts:
        feedbacks.append(tech_stack.tech_stack_model(prompts['Tech Stack']))
    if 'Happy Path' in prompts:
        feedbacks.append(happy_path.happy_path_model(prompts['Happy Path']))

    
    return feedbacks

    # FOR SUMMARIZATION TESTING
    # feedback_summary = response = openai.Completion.create(
    #     model = "text-davinci-002",
    #     prompt = f"The following text is written feedback of a product specification. Write a one-hundred fifty word summary of the feedback. The summary must be one paragraph and well-written.\n\nFEEDBACK:\n\n{total_feedback}\n\nWell written summary of the feedback:\n\n",
    #     temperature = 0.7,
    #     max_tokens = 512,
    #     top_p = 0.8,
    #     frequency_penalty = 0,
    #     presence_penalty = 0
    # )
    
    # return feedback_summary["choices"][0]["text"]


















































































