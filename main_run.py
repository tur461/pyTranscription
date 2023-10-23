import os
import base64 as b64
import openai as OAI
from flask_cors import CORS
from dotenv import load_dotenv
from os.path import join, dirname
from flask import Flask, jsonify, request

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

OAI.api_key = os.environ.get('OPEN_API_KEY')

# print('models')
# l = OAI.Model.list()
# print(l.values())

def generate_response_from_transcript(transcript):
    try:
        response = OAI.ChatCompletion.create(
                model="gpt-3.5-turbo-0301",
                messages=[{"role": "system", "content": transcript}],
                temperature = 0.0
        )
        print('response: ', response)
    except Exception as e:
        print('chat gpt error!!')
        print(e)
        return ''
    full_response = response.choices[0].message.content
    try:
        return full_response#.split('[')[1].split(']')[0]
    except:
        return ''

flask_app = Flask(__name__)

cors = CORS(flask_app, resources={r"/*": {"origins": "*"}})

@flask_app.route('/')
def home():
    return 'Welcome to Audio Transcribed Replier - ATR', 200

@flask_app.route('/resolve', methods=['POST'])
def resolveWithGPT():
    params = request.get_json()
    print('params:', params)
    query = params['query']
    resBytes = generate_response_from_transcript(query).encode('ascii')
    encoded = b64.b64encode(resBytes)
    response = jsonify({
        'reply': encoded.decode('ascii')
    })
    return response, 200

