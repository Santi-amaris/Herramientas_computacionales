import fisica
import conversiones
Ec= fisica.ener_cinetica(2,10)
Ep= fisica.ener_potencial(10,50)
temp=25
dist=10
print(Ec)
print(Ep)
print(conversiones.celsius_fahrenheit(temp))
print(conversiones.fahrenheit_celsius(temp))
print(conversiones.km_millas(dist))
print(conversiones.millas_km(dist))