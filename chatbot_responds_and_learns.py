# How To Build A Chat Bot That along with giving answers, also learns From The User In Python Tutorial
"""
 code : 
    created using chatgpt4 and then the parametrs are tuned based on the used case:    https://www.youtube.com/watch?v=CkkjXTER2KE
    get_close_matches is used to find the match.
    Change the value in  find_best_match to get more than one response or change the similarity cutoff percentage
 knowledge base : 
    is the json file. 
    this knowledge base.json will fill up automatically as the user will type in the question
    based on json file because the user typed stuff goes to json file and thus the training takes place using the data stored in the json file

"""
import json
from difflib import get_close_matches  # going to give us the best matches

# loading the knowledge base 
def load_knowledge_base(file_path:str) -> dict:
    with open(file_path,'r') as file:
        data:dict =json.load(file)
    return data    

# save the knowlwedge to knowledge base so that that can be used for the next time 
def save_knowledge_base(file_path:str, data:dict):
    with open(file_path,'w') as file:
        json.dump(data,file,indent=2)

# find best match from the dictionary
def find_best_match(user_question:str, questions:list[str]) -> str | None:
    matches: list = get_close_matches(user_question,questions,n=1,cutoff=0.6) # n=1 because we want one answer but can be changed to 2 or 3 etc. if response is 60% or more similar thus 0.6 cutoff
    return matches[0] if matches else None

def get_answer_for_question(question:str, knowledge_base:dict) -> str|None:
    for q in knowledge_base['questions']:
        if q['question'] == question:
            return q['answer']

def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input : str = input('You:')

        if user_input.lower() == 'quit':
            break
        best_match:str|None = find_best_match(user_input, [q["question"] for q in knowledge_base['questions']])
        if best_match:
            answer:str = get_answer_for_question(best_match,knowledge_base)
            print(f'Bot:{answer}')  # because answer is the formatted string thus like this syntax

        else: 
            print('Bot: I don\'t know the answer can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')
            if new_answer.lower()!='skip':
                knowledge_base['questions'].append({'question':user_input,'answer': new_answer})
                save_knowledge_base('knowledge_base.json',knowledge_base)
                print('Bot:Thankyou! I learned a new response')

if __name__=='__main__':
    chat_bot()



