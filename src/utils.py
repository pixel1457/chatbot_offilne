import requests
import json

def call_ollama_model(model, prompt, stream=False):
    url = f"http://localhost:11434/api/generate"

    parameters = {
        "model": model,
        "prompt": prompt,
        "stream": stream
}
    playload = json.dumps(parameters)
    response = requests.post(url, data=playload, headers={"Content-Type": "application/json"})

    if response.status_code != 200:
        return 'Error: '
    else:
        response = response.json()['response']
        return response

if __name__ == "__main__":
    prompt = input("Ask your question: ")
    model = "qwen2.5-coder:7b"
    response = call_ollama_model(model, prompt)
    print('result',response)

