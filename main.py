import json
def build_prompt(car_data, matched_chunks):
    regulation_data = {chunk["field"]: chunk["expected"] for chunk in matched_chunks}
    regulations_list = [chunk["reason"] for chunk in matched_chunks]
    return f"""
You are Tata Compliance Assistant. Your job is to compare the car data with government regulations. Start the conversation with the user by greeting them and then provide the following information:

Respond strictly in this JSON format:

{{
  "status": "...",
  "regData": {{...}},
  "carData": {{...}},
  "issues": [{{...}}],
  "reason": "..."
}}

### CAR DATA:
{json.dumps(car_data, indent=2)}

### REGULATIONS TO COMPARE:
{json.dumps(regulation_data, indent=2)}

### EXPLANATIONS:
{json.dumps(regulations_list, indent=2)}
"""
