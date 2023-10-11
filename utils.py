import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
import products

delimiter="####"

def get_OpenAI_API_Key():
    return os.getenv("OPENAI_API_KEY")

# General function to get response with gpt-3.5
def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=1000):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]

# Generate customer prompt
def generate_comment():
    system_message_comment=f"""
    Product details can be found as below
    Assume that you are a customer to an electronic product company.
    Products information delimited by tripe backticks in its own language. 
    Products: ```{products.products_data}```
    """
    
    user_message_comment=f"""
    A less than 100 words comment about the products"""

    messages_comment =  [  
    {'role':'system', 
    'content': system_message_comment},    
    {'role':'user', 
    'content': f"{delimiter}{user_message_comment}{delimiter}"},  
    {'role':'assistant',
    'content':'talk as a customer'}
    ] 
    comment = get_completion_from_messages(messages_comment)
    print("Comment from customers: ")
    print(comment+"\n")
    return comment