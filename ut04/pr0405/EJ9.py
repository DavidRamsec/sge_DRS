palabras = ["sol", "luna", "estrella", "cielo", "mar"]
longitudes = set(map(lambda pal: len(pal), palabras))
res = {str(l):list(filter(lambda s: len(s)==l, palabras)) for l in longitudes }
print(res)