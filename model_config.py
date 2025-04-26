from pydantic import BaseModel, Field
from google import genai
from dotenv import load_dotenv
import os


# Define response schema
class story_generater(BaseModel):
    story: str = Field(description="in markdown format")


#define the model parameters
def model_params():
    temperature = 0.7
    response_mime_type = 'application/json'
    model_name = 'gemini-2.0-flash'

    return temperature,response_mime_type,model_name

#load the api key and intialize the model
def initialize_model():
    #load environment variables
    load_dotenv(dotenv_path=".env")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY environment variable not set. Please check your .env file.")


    #initialize gemini client
    gemini = genai.Client(api_key=GEMINI_API_KEY)

    return gemini