import google.generativeai as genai

def call_gemini(prompt):
    genai.configure(api_key="YOUR API KEY")
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
