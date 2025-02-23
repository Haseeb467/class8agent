from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key="AIzaSyByjPb3Y_l-Of5nlZYEowZeHBME8uu3-vc"
)

# Escape all literal curly braces in the JSON schema by doubling them.
template = """
You are an AI-powered gym workout assistant designed to generate structured and personalized workout plans in JSON format.
You **must** follow these instructions:

1. **Call the onboarding function** at the start of the interaction: `provideOnboarding()`.
2. **Respond only in JSON format** and do not include any extra text.
3. **For general queries and statements** (greeting, soreness, diet, motivation, etc.), respond in the format:
   ```json
   {{
     "chat_gpt_message_response": "Your response text here."
   }}
Question: {question}
"""

# Create the prompt template with one input variable "question".
prompt = PromptTemplate(input_variables=["question"], template=template)

# Format the prompt by providing the question.
formatted_prompt = prompt.format(
    question="please give me the 2 days workout schedule in JSON form"
)

# Invoke the model with the formatted prompt.
result = llm.invoke(formatted_prompt)
print(result)
