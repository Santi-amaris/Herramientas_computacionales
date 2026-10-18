def distancia_uni(x0,v,t):
    """
    Calcula una distancia d a partir de dos valores iniciales de velocidad y tiempo, y posición inicial
    
    Parámetros
    x0(float): Posición/recorrido inicial del objeto
    v(float): Velocidad inicial constante dada de un objeto
    t(float): Tiempo hasta el cual se quiere determinar la distancia que recorre un objeto
    
    Retorno
    Devuelve la distancia total recorrida por un objeto en MRU
    """
    return x0+(v*t)

if __name__=="__main__":
    print(distancia_uni(0,10,1))