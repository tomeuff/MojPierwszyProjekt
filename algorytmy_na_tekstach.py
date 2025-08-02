def czy_palindrom(t):
    t = ''.join(t.split()).lower()
    return t == t[::-1]
    
def czy_anagramy(a, b):
    return sorted(a.lower()) == sorted(b.lower())