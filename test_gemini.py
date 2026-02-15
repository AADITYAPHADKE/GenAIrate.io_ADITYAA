import google.generativeai as genai
from config import GEMINI_API_KEY

print("Testing Gemini API...")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-3-flash-preview")

response = model.generate_content(
    "Explain what a 1 million token context window means in 2 lines."
)

print("\nRESPONSE:\n")
print(response.text)
