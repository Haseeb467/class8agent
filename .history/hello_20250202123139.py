from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key="AIzaSyByjPb3Y_l-Of5nlZYEowZeHBME8uu3-vc"
)

# Escape all literal curly braces in the JSON schema by doubling them.
template = """You are a helpful assistant that generates detailed workout plans in valid JSON format.
Please provide a 7-day workout plan that follows the JSON schema exactly as shown below.
Do not include any additional commentary or text outside the JSON.

Workout Response JSON Format:
{{
  "application_uuid": "getApplicationUUID()",
  "chat_gpt_message_response": "A brief message summarizing the workout plan",
  "workout_description": "A detailed description of today's workout including exercises and their benefits",
  "workout_short_description": "A short summary of the workout",
  "exercise_array": [
    {{
      "date": "display current date",
      "title": "Title of the exercise",
      "description": "Description of the exercise",
      "workout_uuid": "getWorkoutUUID()",
      "exercise_number": 1,
      "video_link": "getExercise('Title of the exercise')",
      "exercise_name": "Name of the exercise",
      "reps": "Repetition information",
      "sets": "Number of sets",
      "weight": "Weight information or 'Bodyweight'",
      "weight_format": "e.g., 'Lbs' or 'N/A'"
    }}
    // ... repeat for each exercise in the 1 day's workout
  ],
  "user_uuid": "getUserUUID()",
  "application_name": "Trainr",
  "motivational_closing": "A closing motivational message"
}}

Using the above schema, please generate a 7-day workout plan.
Question: {question}
"""

# Create the prompt template with one input variable "question".
prompt = PromptTemplate(input_variables=["question"], template=template)

# Format the prompt by providing the question.
formatted_prompt = prompt.format(
    question="please give me the 7 days workout schedule in JSON form"
)

# Invoke the model with the formatted prompt.
result = llm.invoke(formatted_prompt)
print(result)
