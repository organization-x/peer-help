from dotenv import load_dotenv
from notion_extraction import extract_product_spec_text, parse_product_spec_text, extract_id_from_url
from prompts import happy_path, milestones, problem, schedule, solution, success_criteria, target_users, tech_stack
import requests
import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY1')

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
        feedbacks['Problem Statement'] = f"**PEER Feedback**\n\n{problem.problem_model(prompts['Problem Statement'])}"
        feedbacks['Problem Statement'] += f"\n\n**Suggested Rewrite Using PEER's Feedback**:\n\n{problem.suggested_problem_statement_rewrite(prompts['Problem Statement'], feedbacks['Problem Statement'])}"
    if 'Solution Statement' in prompts:
        feedbacks['Solution Statement'] = f"**PEER Feedback**\n\n{solution.solution_model(prompts['Solution Statement'])}"
        feedbacks['Solution Statement'] += f"\n\n**Suggested Rewrite Using PEER's Feedback**:\n\n{problem.suggested_problem_statement_rewrite(prompts['Solution Statement'], feedbacks['Solution Statement'])}"
    if 'Who Has This Problem?' in prompts:
        feedbacks['Who Has This Problem?'] = f"**PEER Feedback**\n\n{target_users.target_users_model(prompts['Who Has This Problem?'])}"
        feedbacks['Who Has This Problem?'] += f"\n\n**Suggested Rewrite Using PEER's Feedback**:\n\n{target_users.suggested_target_users_rewrite(prompts['Who Has This Problem?'], feedbacks['Who Has This Problem?'])}"
    if 'Success Criteria' in prompts:
        feedbacks['Success Criteria'] = f"**PEER Feedback**\n\n{success_criteria.success_criteria(prompts['Success Criteria'])}"
        feedbacks['Success Criteria'] += f"\n\n**Suggested Rewrite Using PEER's Feedback**:\n\n{success_criteria.suggested_success_criteria_rewrite(prompts['Success Criteria'], feedbacks['Success Criteria'])}"
    if 'Milestones' in prompts:
        feedbacks['Milestones'] = f"**PEER Feedback**\n\n{milestones.milestones_model(prompts['Milestones'])}"
        feedbacks['Milestones'] += f"\n\n**Suggested Rewrite Using PEER's Feedback**:\n\n{milestones.suggested_milestones_rewrite(prompts['Milestones'], feedbacks['Milestones'])}"
    if 'Schedule of Deliverables' in prompts:
        feedbacks['Schedule of Deliverables'] = f"**PEER Feedback**\n\n{schedule.schedule_model(prompts['Schedule of Deliverables'])}"
        feedbacks['Schedule of Deliverables'] += f"\n\n**Suggested Rewrite Using PEER's Feedback**:\n\n{schedule.suggested_schedule_rewrite(prompts['Schedule of Deliverables'], feedbacks['Schedule of Deliverables'])}"
    if 'Tech Stack' in prompts:
        feedbacks['Tech Stack'] = f"**PEER Feedback**\n\n{tech_stack.tech_stack_model(prompts['Tech Stack'])}"
        feedbacks['Tech Stack'] += f"\n\n**Suggested Rewrite Using PEER's Feedback**:\n\n{tech_stack.suggested_tech_stack_rewrite(prompts['Tech Stack'], feedbacks['Tech Stack'])}"
    if 'Happy Path' in prompts:
        feedbacks['Happy Path'] = f"**PEER Feedback**\n\n{happy_path.happy_path_model(prompts['Happy Path'])}"
        feedbacks['Happy Path'] += f"\n\n**Suggested Rewrite Using PEER's Feedback**:\n\n{happy_path.suggested_happy_path_rewrite(prompts['Happy Path'], feedbacks['Happy Path'])}"
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
