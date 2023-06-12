import json
import requests
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
  
# TODO: define
prompt = ""

data = query(prompt)
