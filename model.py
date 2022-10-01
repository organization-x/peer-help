from prompts.problem import problem_model
from prompts.solution import solution_model
from prompts.target_users import target_users_model
from prompts.tech_stack import tech_stack_model
from prompts.milestones import milestones_model
from prompts.schedule import schedule_model
from prompts.happy_path import happy_path_model
from notion_extraction import extract_product_spec_text
from notion_extraction import parse_product_spec_text
from notion_extraction import page_id

#from text.peer import notion_token

# unused labels = ['', '', '', 'Success Criteria', 'Success Metrics', '', '', '', '']
    
# until the backend is implemented

print(problem_model(parse_product_spec_text(extract_product_spec_text(page_id))['Problem Statement']))
print(solution_model(parse_product_spec_text(extract_product_spec_text(page_id))['Solution Statement']))
print(target_users_model(parse_product_spec_text(extract_product_spec_text(page_id))['Who Has This Problem?']))
print(tech_stack_model(parse_product_spec_text(extract_product_spec_text(page_id))['Tech Stack']))
print(milestones_model(parse_product_spec_text(extract_product_spec_text(page_id))['Milestones']))
print(schedule_model(parse_product_spec_text(extract_product_spec_text(page_id))['Schedule of Deliverables']))
print(happy_path_model(parse_product_spec_text(extract_product_spec_text(page_id))['Happy Path']))
