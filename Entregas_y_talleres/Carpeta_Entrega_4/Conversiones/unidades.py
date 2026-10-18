def m_km(mkm):
    """
    Esta función convierte una medida dada en metros a kilómetros.
    
    Parámetros
    mkm (float): medida dada en metros
    
    Retorno:
    [medida] km, o sea, la medida inicial dada en metros convertida a kilómetros
    """
    return mkm*(1/1000)

def km_m(kmm):
    """
    Esta función convierte una medida dada en kilómetros a metros.
    
    Parámetros
    kmm (float): medida dada en kilómetros
    
    Retorno:
    [medida] m, o sea, la medida inicial dada en kilómetros convertida a metros
    """
    return kmm*(1000)

def m_cm(mcm):
    """
    Esta función convierte una medida dada en metros a centímetros.
    
    Parámetros
    mcm (float): medida dada en metros
    
    Retorno:
    [medida] cm, o sea, la medida inicial dada en metros convertida a centímetros
    """
    return mcm*(100)

def cm_m(cmm):
    """
    Esta función convierte una medida dada en centímetros a metros.
    
    Parámetros
    cmm (float): medida dada en centímetros
    
    Retorno:
    [medida] m, o sea, la medida inicial dada en centímetros convertida a metros
    """
    return cmm*(1/100)

if __name__== "__main__":
    print(m_km(1000))
    print(m_cm(1))
    print(cm_m(100))
    print(km_m(1))