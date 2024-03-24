from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('API_KEY'))

def get_content(title):
  prompt =f"""
  you are a content writer your task is to write a article on a topic which delimited
  by three backticks. article should be in 700 - 800 words And make sure it should look like
  human written Add necessary points and examples.
  Article Should be in HTML format

  topic name: ```{title}```
  """
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(prompt)
  print(str(response.text))
  return response.text

