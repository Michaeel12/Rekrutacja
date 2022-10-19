sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

Słowa ={}

for i in sentences:

   k=i.split(' ')

   for s in range(len(k)):
       k[s]=k[s].lower()
       if k[s] in Słowa.keys():
            Słowa[k[s]]+=1

       else:
           Słowa.setdefault(k[s])
           Słowa[k[s]] = 1

l=sorted(Słowa.items(), key=lambda x: x[1], reverse=True)

print(l[:3])



