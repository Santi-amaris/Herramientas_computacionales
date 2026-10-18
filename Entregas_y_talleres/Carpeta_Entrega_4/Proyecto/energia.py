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

if __name__== "__main__":
    print(E_c(2,2))
    print(E_p(2,2))