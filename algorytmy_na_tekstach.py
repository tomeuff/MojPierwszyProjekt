def czy_palindrom(t):
    t = ''.join(t.split()).lower()
    return t == t[::-1]