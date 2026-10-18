import energia,movimiento,conversiones

masa=float(input("Ingrese la masa de su objeto: ",))

opcion=int(input("\n¿Quisiera convertir su cantidad de masa antes de comenzar? Tenga en cuenta que la unidad ingresada debe estar en kilogramos. Ingrese 1 para 'Sí': ",))

if opcion==1:
    masa=conversiones.gr_kg(masa)

altura=float(input("\nIngrese la altura respecto a un punto de su objeto: ",))

opcion=int(input("\n¿Quisiera convertir su cantidad de altura antes de comenzar? Tenga en cuenta que la unidad ingresada debe estar en metros. Ingrese 1 para 'Sí': ",))

if opcion==1:
    opcion2=int(input("\nIngrese el respectivo número de su unidad a convertir en metros | Pulgadas [1]; Pies [2]; Centímetros [3]: "))
    match opcion2:
        case 1:
            altura=conversiones.in_m(altura)
        case 2:
            altura=conversiones.ft_m(altura)
        case 3:
            altura=conversiones.cm_m(altura)

velocidad=float(input("\nIngrese la velocidad del objeto: ",))

opcion=int(input("\n¿Quisiera convertir su cantidad de velocidad antes de comenzar? Tenga en cuenta que la unidad ingresada debe estar en m/s. Ingrese 1 para 'Sí': ",))
if opcion==1:
    velocidad=conversiones.kmh_ms(velocidad)

opcion3=int(input("\nBienvenido al programa 'Calculadora física'. Elija el módulo que desea utilizar insertando su respectivo número | Energía [1]; Movimiento uniforme [2]: ",))

match opcion3:
    case 1:
        print("La cantidad de energía cinética del objeto es de:",energia.E_c(masa,velocidad))
        print("\nLa cantidad de energía potencial del objeto es de:",energia.E_p(masa,altura))
    case 2:
        x0=float(input("\nIngrese la posición/recorrido inicial del objeto: ",))
        
        opcion=int(input("\n¿Quisiera convertir su cantidad de posición inicial/recorrido antes de comenzar? Tenga en cuenta que la unidad ingresada debe estar en metros. Ingrese 1 para 'Sí': ",))
        
        if opcion==1:
            opcion2=int(input("\nIngrese el respectivo número de su unidad a convertir en metros | Pulgadas [1]; Pies [2]; Centímetros [3]: "))
            match opcion2:
                case 1:
                    x0=conversiones.in_m(x0)
                case 2:
                        x0=conversiones.ft_m(x0)
                case 3:
                    x0=conversiones.cm_m(x0)
        
        t=float(input("\nIngrese la cantidad de tiempo en segundos que estuvo el objeto en movimiento: "))
        
        print("\nLa distancia que recorrió el objeto durante [",t,"] segundos fue de: ",movimiento.distancia_uni(x0,velocidad,t))