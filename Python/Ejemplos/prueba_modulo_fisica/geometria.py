import math 

#Definición funciones

def area_circu(r):
    """
    Esta función calcula el área de un círculo de radio r dado.
    
    Parámetros
    r (float): Radio del círculo
    
    Retorno:
    A, o sea, el área del círculo
    """
    return (math.pi)*r**2

def area_rect():
    """
    Esta función calcula el área de un rectángulo de base y altura dadas.
    
    Parámetros
    r (float): Radio del círculo
    
    Retorno:
    A, o sea, el área del círculo
    """
    base= float(input("Ingrese la base deseada:",))
    altura= float(input("Ingrese la altura deseada:",))
    return base*altura