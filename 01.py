with open('fajl.txt', 'a+', encoding='utf-8') as forrasfajl, \
    open('fajl_masolat.txt', 'w', encoding='utf-8') as celfajl:
    for sor in forrasfajl:
        print(sor.strip(), file=celfajl)