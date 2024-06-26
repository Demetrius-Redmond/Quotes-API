import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def quote_by_category(category: str):
    configure()
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': os.getenv("api_key")})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

quote_by_category("inspirational")
