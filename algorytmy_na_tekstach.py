def czy_palindrom(t):
    t = ''.join(t.split()).lower()
    return t == t[::-1]
    
def czy_anagramy(a, b):
    return sorted(a.lower()) == sorted(b.lower())
    
def naiwne_wyszukiwanie(tekst, wzorzec):
    for i in range(len(tekst) - len(wzorzec) + 1):
        if tekst[i:i+len(wzorzec)] == wzorzec:
            return i
    return -1