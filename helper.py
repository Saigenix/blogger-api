from dotenv import load_dotenv

load_dotenv()
import google.generativeai as genai
import os
import ast

genai.configure(api_key=os.getenv("API_KEY"))


def get_titles(title):
    prompt = f"""You are a content manager your job is to provide a list of titles for article, title should be of 3-4 words and attractive
  provide in this format ['title1', 'title2', 'title3',...] related to topic which is delimited by three backticks
   ```{title}```
  """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    print(response.text)
    if response.text[0] == "[":
      title_list = ast.literal_eval(response.text)
      # print(title_list[0])
      return title_list
    else:
      get_titles(title)


# list = get_titles("computer science")
