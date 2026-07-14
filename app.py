import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.utils import fetch_doc_contents

load_dotenv(override=True)

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini_api_key = os.getenv("GOOGLE_API_KEY")

gemini = OpenAI(base_url=BASE_URL, api_key=gemini_api_key)

SYSTEM_PROMPT = (
    "You are a helpful assistant that can help with tasks related to the web. "
    "Your task is to carefullly analyze the given content, give an overall summary, "
    "enpoints to be used, methods to be used, and other relevant information."
    "Return the response in a structured format."
    
)
USER_PROMPT = "Please analyze the following"

url = "https://pypi.org/project/beautifulsoup4/"
contents = fetch_doc_contents(url)


def messages_for(website, url):
    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": USER_PROMPT.format(contents=website) + " website: " + url
        }
    ]


def summarize(url):
    website = fetch_doc_contents(url)
    response = gemini.chat.completions.create(
        model="gemini-3.1-flash-lite",
        messages=messages_for(website, url)
    )
    return response.choices[0].message.content

print(summarize(url))
