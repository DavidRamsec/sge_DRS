num = 2
while (num%2==0):
    num = int(input("Introduce un numero: "))
i = 1
e = int((num-1)/2)
for i in range(1,num+1,2):
    print(" "*e,"*"*i)
    e = e-1