with open('fajl.txt', 'a+', encoding='utf-8') as celfalj:
    celfalj.seek(0)
    print(celfalj.readline())
    print(celfalj.tell())
    print('Ez kerül mentésre!!!', file=celfalj)