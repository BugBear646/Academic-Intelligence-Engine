SCORING_RULES = {

    "product management": 10,
    "platform strategy": 10,
    "innovation": 8,
    "consumer behavior": 9,
    "behavioral economics": 9,
    "decision science": 7,
    "human computer interaction": 8,
    "information systems": 8,
    "digital transformation": 7,
    "enterprise systems": 7,
    "artificial intelligence": 6,
    "ai": 7,
    "saas": 7,
    "strategy": 8,
    "platform ecosystems": 8
}

def calculate_score(text):

    text = text.lower()

    score = 0

    for keyword, value in SCORING_RULES.items():

        if keyword in text:
            score += value

    return score