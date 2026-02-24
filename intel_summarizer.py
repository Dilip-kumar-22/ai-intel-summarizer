import trafilatura
import requests
import json

# --- CONFIGURATION ---
# Note: This uses a free HuggingFace API inference point. 
# No API key is strictly needed for light testing, but recommended.
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

class IntelAgent:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    def scrape_content(self, url):
        """Extracts main body text from any URL."""
        print(f"[*] Intelligence Gathering: {url}...")
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            content = trafilatura.extract(downloaded)
            return content
        return None

    def summarize(self, text):
        """Sends text to LLM for executive summarization."""
        print("[*] Processing through Neural Layer...")
        # BART model has a limit, so we take the first 3000 chars
        payload = {"inputs": text[:3000], "parameters": {"do_sample": False}}
        
        try:
            response = requests.post(API_URL, headers=self.headers, json=payload)
            result = response.json()
            if isinstance(result, list):
                return result[0]['summary_text']
            return "Error: Could not process summary."
        except Exception as e:
            return f"Neural Failure: {e}"

if __name__ == "__main__":
    agent = IntelAgent()
    print("--- SILENT WHISPER: AI INTEL AGENT ---")
    target_url = input("Enter Target URL for Intel Extraction: ")
    
    raw_intel = agent.scrape_content(target_url)
    
    if raw_intel:
        summary = agent.summarize(raw_intel)
        print("\n" + "="*50)
        print("EXECUTIVE SUMMARY:")
        print("="*50)
        print(summary)
        print("="*50 + "\n")
    else:
        print("[!] Target unreachable or anti-scraping active.")
