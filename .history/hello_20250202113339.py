from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

# app = FastAPI()

# Initialize the Google Generative AI model
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash", google_api_key="AIzaSyByjPb3Y_l-Of5nlZYEowZeHBME8uu3-vc"
)


template = """ 
You are a helpful assistant that generates detailed workout plans in valid JSON format.
Please provide a 7-day workout plan that follows the JSON schema exactly as shown below.
Do not include any additional commentary or text outside the JSON.

Workout Response JSON Format:
{
  "application_uuid": "getApplicationUUID()",
  "chat_gpt_message_response": "A brief message summarizing the workout plan",
  "workout_description": "A detailed description of today's workout including exercises and their benefits",
  "workout_short_description": "A short summary of the workout",
  "exercise_array": [
    {
      "date": "getCurrentDate()",
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
    }
    // ... repeat for each exercise in the day's workout
  ],
  "user_uuid": "getUserUUID()",
  "application_name": "Trainr",
  "motivational_closing": "A closing motivational message"
}

Using the above schema, please generate a 7-day or 1-day  workout plan.
"""

prompt = PromptTemplate(input_variables=["question"], template=template)

formatted_prompt = prompt.format(question="""please give me the 7 days workout schedule in jason form """)
result = llm.invoke(formatted_prompt)
print(result)
