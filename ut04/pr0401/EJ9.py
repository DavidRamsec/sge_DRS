num = int(input("Escribe cuantos numeros de la secuencia de Fibonacci quieres generar: "))
a = 0
b = 1
secuencia = []
for i in range(num):
    secuencia.append(a)
    a, b = b, a + b
print("Secuencia: ",secuencia)