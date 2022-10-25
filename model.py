from notion_extraction import extract_product_spec_text, parse_product_spec_text, extract_id_from_url
from prompts import happy_path, milestones, problem, schedule, solution, success_criteria, target_users, tech_stack
import requests
import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY1']

def main(url):

    prompts = extract_product_spec_text(extract_id_from_url(url))

    if prompts == 'invalid':
        return 'We could not complete the grading. Please make sure that you\'ve integrated PEER with your Notion page.'
    prompts = parse_product_spec_text(prompts)

    if prompts == 'invalid':
        return 'We could not complete the grading. Please make sure that you\'re product spec is organized using headings.'
        
    prompts = {key : value for key, value in prompts.items() if len(value) > 0}

    feedbacks = {}
    
    if 'Problem Statement' in prompts:
        feedbacks['Problem Statement'] = happy_path.happy_path_model(prompts['Problem Statement'])
    if 'Solution Statement' in prompts:
        feedbacks['Solution Statement'] = solution.solution_model(prompts['Solution Statement'])
    if 'Who Has This Problem?' in prompts:
        feedbacks['Who Has This Problem?'] = target_users.target_users_model(prompts['Who Has This Problem?'])
    if 'Success Criteria' in prompts:
        feedbacks['Success Criteria'] = success_criteria.success_criteria(prompts['Success Criteria'])
    if 'Milestones' in prompts:
        feedbacks['Milestones'] = milestones.milestones_model(prompts['Milestones'])
    if 'Schedule of Deliverables' in prompts:
        feedbacks['Schedule of Deliverables'] = schedule.schedule_model(prompts['Schedule of Deliverables'])
    if 'Tech Stack' in prompts:
        feedbacks['Tech Stack'] = tech_stack.tech_stack_model(prompts['Tech Stack'])
    if 'Happy Path' in prompts:
        feedbacks['Happy Path'] = happy_path.happy_path_model(prompts['Happy Path'])
    """
    total_feedback = '\n\n'.join(feedbacks)

    
    feedback_summary = response = openai.Completion.create(
        model = "text-davinci-002",
        prompt = f"The following text is written feedback of a product specification. Write a one-hundred fifty word summary of the feedback. The summary must be one paragraph and well-written.\n\nFEEDBACK:\n\n{total_feedback}\n\nWell written summary of the feedback:\n\n",
        temperature = 0.7,
        max_tokens = 512,
        top_p = 0.9,
        frequency_penalty = 0,
        presence_penalty = 0
    )

    if len(feedback_summary["choices"][0]["text"]) == 0:
        return 'PEER seems to have malfunctioned. Those darn LLM parameters. Let us know by pinging the @peer role and we will get this fixed.'
    
    return feedback_summary["choices"][0]["text"]
    """
    return feedbacks