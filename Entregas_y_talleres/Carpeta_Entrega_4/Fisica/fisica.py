def vel_prom(lista):
    """
    Esta función recibe una lista de velocidades y devuelve la velocidad promedio de ellas.
    
    Parámetros
    lista (list[float]): lista compuesta de una cantidad de velocidades
    
    Retorno:
    float, o sea, el número decimal que resultó de la operación
    """
    return sum(lista)/len(lista)

def acel_prom(lista):
    """
    Esta función recibe una lista de aceleraciones y devuelve la aceleración promedio de ellas.
    
    Parámetros
    lista (list[float]): lista compuesta de una cantidad de aceleraciones
    
    Retorno:
    float, o sea, el número decimal que resultó de la operación
    """
    return sum(lista)/len(lista)

def E_p(m,h,g=9.81):
    """ 
    Calcula la energía potencial de un objeto respecto a una altura
    
    Parámetros
    m(float): Masa del objeto 
    g(float): Valor de la gravedad en la tierra 
    h(float): Altura respecto a un punto del objeto 
    
    Retorno
    Devuelve el valor de la energía potencial asociada al objeto 
    """
    return(m*g*h)

def E_c(m,v):
    """ 
    Calcula la energía cinética de un objeto
    
    Parámetros
    m(float): Masa del objeto 
    v(float): Velocidad del objeto 
    
    Retorno 
    Devuelve el valor de la energía cinética asociada al objeto
    """
    return (0.5*m*(v**2))

if __name__== "__main__":
    print(E_c(1,1))
    print(E_p(1,1))