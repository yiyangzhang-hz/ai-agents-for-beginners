import requests

def ask_ollama(model: str, prompt: str) -> str:
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }
    try:
        resp = requests.post(url, json=payload, timeout=300)
        resp.raise_for_status()
        data = resp.json()
        # Ollama /api/chat 返回结构：{"message": {"role": "...","content": "..."} , ...}
        return data.get("message", {}).get("content", "").strip()
    except Exception as e:
        return f"[Error] {e}"

if __name__ == "__main__":
    model_name = "qwen2.5:1.5b"
    question = "人生的意义是什么"
    answer = ask_ollama(model_name, question)
    print("Q:", question)
    print("A:", answer)
