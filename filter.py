keywords = []

with open('keywords.txt', "r", encoding='utf-8') as f:
    keywords = f.read().split()

def isMatch(entry):
    if any(words in entry for words in keywords):
        return True
    else:
        return False
