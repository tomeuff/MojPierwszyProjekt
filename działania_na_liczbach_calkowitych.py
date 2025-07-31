def NWD_lista(lst):
    if not lst:
        return None
    wynik = abs(lst[0])
    for liczba in lst[1:]:
        a, b = abs(wynik), abs(liczba)
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        wynik = a
    return wynik
    
def NWW_lista(lst):
    if not lst:
        return None
    wynik = abs(lst[0])
    for liczba in lst[1:]:
        a, b = abs(wynik), abs(liczba)
        x, y = a, b
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        nwd = a
        wynik = (x * y) // nwd
    return wynik