import json
from flask import Flask, request, jsonify
from google.genai import types
from prompt import SYSTEM_PROMPT
from model_config import *


#initializing the model
gemini = initialize_model()

#loading the model params
temperature,response_mime_type,model_name = model_params()

#initialize app
app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route("/StoryGenerator", methods=["POST"])
def generate_story():
        
        message = request.json.get("message")
        response = gemini.models.generate_content(
            model = model_name,
            contents = message,
            config = types.GenerateContentConfig(
                system_instruction = SYSTEM_PROMPT,
                temperature = temperature,
                response_mime_type = response_mime_type,
                response_schema = story_generater
            )
        )
        
        response_data = response.text.strip("```json").strip("```").strip()
        
        try:
            response_json = json.loads(response_data)
        except json.JSONDecodeError:
            app.logger.error(f"Failed to parse response: {response_data}")
            response_json = {"story": response_data}
        
        return jsonify(response_json)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)