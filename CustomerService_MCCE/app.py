import os
import openai
import sys
sys.path.append('..')
import utils
import utilsMCCE

# Import API Key
openai.api_key  = utils.get_OpenAI_API_Key()
# print(openai.api_key)

# Get Comments
# customer_comments = utils.generate_comment()
# print(customer_comments)

customer_comments = f"""The product range offered by this electronic company is impressive. 
They have a variety of options in different categories like computers, smartphones, televisions, 
gaming consoles, and audio equipment. The products have good ratings and come with warranties, which is reassuring. 
The features mentioned for each product are appealing, and the prices seem reasonable for the quality offered. Overall, 
I am impressed with the range and variety of products available, and I would definitely consider purchasing from this company.
"""
# Step 1: Moderation
print("Check for moderation:\n")
moderation_output=utilsMCCE.test_Moderation(customer_comments)
print(moderation_output)
    
# Step 2: Generate a Prompt Injection
