API Token : GBMThx4M0xgJkrMUN9XppJIJKj76j_VwkkguTTyG

curl "https://api.cloudflare.com/client/v4/user/tokens/verify" \
  -H "Authorization: Bearer GBMThx4M0xgJkrMUN9XppJIJKj76j_VwkkguTTyG"

curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/meta/llama-3.1-8b-instruct \
  -H 'Authorization: Bearer {API_TOKEN}' \
  -d '{ "prompt": "Where did the phrase Hello World come from" }'

https://developers.cloudflare.com/workers-ai/models/

For embedding use : https://developers.cloudflare.com/workers-ai/models/bge-large-en-v1.5/ (Text Embedding) : @cf/baai/bge-large-en-v1.5
For Text generation : Below "@cf/meta/llama-3-8b-instruct" is good enough for now

Python : 

import requests

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/f3dc4c67a58799cf5b8042e17747d876/ai/run/"
headers = {"Authorization": "Bearer {API_TOKEN}"}

def run(model, inputs):
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

inputs = [
    { "role": "system", "content": "You are a friendly assistan that helps write stories" },
    { "role": "user", "content": "Write a short story about a llama that goes on a journey to find an orange cloud "}
];
output = run("@cf/meta/llama-3-8b-instruct", inputs)
print(output)