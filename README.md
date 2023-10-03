# Customer Support System: An email to the customer
[Google Slides](https://docs.google.com/presentation/d/1aqFh4tzRhZ6w0nnEgkv_dZDaY8N0wDEi5jTru9reDCQ/edit?usp=sharing)

## Project Settings
1. You're a customer service assistant for a large electronics store
2. The website of the store allows the customers to select language.
3. The store's products
    * Belong to different categories
    * Each product has detailed description
4. Desired interface:
![Screenshot 2023-10-02 114221](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/0eb7af5f-297e-40d9-9874-ed4f435d6c45)


## Project Sections Step by Step
### Step 1: Generate a customer's comment
![image](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/6f7713a9-3ae1-4637-aa10-ff49d00b6086)

### Step 2: Generate email subject
![image](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/973cdcec-7f00-48cf-baae-46580ce6a521)

### Step 3: Generate the summary of the customer's comment
![image](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/f67c9ff7-7081-430d-9580-14f6e4105b9b)

### Step 4: Sentiment analysis of the customer's comment
![image](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/887c0081-7d92-4caf-aca2-fe129ef773ff)

### Step 5: Generate an email to be sent to the customer.
![image](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/b31b5ec4-3b2e-4219-8873-5c6513082826)

## Project Implementation Tips

### 1. Step by Step
Follow the steps, achieve the results one by one

### 2.Simple Code
Write simple code blocks for each steps

### 3. Playground
Use OpenAI playground to pre-test the result of the model get back. https://platform.openai.com/playground 
![image](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/05392253-b9c4-4905-88b9-8f9e46f195de)

### 4. Combine the Blocks
Combine the chain of code together and test result.

### 5. Convert Code to Project
Use Flask framework to convert the code into web based application.

### 6. Use ChatGPT
Use ChatGPT to fine tune the project to look better.

<br>
## Test Cases

### **To run the project: $ python3 app.py**

![image](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/1e4bf04f-3596-46a7-8905-b69f388fc8bd)

### English <-> English
![Screenshot 2023-10-02 132246](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/70cd4c58-aa89-48c4-9976-d079e7b17c8f)

### English <-> Non-English
![Screenshot 2023-10-02 132522](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/c907bf2b-1baf-44c9-b44a-8be65ba529fb)

### Non-English <-> English
![Screenshot 2023-10-02 132349](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/1094cd76-16d1-45ae-9d02-bd269852dc26)

### Non-English <-> Non-English
![Screenshot 2023-10-02 132712](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/adec3c64-1c8c-4bb6-827e-ba7a5c737e31)

### In terminal

![Screenshot 2023-10-02 024741](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/cb127fbc-59c3-47e7-a887-d5e3c968e79d)

![Screenshot 2023-10-02 024756](https://github.com/SharonCao0920/emailToCustomer_OpenAI/assets/54694766/3a5e3de8-21d8-4a20-9afe-d3c37a3c82f9)

