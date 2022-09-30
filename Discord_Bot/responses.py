
def handle_response(message) -> str:
    
    if message == 'hello':
        return 'Hey there!'
    
    if message == '$score solution_statement':
        return 'This function will return a score and a reason once the code is done!'