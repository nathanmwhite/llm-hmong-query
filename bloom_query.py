import json
import requests

from .util import prompt_prefix, words

API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}",
           "Content-Type": "application/json"}
def query(text):
    payload = {"inputs": text,
           "parameters": {"max_new_tokens": 32,
                          "return_full_text": False},
           "options": {"use_cache": False, "wait_for_model": True}}
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
  
def loop_words():
    results = []
    for w in words.keys():
        data = query(prompt_prefix + w + " - ")
        results.append((w, data))
    return results
