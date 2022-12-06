import openai
import os 
from api_key import api_key


openai.api_key = api_key
def quote(prompt='what is prompt'):
    response = openai.Completion.create(engine='text-babbage-001',prompt=prompt,temperature=0.4,max_tokens=999)
    response = response.get('choices')
    response = response[0].get('text')
    return response
    print(response.replace('\n\n' , "-: "))
     