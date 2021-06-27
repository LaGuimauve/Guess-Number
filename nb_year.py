def nb_year(p0, percent, aug, p):
    more = p0
    year = 0
    pourcent = percent / 100
    while more < p:
        more = more + more * pourcent + aug
        year += 1
    return print(year)
