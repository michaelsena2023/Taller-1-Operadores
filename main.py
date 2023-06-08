ejercicios = 0

while ejercicios < 99:
  ejercicios = int(input("Ingrese el numero de ejercicio que desea ejecutar: "))
  if ejercicios == 1:
    #SUMA
    n1=int(input("ingrese su primer numero: "))
    n2=int(input("ingrese su segundo numero: "))
    sum=n1+n2
    print("El resultado de la suma es", sum)
  elif ejercicios == 2:
    #Potenciacion
    n1=int(input("ingrese el numero que le va colocar al cuadrado"))
    po=n1**2
    print("El cuadrado del numero es",po)
  elif ejercicios == 3:
    #Suma de 1234 + 532
    n1=1234
    n2=532
    print(f"El primer numero es {n1}")
    print(f"El segundo numero es {n2}")
    s=n1+n2
    print("El resultado de la suma es",s)
  elif ejercicios == 4:
    #Resta de 1234 - 532
    n1=1234
    n2=532
    print(f"El primer numero es {n1}")
    print(f"El segundo numero es {n2}")
    s=n1-n2
    print("El resultado de la resta es",s)
  elif ejercicios == 5:
    #Multiplicacion de 1234 * 532
    n1=1234
    n2=532
    print(f"El primer numero es {n1}")
    print(f"El segundo numero es {n2}")
    s=n1*n2
    print("El resultado de la multiplicacion es",s)
  elif ejercicios == 6:
    #division entre 1234 / 532
    n1=1234
    n2=532
    print(f"El primer numero es {n1}")
    print(f"El segundo numero es {n2}")
    s=n1/n2
    print("El resultado de la division es",s)
  elif ejercicios == 7:
    #Modulo entre 1234 y 532
    n1=1234
    n2=532
    print(f"El primer numero es {n1}")
    print(f"El segundo numero es {n2}")
    s=n1%n2
    print("El modulo entre los dos numeros es",s)
  elif ejercicios == 8:
    #euros a dolares
    n1 = int(input("ingrese la cantidad de euros que se convertiran en dolares "))
    n2 = 1.10
    euros=n1*n2
    print("el total de dolares es", euros)
  elif ejercicios == 9:
    #Area de un rectangulo
    n1=float(input("Ingrese el largo del rectangulo"))
    n2=float(input("Ahora ingrese el ancho del rectangulo"))
    A=n1*n2
    print("El area de su rectangulo es de", A)
  elif ejercicios == 10:
    #area y volumen de un cilindro
    print("calcularemos el area de su cilindro")
    n1=float(input("digite el radio de su cilindro"))
    pi=3.1416
    p=n1**2
    a2=pi*p
    print("El area es de)", a2)
    print("seguimos con el volumen ")
    n2=float(input("digite la altura de su cilindro"))
    altura=a2*n2
    print("el volumen de su cilindro es", altura)
  elif ejercicios == 11:
    #area y perimetro de un cuadrado
    print("se calculara el area de su cuadrado")
    n1=int(input("Ingrese el valor de un lado del cuadrado"))
    a=n1*n1
    print("El area del cuadrado es",a)
    p=n1+n1+n1+n1
    print("el perimetro del cuadrado es",p)
  elif ejercicios == 12:
    #Radio de una circunferencia y longitud
    n1=float(input("digite el valor del diametro de su circulo"))
    ñ=n1/2
    pi=3.14
    lon=pi*ñ
    l=p**2
    a=l*pi
    print("El valor del radio es de",ñ )
    print("El valor de la longitud es de", lon)
    print("el area de su circulo es de",a)
