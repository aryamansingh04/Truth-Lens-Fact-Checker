def classify_source(url):
    url = url.lower()

    HIGH = [
        "reuters", "bbc", "apnews", "associatedpress", "whitehouse.gov",
        "gov", "nasa.gov", "who.int", "un.org", "nature.com",
        "science.org", "theguardian.com", "wsj.com",
        "economist.com", "bloomberg.com", "ft.com",
        "nbcnews.com", "cbsnews.com", "abcnews.go.com",
        "aljazeera.com", "dw.com", "npr.org"
    ]

    MEDIUM = [
        "cnn.com", "nytimes.com", "washingtonpost.com",
        "forbes.com", "time.com", "newsweek.com",
        "usatoday.com", "independent.co.uk",
        "hindustantimes.com", "thehindu.com",
        "indiatimes.com", "businessinsider.com",
        "verge.com", "techcrunch.com"
    ]

    LOW = [
        "twitter.com", "instagram.com", "tiktok.com",
        "reddit.com", "quora.com", "medium.com",
        "blogspot", "wordpress", "facebook.com",
        "youtube.com"
    ]

    if any(x in url for x in HIGH):
        return "Highly Reliable", 0.9

    if any(x in url for x in MEDIUM):
        return "Moderately Reliable", 0.7

    if any(x in url for x in LOW):
        return "Low Reliability", 0.3

    return "Unknown Reliability", 0.5


def compute_credibility(search_results):
    if not search_results:
        return 0

    total_score = 0

    for result in search_results:
        _, score = classify_source(result["href"])
        total_score += score

    return round(total_score / len(search_results), 2)