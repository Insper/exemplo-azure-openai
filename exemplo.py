import os

from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_VERSION = os.getenv('API_VERSION')
AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT')
DEPLOYMENT_NAME = os.getenv('DEPLOYMENT_NAME')

client = AzureOpenAI(
    api_key=API_KEY,
    api_version=API_VERSION,
    azure_endpoint=AZURE_ENDPOINT,
)

completion = client.chat.completions.create(
    model=DEPLOYMENT_NAME,
    messages=[
        {
          "role": "system",
          "content": "Você conhece o Insper?."
        }
    ]
)

answer = completion.choices[0].message.content
print(answer)
