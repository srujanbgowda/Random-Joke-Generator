import random

def get_random_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why don't scientists trust atoms? Because they make up everything.",
        "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
        "Why did the math book look sad? Because it had too many problems."
    ]
    return random.choice(jokes)

# Main
if __name__ == "__main__":
    input("Press Enter to get a random joke...")
    print(get_random_joke())