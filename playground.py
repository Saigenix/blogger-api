from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('API_KEY'))

def get_content(title):
  prompt =f"""You are a content manager your job is to provide a list of titles for article, title should be of 3-4 words and attractive
  provide in a json format topic,titles related to topic which is delimited by three backticks
   ```{title}```
  """
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(prompt)
  print(response.text)
  return response.text


list = get_content("computer science")