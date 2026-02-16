import google.generativeai as genai
from config import GEMINI_API_KEY

print("Sending extracted email to Gemini...\n")

# configure gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-3-flash-preview")

# path of extracted txt file
file_path = "EX1_output.txt"


# read file
with open(file_path, "r", encoding="utf-8") as f:
    email_text = f.read()

print("File loaded. Sending to Gemini...\n")

# send to gemini
response = model.generate_content(
    f"""
You are an insurance document analysis assistant.

From the following email/document text, extract these fields clearly.

Return output in structured format:

Property Damage:
Business Interruption:
Total Insured Value:
Deductibles:
Sublimits:
Address of Location(s):
Claims (if any):

If any field is missing, write: Not found.

Document text:
{email_text[:30000]}
"""
)


print("GEMINI RESPONSE:\n")
print(response.text)

# save response to file
with open("gemini_output.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("\nOutput also saved to gemini_output.txt")
