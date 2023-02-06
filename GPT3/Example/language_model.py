import os
import openai
import argparse
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', type=str, required=True)
parser.add_argument('-n', '--max-token', type=int, default=30)
args = parser.parse_args()

load_dotenv('.env')

openai.api_key = os.getenv('API_KEY')
openai.api_base = os.getenv('API_BASE')
openai.api_type = os.getenv('API_TYPE')
openai.api_version = os.getenv('API_VERSION')

# This will correspond to the custom name you chose for your deployment when you deployed a model.
deployment_id = os.getenv('DEPLOYMENT_ID')

# Send a completion call to generate an answer
start_phrase = args.text
response = openai.Completion.create(
    engine=deployment_id, prompt=start_phrase, max_tokens=args.max_token)
text = response['choices'][0]['text'].replace(' .', '.').strip()
# text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print(start_phrase + '\n' + text)
