#Programa para verificar que número es mayor

print("-------------------------------------")
print("---------------Tarea-----------------")
print("-------------------------------------")

#Imput
a=int(input("Digite un número entero: "))
b=int(input("Digite otro número entero: "))

#Processing y output
if a==b:
    print(str(a) + " es igual " + str(b))
else:
    if a>b:
        print("-------------------------------------")
        print(str(a) + " es mayor que " + str(b))
        print("-------------------------------------")
    else:
        print("-------------------------------------")
        print(str(b) + " es mayor que " + str(a))
        print("-------------------------------------")
        