# Silent Whisper: AI Web Intel Agent 🕵️

An automated intelligence gathering tool that extracts core content from web sources and generates executive summaries using Transformer-based NLP models.

## ⚡ Features
* **High-Fidelity Extraction:** Utilizes `trafilatura` to bypass ads, sidebars, and trackers to get raw body text.
* **Neural Summarization:** Integrated with the **BART (Large CNN)** model to condense long articles into actionable intel.
* **Contextual Truncation:** Automatically handles token limits for efficient LLM processing.

## 🛠️ Technology Stack
* **Scraping Engine:** Trafilatura
* **AI Model:** facebook/bart-large-cnn (via HuggingFace API)
* **Language:** Python 3.12

## 🚀 Usage
1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Activate the Agent:**
    ```bash
    python intel_summarizer.py
    ```
3.  **Input:** Provide any article URL (e.g., TechCrunch, Bloomberg, or a research paper) to receive a condensed summary.
