from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key="AIzaSyByjPb3Y_l-Of5nlZYEowZeHBME8uu3-vc"
)

# Escape all literal curly braces in the JSON schema by doubling them.
template = """

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
