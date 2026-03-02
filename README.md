# 🧠 Truth Lens — AI Fact Checker

**AI-powered real-time fact-checking agent** that uses web search, credibility-weighted source analysis, contradiction detection, and LLM reasoning to verify claims and generate structured verdicts with timelines.

---

## 🚀 Overview

Truth Lens is designed to help users **discern truth from misinformation** by analyzing a claim or news text and returning:

✔ Verdict (Fake / Real / Misleading)  
✔ Source credibility score  
✔ Contradiction detection  
✔ Timeline evidence summary  
✔ Structured explanations

Its reasoning is powered by a blend of real-time web retrieval, credibility weighting, and large-language-model reasoning.

---

## 🧩 Key Features

- 🔎 **Real-time search & retrieval** — Fetches context from multiple sources.
- 📊 **Credibility scoring** — Weights sources by reliability.
- 🧠 **LLM-powered reasoning** — Generates structured, explainable output.
- 🔄 **Contradiction detection** — Spots conflicts across sources.
- 📆 **Timeline generation** — Shows chronological evidence progression.
- 🗣️ **Modular and extensible** — Easy to plug into other apps or UIs.

---

## 🧰 Tech Stack

| Component | Purpose |
|----------|---------|
| Python | Core language |
| LLMs | Reasoning & explanations |
| Web Search APIs | Evidence retrieval |
| Custom scoring | Credibility & contradiction analysis |

---

## ⚙️ Installation

1. Clone the repo:

```bash
git clone https://github.com/aryamansingh04/Truth-Lens-Fact-Checker.git
cd Truth-Lens-Fact-Checker

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

export SEARCH_API_KEY="your_api_key_here"
export OPENAI_API_KEY="your_openai_api_key"
