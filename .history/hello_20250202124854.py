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

   {{
  "application_uuid": "getApplicationUUID()",
  "chat_gpt_message_response": "A motivational intro for today's workout.",
  "workout_description": "Detailed workout overview, focusing on strength, endurance, or fat loss.",
  "workout_short_description": "A concise summary of the workout.",
  "exercise_array": [
    {{
      "date": "getCurrentDate()",
      "title": "Day 1 - Warm-Up: Jump Rope",
      "description": "Jump rope at a moderate pace to elevate your heart rate.",
      "workout_uuid": "getWorkoutUUID()",
      "exercise_number": 1,
      "video_link": "getExercise('Jump Rope Basic Jump White Screen')",
      "exercise_name": "Jump Rope Basic Jump",
      "reps": "3 minutes",
      "sets": 1,
      "weight": "Bodyweight",
      "weight_format": "N/A"
    }},
    {{
      "date": "getCurrentDate()",
      "title": "Day 1 - Strength: Barbell Deadlift",
      "description": "Perform a controlled deadlift to build lower body strength.",
      "workout_uuid": "getWorkoutUUID()",
      "exercise_number": 2,
      "video_link": "getExercise('Barbell Deadlift 360 Degrees')",
      "exercise_name": "Barbell Deadlift",
      "reps": 8,
      "sets": 4,
      "weight": "225",
      "weight_format": "Lbs"
    }}
  ],
  "user_uuid": "getUserUUID()",
  "application_name": "Trainr",
  "motivational_closing": "Great job! Tomorrow, we'll focus on core endurance."
}}



---

### **Key Improvements:**
✅ **Ensures structured JSON output** with the correct schema.  
✅ **Calls onboarding function** as per the requirements.  
✅ **Includes personalization** (fitness level, goals, past feedback).  
✅ **Uses valid exercises** and fetches exercise videos.  
✅ **Automatically includes a motivational closing**.  
✅ **Supports multiple workout days** (`Day 1, Day 2, etc.`).  

This will ensure that your AI gym trainer consistently generates high-quality, structured, and useful workout plans. 🚀 Let me know if you need any tweaks!


Question: {question}
"""

# Create the prompt template with one input variable "question".
prompt = PromptTemplate(input_variables=["question"], template=template)

# Format the prompt by providing the question.
formatted_prompt = prompt.format(
    question="i am perform 2 days "
    # question="please give me the 2 days workout schedule in JSON form"
)

# Invoke the model with the formatted prompt.
result = llm.invoke(formatted_prompt)
print(result)
