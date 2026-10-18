"""#Ejercicio 1 -- División segura 

def div(a,b):
        if (type(a)==float or int) and (type(b)==float or int):
                if b==0:
                        raise ZeroDivisionError ("Operación indefinida, no se puede dividir entre cero")
        return a/b
print(div(10,5))
# print(div(10,0)) | Arrojo el resultado que debería, funciona...

#Ejercicio 2 -- Conversión de edades

try:
        edad=int(input("Ingrese su edad: ",))
        if edad<0:
                raise ValueError ("Edad negativa detectada, vuelva ingresarla correctamente")
        print("Su edad es de:",edad)
except:
        raise ValueError ("Entrada no válida, vuelva a ingresarla")

#Se probó con los valores sugeridos y funcionó...

#Ejercicio 3 -- Acceso seguro a una lista

numeros=[10,20,30,40,50]
indice=0

try:
        indice=int(input("Ingrese el índice deseado a buscar:",))
        if (indice>5 or indice <0):
                raise IndexError ("Fuera del rango de índice permitido, vuelva a ingresarlo")
        else:
                print("El elemento del índice [",indice,"] es:",numeros[indice])
except:
        raise ValueError ("Entrada no válida, vuelva a ingresarla")

#Ejercicio 4 -- Diccionario de estudiantes

estudiantes ={
        "Ana": 4.5,
        "Carlos": 3.8,
        "Laura": 4.9,
        "Pedro": 3.2
}

nombre=(input("Ingrese el nombre del estudiante para ver su nota a continuación:",)).capitalize()

cont=0

for clave in estudiantes.keys():
        if (nombre==clave):
                print(estudiantes[nombre])
                cont+=1

if cont==0:
        raise KeyError ("Clave inexistente, vuelva ingresarla")

#Ejercicio 5 -- Validador de notas

nota=0
notas=[]

def validar_notas(nota):
        if (nota==-1):
                print(notas)
                raise SystemExit("Código finalizado...")
        elif (nota>5 or nota<0):
                raise ValueError ("Valor inválido, nota mayor que 5 o negativa. Vuelva a ingresarla")
        else:
                return nota

while nota!=-1:
        nota=float(input("Ingrese la nota que quiere ingresar al sistema. Ingrese '-1' para terminar: ",))
        validar_notas(nota)
        notas.append(nota)

#Ejercicio 6 -- Depuración en VS Code

def calcular_descuento(precio, porcentaje):
        descuento = precio * (porcentaje/100)
        precio_final = precio - descuento
        return precio_final

precio = 80000
porcentaje = 20

resultado = calcular_descuento(precio, porcentaje)

print("Precio final:", resultado)

#Preguntas 
#1. R/ Debería tener el valor 20/100 
#2. R/ Tiene el valor de 20
#3. R/...
#4. R/Se ejecutó paso por paso el programa...
#5. R/La correción se podría hacer cambiando la operación que realiza la función (ya está corregido) 
#6. Arroja el resultado esperado"""

#Ejercicio 7 -- Reto integrador

totales=[]
nombres=[]
precios=[]
cantidades=[]

def agregar_y_total(nombre,precio,cantidad):
        nombres.append(nombre)
        precios.append(precio)
        cantidades.append(cantidad)
        totales.append(cantidad*precio)


try:
        nombre=input("Ingrese el nombre del producto: ",)
        precio=float(input("Ingrese el precio del producto: ",))
        if precio<0:    
                raise ValueError ("Precio negativo, vuelva a ingresarlo...")
        cantidad=int(input("Ingrese la cantidad comprada del producto: ",))
        if cantidad<0:
                raise ValueError ("Cantidad negativa, vuelva a ingresarla...")
        agregar_y_total(nombre,precio,cantidad)
except ValueError as error:
        print("Error de valor, vuelva a intentarlo: ",error)
else:
        print("Este es el resumen:\n")
        print("- Nombre: ",nombre,"\n")
        print("- Precio: ",precio,"\n")
        print("- Cantidad: ",cantidad,"\n")
        print("- Total: ",precio*cantidad,"\n")
finally:
        print("Código finalizado...")