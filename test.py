import requests
import time

API_URL = "https://us-central1-dauntless-loop-285816.cloudfunctions.net/f"
key=_

def query(**payload):
    response = requests.post(API_URL,  json=payload)
    print(response)
    return response.json()


query(action='start',key=key)
print('server starting in 40s...')
time.sleep(40)

output=query(q='me no pueder hablars bueno espanio',action='correct',lang='es',key=key)
print(output)
# {'old': 'me no pueder hablars bueno espanio', 'new': 'No puedo hablar bien español.', 'corrections': [{'start': 0, 'end': 20, 'old': 'me no pueder hablars', 'new': 'No puedo'}, {'start': 21, 'end': 34, 'old': 'bueno espanio', 'new': 'hablar bien español.'}]}

output=query(q='me wanna talk english good',action='correct',lang='en',key=key)
print(output)
# {'old': 'me wanna talk english good', 'new': 'I want to speak English well.', 'corrections': [{'start': 0, 'end': 13, 'old': 'me wanna talk', 'new': 'I want to speak'}, {'start': 14, 'end': 21, 'old': 'english', 'new': 'English'}, {'start': 22, 'end': 26, 'old': 'good', 'new': 'well.'}]}

