from rag_utils import load_and_embed_regulations, retrieve_similar_chunks
from main import build_prompt
from gemini_config import call_gemini
import json

# Load car data
with open("input\sample_car_data.json") as f:
    car_data = json.load(f)

# Embed and retrieve matching rules
data, index, _ = load_and_embed_regulations("data\gov_regulation.jsonl")
matched = retrieve_similar_chunks(json.dumps(car_data), data, index)

# Create prompt and query Gemini
prompt = build_prompt(car_data, matched)
gemini_response = call_gemini(prompt)

# Save result
with open("output\output.json", "w") as f:
    f.write(gemini_response)
