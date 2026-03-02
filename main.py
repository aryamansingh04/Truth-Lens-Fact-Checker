import os
from dotenv import load_dotenv
from groq import Groq

from searcher import search_web
from scorer import compute_credibility, classify_source

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# -------- Detect Query Type --------
def detect_query_type(query):
    query = query.lower()

    if any(word in query for word in ["who", "what", "when", "president", "capital", "ceo"]):
        return "fact"

    if any(word in query for word in ["did", "attack", "join", "happen", "strike", "war"]):
        return "event"

    return "general"


# -------- Entity Extraction --------
def extract_entities(query):
    prompt = f"""
Extract the main entities from this claim.
Return only a comma-separated list.

Claim: {query}
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return completion.choices[0].message.content.strip()


# -------- LLM Analysis --------
def analyze_claim(query, search_results, credibility_score):

    combined = "\n\n".join(
        [f"{r['title']} - {r['body']} (Source: {r['href']})"
         for r in search_results[:6]]
    )

    prompt = f"""
You are an advanced real-time fact-checking AI.

User Claim:
{query}

Overall Source Credibility Score (0 to 1):
{credibility_score}

Web Evidence:
{combined}

Tasks:
1. Decide clearly: TRUE, FALSE, or UNCERTAIN.
2. Explain reasoning using evidence.
3. Identify contradictions if present.
4. If event-based, generate a chronological timeline.
5. Mention how credibility score impacts confidence.
6. Provide structured sections.
7. Do NOT mention knowledge cutoff.
Be confident and structured.
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return completion.choices[0].message.content


# -------- Main Pipeline --------
def run(query):

    print("\nDetecting query type...")
    query_type = detect_query_type(query)
    print(f"Query Type: {query_type}")

    print("Extracting entities...")
    entities = extract_entities(query)
    print(f"Entities detected: {entities}")

    print("\nSearching the web...")
    search_results = search_web(query)

    if not search_results:
        print("No web results found.")
        return

    print("Computing source credibility...")
    credibility_score = compute_credibility(search_results)
    print(f"Overall Credibility Score: {credibility_score}")

    print("\nAnalyzing claim with LLM...\n")
    result = analyze_claim(query, search_results, credibility_score)

    print("============== FINAL RESULT ==============\n")
    print(result)

    print("\n============== SOURCE ANALYSIS ==============\n")

    for i, r in enumerate(search_results[:6], 1):
        category, score = classify_source(r["href"])

        print(f"{i}. {r['title']}")
        print(f"   URL: {r['href']}")
        print(f"   Category: {category}")
        print(f"   Reliability Score: {score}\n")

    print(f"\nFinal Aggregated Credibility Score: {credibility_score}")


if __name__ == "__main__":
    user_query = input("Enter claim to fact-check: ")
    run(user_query)