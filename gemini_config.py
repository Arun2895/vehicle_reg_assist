import google.generativeai as genai

def call_gemini(prompt):
    genai.configure(api_key="AIzaSyAI2nDMfacvid9A9LBDRZjAojSdm72nGUM")
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text
