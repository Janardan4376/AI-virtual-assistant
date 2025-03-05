from google import genai
import user_config

client = genai.Client(api_key=user_config.openai_key)
def send_request(query):
     completion = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents= query
        )   
     print(completion.text)