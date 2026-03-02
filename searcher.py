from ddgs import DDGS

def search_web(query, max_results=8):
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "body": r.get("body", ""),
                "href": r.get("href", "")
            })

    return results