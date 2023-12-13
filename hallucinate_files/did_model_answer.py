def check_keywords(response, keywords):
    answer = False
    for keyword in keywords:
        if keyword["position"] == "beginning":
            if response.startswith(keyword["keyword"]):
                answer = True
                break
        elif keyword["position"] == "anywhere":
            if keyword["keyword"] in response: 
                answer = True
                break
    return answer

def did_model_equivocate(response):
    did_model_equivocate = False
    KEYWORDS = [
    {"keyword": "I'm sorry", "position": "beginning"},
    {"keyword": "I am sorry", "position": "beginning"},
    {"keyword": "Sorry,", "position": "beginning"},
    {"keyword": "I cannot fulfill your request", "position": "beginning"},
    {"keyword": "I apologize", "position": "beginning"},
    {"keyword": "I cannot", "position": "beginning"},
    {"keyword": "I will not", "position": "beginning"},
    {"keyword": "language model", "position": "anywhere"},
    ]
    return check_keywords(response, KEYWORDS)

def did_model_break_char(response, name):
    KEYWORDS = [
        {"keyword": "in the description", "position": "anywhere"},
        {"keyword": "As " + name, "position": "anywhere"},
        {"keyword": "As a character", "position": "anywhere"},
    ]
    return check_keywords(response, KEYWORDS)
