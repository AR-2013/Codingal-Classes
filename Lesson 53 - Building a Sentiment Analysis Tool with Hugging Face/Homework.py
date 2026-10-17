import requests, re, random
from config import HF_API_KEY

MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
API = f"https://router.huggingface.co/hf-inference/models/{MODEL}"
HEAD = {"Authorization": f"Bearer {HF_API_KEY}"}
TH = 0.72

TOK = lambda s: " | ".join(s.split())
bar = lambda s: "#" * int(s * 10) + "-" * (10 - int(s * 10))
clean = lambda t: [w for w in (re.sub(r"[^a-z0-9']+", "", x.lower())) for x in t.split() if w]

def analyze_sentiment(text):
    r = requests.post(API, headers=HEAD, json={"inputs": text}, timeout=30)
    if not r.ok: 
        raise RuntimeError(r.text)
    data = r.json()
    if isinstance(data, dict) and "error" in data: 
        raise RuntimeError(data["error"])
    
    preds = data[0] if isinstance(data, list) and isinstance(data[0], list) else data
    return sorted(preds, key=lambda x: x['score'], reverse=True)

def main():
    print("Hugging Face Sentiment Analyzer")
    print("Type 'exit' to quit.\n")
    
    while True:
        text = input("Enter text: ").strip()
        if text.lower() == 'exit': 
            break
        if not text: 
            continue
        
        try:
            results = analyze_sentiment(text)
            print("\nSentiment Breakdown:")
            for p in results:
                lbl = p['label'].upper()
                scr = p['score']
                print(f"  {lbl:8} | {bar(scr)} {scr*100:.1f}%")
            print("-" * 35)
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()