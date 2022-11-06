import requests
import os
from dotenv import load_dotenv
import openai
import time


load_dotenv()
notion_token = os.getenv('NOTION_TOKEN')

def extract_id_from_url(url): 
    return url.split('-')[-1]

def extract_product_spec_text(page_id):

    texts = []

    def extract_data_from_notion_page(page_id):

        url = f'https://api.notion.com/v1/blocks/{page_id}/children?page_size=100'

        headers = {
            'accept': 'application/json',
            'Notion-Version': '2022-06-28',
            'authorization': f'Bearer {notion_token}'
        }

        response = requests.get(url, headers=headers)
        results = response.json()['results']

        for result in results:

            if not result['has_children']: # If the block has no children

                result_type = result['type']

                if 'rich_text' in result[result_type].keys():

                    if result[result_type]['rich_text']:
                        
                        for rich_text in result[result_type]['rich_text']:
                            texts.append((rich_text['plain_text'], result_type))

            else: # If the block has children, recursively visit each child block.

                result_type = result['type']

                if 'rich_text' in result[result_type].keys():

                    if result[result_type]['rich_text']:
                        
                        for rich_text in result[result_type]['rich_text']:
                            texts.append((rich_text['plain_text'], result_type))

                extract_data_from_notion_page(result['id'])
    try:
        extract_data_from_notion_page(page_id)
    
        return texts
    except Exception as e:
        print(e)
        return 'invalid'

def jaccard_similarity(list1, list2): # Similarity metric
    
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(set(list1)) + len(set(list2))) - intersection
    return float(intersection) / union

def match_name_to_label(name): # Matches a name to a product spec label
    
    labels = ['Problem Statement', 'Solution Statement', 'Who Has This Problem?', 'Success Criteria', 'Success Metrics', 'Milestones', 'Schedule of Deliverables', 'Tech Stack', 'Happy Path']
    
    highest_similarity_score = 0
    most_similar = None
    
    openai.api_key = os.getenv("OPENAI_API_KEY1")

    labels = ['Problem Statement', 'Solution Statement', 'Who Has This Problem?', 'Success Criteria', 'Success Metrics', 'Milestones', 'Schedule of Deliverables', 'Tech Stack', 'Happy Path']

    questionable_header = name
    response = openai.Completion.create(
    model="text-curie-001",
    prompt=f"prompt: answer the following question only using the header_list, then say where they are in the list\n\nheader_list: 'Problem Statement', 'Solution Statement', 'Who Has This Problem?', 'Success Criteria', 'Success Metrics', 'Milestones', 'Schedule of Deliverables', 'Tech Stack', 'Happy Path'\n\nquestion: out of the header_list which one is most similar to the header \"Other Ideas Further areas of improvement:\"?\n\noutput: \"Other Ideas Further areas of improvement\" is most similar to the header \"Milestones\". milestones is the sixth in header_list\n\nquestion: out of the header_list which one is most similar to the header \"Success Criteria\"?\n\noutput: \"Success Criteria\" is most similar to the header \"Success Criteria\" Success Criteria is the fourth in header_list.\n\nquestion: out of the header_list which one is most similar to the header \"What The Product Will Not Do\"?\n\noutput: \"What The Product Will Not Do\" is most similar to the header  \"Success Criteria\" Success Criteria is the fourth in header_list.\n\nquestion: out of the header_list which one is most similar to the header \"{questionable_header}\"?\n\noutput: \"{questionable_header}\" is most similar to the header  ",
    temperature=1,
    max_tokens=75,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    corrected_header = response["choices"][0]["text"]
    redone_lables = corrected_header.replace('"',"")
    for x in labels:
       if x in redone_lables: 
            print('ai generated labels worked', x)
            return x
            
        
    for y in range(2): print('jacard runnging as backup for[gtp3 failure]')
    print(f"'{redone_lables}' is the out come of '{questionable_header}' delete this line of code later")
    for label in labels: # Finds the label with the highest similarity score
                    
        similarity_score = jaccard_similarity(label.split(), name.split())
                
        if similarity_score > highest_similarity_score:
                    
            most_similar = label
            highest_similarity_score = similarity_score
            
    return most_similar


def parse_product_spec_text(product_spec_text): # separates product spec text into different sections. 
    
    parsed_text = {}
    
    current_heading = None
    
    for text_piece in product_spec_text:
        
        try:
            if text_piece[1][:7] == 'heading':
            
                current_heading = text_piece[0]
                parsed_text[current_heading] = []
        
            elif current_heading != None:
            
                parsed_text[current_heading].append(text_piece[0])
        except Exception as e:
            pass
    
    if len(parsed_text.items()) == 0:
        print('very little')
        print(parsed_text)
        return 'invalid'
    parsed_text = {match_name_to_label(key) : '\n'.join(value) for key, value in parsed_text.items()}

    return parsed_text
