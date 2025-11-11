palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
def contar_letras(palabra):
    return len(palabra) > 5
largas = list(filter(contar_letras, palabras))
def a_mayus(word):
    return word.upper()
res = list(map(a_mayus, largas))
print(res)