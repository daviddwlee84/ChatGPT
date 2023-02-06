import os
import openai
import argparse
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', type=str, required=True)
parser.add_argument('-n', '--max-token', type=int, default=30)
parser.add_argument('-s', '--type', type=str,
                    choices=['zero-shot', 'one-shot', 'few-shot'], default='few-shot')
args = parser.parse_args()

load_dotenv('.env')

openai.api_key = os.getenv('API_KEY')
openai.api_base = os.getenv('API_BASE')
openai.api_type = os.getenv('API_TYPE')
openai.api_version = os.getenv('API_VERSION')

# This will correspond to the custom name you chose for your deployment when you deployed a model.
deployment_id = os.getenv('DEPLOYMENT_ID')

# Send a completion call to generate an answer
start_phrase = 'Calculate:'

if args.type in ['one-shot', 'few-shot']:
    start_phrase += '\n1 + 2 = 3'

if args.type in ['few-shot']:
    start_phrase += '\n3 * 8 = 24'
    start_phrase += '\n5 / 2 = 2.5'
    start_phrase += '\n100 - 96 = 4'

start_phrase += f'\n{args.text} ='

response = openai.Completion.create(
    engine=deployment_id, prompt=start_phrase, max_tokens=args.max_token)
text = response['choices'][0]['text'].replace(
    '\n', '').replace(' .', '.').strip()
print('Prompt:')
print(start_phrase)

print('\nInput:', args.text)

print('\nResult:', text)
