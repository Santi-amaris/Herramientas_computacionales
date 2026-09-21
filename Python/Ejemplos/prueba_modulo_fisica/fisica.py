G=6.67430e-11

def ener_cinetica(masa,velocidad):
    return 0.5*masa*velocidad**2

def ener_potencial(masa,altura):
    g=9.81
    return masa*altura*g