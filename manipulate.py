import string
def capitalize_words(s):
    x = s.capitalize()
    return x

def reverse_string(s):
    x = s[::-1]
    return x

def remove_punctuation(s):
    news = ""
    for char in s:
        if char not in string.punctuation:
            news += char
    return news
