from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

# app = FastAPI()

# Initialize the Google Generative AI model
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key="AIzaSyByjPb3Y_l-Of5nlZYEowZeHBME8uu3-vc"
)


template =