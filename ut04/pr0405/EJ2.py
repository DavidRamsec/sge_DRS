celsius = [0, 20, 37, 100]
def celsius_far(grado):
    return (grado * 9 / 5) + 32
res = list(map(celsius_far, celsius))
print(res)