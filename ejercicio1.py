import math
import turtle

# Pruebas:
pruebaChi = False
pruebaVodka = False

# Metodo de RN:
numero = 9  # Semilla
k = 13091206342165455000  # Constante
weyl = 0  # Secuencia weyl, evitando que el algoritmo se vuelva ciclico


def miMetodoRN():
    global numero
    global contador
    global k
    global weyl

    numero = numero * numero
    weyl += k
    numero += weyl
    numero = (numero >> 32) | (numero << 32)
    corteA = int((len(str(numero)) - 16) / 2)
    numero = str(numero)[corteA: corteA + 16]
    numero = int(numero)

    return numero


# Metodo para imprimir con Turtle:
def imprimeChi():
    acumulado = 0.0
    turtle.setup(520, 540)  # Tamano de la pantalla
    turtle.speed(20)  # Velocidad del dibujo
    # Titulo del dibujo
    turtle.penup()
    turtle.goto(0, 200)
    turtle.write("Categorias Chi:", align="center", font=("Comic Sans", 30, "normal"))
    # Posicion inicial
    turtle.goto(-240, -230)
    turtle.pendown()
    turtle.pensize(10)  # Tamano de la barra
    maxLen = (len(numeros) / 20) * 1.5  # El tamano maximo de la grafica
    turtle.right(270)

    for i in categories:
        turtle.forward((500 / maxLen) * i)
        turtle.penup()
        turtle.right(180)
        turtle.forward(((500 / maxLen) * i) + 20)
        acumulado += .05
        turtle.write(acumulado, align="center", font=("Comic Sans", 10, "normal"))
        turtle.right(180)
        turtle.forward(20)
        turtle.right(180)

        turtle.right(-90)
        turtle.penup()
        turtle.forward(25)
        turtle.right(270)
        turtle.pendown()

    turtle.exitonclick()
    return


# Pruebas:
# Haciendo todos los numeros random posibles:
numeros = []
num = str(miMetodoRN())
if len(num) == 15:
    num = '.0' + num
else:
    num = '.' + num
num = float(num)

# Categorias para Chi:
categories = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
chiValueW20CategoriesAnd05DegreesOfFreedom = 31.41
cont = 0
while numero not in numeros and cont < 10_000_000:
    cont += 1
    print(cont)
    numeros.append(num)  # Agregando el numero a la lista total de numeros random
    if num < .05:  # Dependiendo del valor random categorizamos:
        categories[0] += 1
    elif num < .1:
        categories[1] += 1
    elif num < .15:
        categories[2] += 1
    elif num < .2:
        categories[3] += 1
    elif num < .25:
        categories[4] += 1
    elif num < .3:
        categories[5] += 1
    elif num < .35:
        categories[6] += 1
    elif num < .4:
        categories[7] += 1
    elif num < .45:
        categories[8] += 1
    elif num < .5:
        categories[9] += 1
    elif num < .55:
        categories[10] += 1
    elif num < .6:
        categories[11] += 1
    elif num < .65:
        categories[12] += 1
    elif num < .7:
        categories[13] += 1
    elif num < .75:
        categories[14] += 1
    elif num < .8:
        categories[15] += 1
    elif num < .85:
        categories[16] += 1
    elif num < .9:
        categories[17] += 1
    elif num < .95:
        categories[18] += 1
    else:
        categories[19] += 1

    num = str(miMetodoRN())
    if len(num) == 15:
        num = '.0' + num
    else:
        num = '.' + num
    num = float(num)

# Prueba Chi:
calculoChi = categories[:]
e = int(len(numeros) / 20)

for i in range(len(calculoChi)):
    calculoChi[i] = ((calculoChi[i] - e) ** 2) / e
res = 0.0
for i in calculoChi:
    res += i
if res < chiValueW20CategoriesAnd05DegreesOfFreedom:
    pruebaChi = True

print(f"Paso chi: ", pruebaChi)
imprimeChi()
