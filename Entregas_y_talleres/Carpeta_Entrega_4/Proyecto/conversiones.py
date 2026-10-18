def cm_m(cmm):
    """
    Esta función convierte una medida dada en centímetros a metros.
    
    Parámetros
    cmm (float): medida dada en centímetros
    
    Retorno:
    [medida] m, o sea, la medida inicial dada en centímetros convertida a metros
    """
    return cmm*(1/100)

def in_m(inm):
    """
    Esta función convierte una medida dada en pulgadas a metros.
    
    Parámetros
    inm (float): medida dada en pulgadas
    
    Retorno:
    [medida] m, o sea, la medida inicial dada en pulgadas convertida a metros
    """
    return inm*(2.54/100)

def ft_m(ftm):
    """
    Esta función convierte una medida dada en pies a metros.
    
    Parámetros
    ftm (float): medida dada en pies
    
    Retorno:
    [medida] m, o sea, la medida inicial dada en pies convertida a metros
    """
    return ftm*(0.3048)

def gr_kg(grkg):
    """
    Esta función convierte una medida dada en gramos a kilogramos.
    
    Parámetros
    grkg (float): medida dada en pies
    
    Retorno:
    [medida] kg, o sea, la medida inicial dada en gramos convertida a kilogramos
    """
    return grkg*(1/1000)

def kmh_ms(kmhms):
    """
    Esta función convierte una medida dada en km/h a m/s.
    
    Parámetros
    kmhms (float): medida dada en km/h
    
    Retorno:
    [medida] m/s, o sea, la medida inicial dada en km/h convertida a m/s
    """
    return kmhms*(1/3.6)

if __name__== "__main__":
    print(ft_m(1), "m")
    print(in_m(100), "m")
    print(cm_m(10), "m")
    print(gr_kg(1000), "m")