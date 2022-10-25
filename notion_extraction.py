import requests
import os

notion_token = os.environ['NOTION_TOKEN1']

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
