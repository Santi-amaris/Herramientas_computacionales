import fisica

lista_vels=[3.128,95.32,3.6] #Velocidades medidas de un objeto
lista_acels=[45.21,69.32,82,14.92,22.65] #Aceleraciones medidas de un objeto
m=26 #Masa del objeto
h=6.5 #Altura del objeto 

#Se asume que todos los datos suministrados están en unidades métricas. v(m/s), a(m/s^2), m(kg), h(m)

print("La velocidad promedio del objeto es de:",fisica.vel_prom(lista_vels),"[m/s]")
print("La aceleración promedio del objeto es de:",fisica.acel_prom(lista_acels),"[m/s]")
print("La energía cinética del objeto medida según su velocidad promedio es de:",fisica.E_c(m,fisica.vel_prom(lista_vels)),"[J]")
print("La energía potencial del objeto es de:",fisica.E_p(m,h),"[J]")