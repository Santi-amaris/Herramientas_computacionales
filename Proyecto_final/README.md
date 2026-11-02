$\hspace{0.25cm}{\color{#ab7fab}{\underline{\huge{{\textbf{{Proyecto Final -- Simulador de Blackjack}}}}}}}$

$\hspace{0.5cm}{\color{#ab7fab}{\Large{\textbf{Santiago Andrés Amarís Álvarez}}}}$



Mi proyecto final consistirá en un simulador de un juego de casino, específicamente la modalidad de Blackjack, donde el usuario podrá competir contra el "dealer" (persona que representa a la "casa", dueña del casino, y que también reparte las cartas) con el objetivo de obtener ganancias apostando una suma de dinero inicial. El programa tendrá como estructura/referencia algunas de las reglas básicas de la modalidad del juego Blackjack, con el que se podrá interactuar mediante comandos/datos introducidos por el usuario a través de la interfaz del formato ".ipynb". 

Como tal esto no resuelve ningún problema en específico, solo busca ser una simulación (aunque reducida en alcance y complejidad) de una actividad de ocio lo más parecida posible a la realidad, dentro de mis capacidades.

Otra característica única del juego es que lo verdaderamente relevante es el valor de la carta (por ejemplo, una carta "Rey", una carta "Reina", una carta "Joker" o una carta "diez" tienen todas ellas el mismo valor dentro del juego que es de: 10 unidades), así que no importa su tipo (diamante, pica, trébol, corazones) lo cual reduce significativamente la complejidad del programa.



$\hspace{0.5cm}{\color{#ab7fab}{\large{\textbf{Funcionalidades principales}}}}$

Entre las funcionalidades principales del programa se encuentran: 

$\color{#ab7fab}{\hspace{0.375cm}{1.}}\hspace{0.125cm}$  "Hit" (Pedir cartas): El jugador podrá pedir cartas de valores aleatorios entre 1 y 11 (entre ellas las cartas de puntos: 2,3...,10; las cartas de figura: Rey, Reina, Joker cuyo valor en unidades es de 10; y por último la carta del "As" que es excepcional, ya que puede tomar como valor en unidades 1, o también 11, dependiendo de la conveniencia) para acercarse lo más posible al número 21, que es el máximo e ideal valor posible que permite el juego antes de perder, y por tanto perder el dinero apostado. 

$\color{#ab7fab}{\hspace{0.375cm}{2.}}\hspace{0.125cm}$  "Stand" (Quedarse/Pasar turno): El jugador podrá elegir quedarse (no tomar más cartas) si considera que el valor que tiene en mano es suficiente para obtener la victoria hasta que la ronda acabe.

$\color{#ab7fab}{\hspace{0.375cm}{3.}}\hspace{0.125cm}$  "Double Down" (Doblar la apuesta): El jugador podrá elegir doblar su apuesta inicial a cambio de obtener una única carta adicional, esto se puede realizar en cualquier momento del juego cuando el jugador lo considere adecuado.

$\color{#ab7fab}{\hspace{0.375cm}{4.}}\hspace{0.125cm}$  "Surrender" (Rendirse): El jugador podrá retirarse de la ronda de juego en cualquier momento cuando lo considere oportuno a cambio de perder la mitad de su apuesta inicial.

La ronda acaba hasta que el "Dealer" llegue como mínimo a la cantidad de 17, y en ese momento se planta y se da por terminada la ronda. Quien tenga más puntos cuando esto ocurra, ya sea el jugador o el "Dealer", gana la partida. Si alguno de los dos ("Dealer" o jugador) se pasa de los 21 puntos la ronda también acaba inmediatamente y quien se haya pasado pierde.

Si la ronda la gana el jugador obtiene de vuelta su apuesta inicial por duplicado, o sea, tiene una ganancia igual al valor de su apuesta inicial; si la ronda la gana el "Dealer" entonces el jugador pierde su apuesta inicial y no obtiene ninguna ganancia. 



$\hspace{0.5cm}{\color{#ab7fab}{\large{\textbf{Instrucciones de uso}}}}$



Al principio de la ejecución del programa se le pedirá al usuario introducir su nombre y este será un campo que no tendrá ninguna restricción. Luego se le pedirá al usuario la cantidad a apostar, la cual deberá ser ingresada en la interfaz exclusivamente en su formato númerico (por ejemplo: "100") sin comas y positiva. Cualquier otra cosa diferente será interpretada como un error y el programa le pedirá al usuario volver a ingresarla nuevamente. 

Luego, en la interfaz de Python el programa le preguntará al usuario cual acción quiere tomar, entre estas están: (1) "Hit"/Pedir carta que el usuario podrá elegir introduciendo exclusivamente el número respectivo en la consola; (2) "Stand"/Pasar turno que el usuario podrá elegir introduciendo exclusivamente el número respectivo en la consola; (3) "Double Down" que el usuario podrá elegir introduciendo exclusivamente el número respectivo en la consola; (4) "Surrender" que el usuario podrá elegir introduciendo exclusivamente el número respectivo en la consola.

Todas la anteriores opciones serán las únicas con las que el usuario podrá interactuar a través de una ronda y posteriormente cuando acabé la partida, toda la información de los movimientos hechos tanto por el jugador como por el "Dealer" serán impresas en la consola según se desarrolla el juego. 


$\hspace{0.5cm}{\color{#ab7fab}{\large{\textbf{Ejemplo de uso y resultados esperados}}}}$


Tomemos de ejemplo la siguiente situación: 

${\color{#ab7fab}{{\Longrightarrow}}}\hspace{0.125cm}$  Comienza el programa.

${\color{#ab7fab}{{\Longrightarrow}}}\hspace{0.125cm}$  El jugador introduce la apuesta inicial de "100" (unidad monetaria cualquiera, dólares, euros, pesos, libras, etc...) en la interfaz.

${\color{#ab7fab}{{\Longrightarrow}}}\hspace{0.125cm}$  El "Dealer" le da la bienvenida al jugador y le reparte una carta de la baraja al jugador, que en este ocasión fue una carta "Rey" (valor unitario: 10). El "Dealer" selecciona una carta de la baraja para sí mismo, en este caso fue una carta "Joker". Toda la información de este turno que sería el primero (1) se imprime en la consola una vez terminado por completo. 

${\color{#ab7fab}{{\Longrightarrow}}}\hspace{0.125cm}$  Se le da paso al jugador para que tome una acción (la cual se muestra en la interfaz y debe ser introducida). El jugador en este caso elige la número uno (1) "Hit"/Pedir carta e inmediatamente el "Dealer" se la reparte; le salió una carta "9" y se le suma a la cantidad que tenía previamente el jugador ("Rey";10), quedando finalmente un total de 19 puntos. Acaba el turno y se le da paso al "Dealer".

${\color{#ab7fab}{{\Longrightarrow}}}\hspace{0.125cm}$  El "Dealer" toma otra carta de la baraja, en este caso le salió una carta "9", la cual se suma a la cantidad que tenía previamente, dando un total de 19 puntos. Como el "Dealer" llegó al requisito mínimo de puntuación la ronda acaba en ese instante. 

${\color{#ab7fab}{{\Longrightarrow}}}\hspace{0.125cm}$  Al final como ambas partes obtuvieron la misma puntuación la ronda termina en un empate... (Finaliza el programa y toda la información se muestra en consola). Ninguna parte gana y al jugador se le es devuelta su apuesta inicial íntegramente.

En otro caso si el jugador se hubiera pasado de la puntuación máxima permitida, el "Dealer" habría ganado y el jugador perdido su apuesta inicial. Caso contrario, si el "Dealer" se hubiera pasado este perdía y el jugador habría obtenido una ganancia neta igual a la apuesta inicial apostada.

Los demás resultados esperados como aquel en que el turno acaba bien para el jugador y este elige como última acción previa a su victoria la opción (3) "Double Down", se obtendría una ganancia de 3 veces el valor de apuesta inicial, si no se cuenta la apuesta inicial (por ejemplo, si su apuesta inicial fue de 100, entonces se habría obtenido una ganancia neta de 300, para sumar un total de 400). Al final los resultados se reducen a tres posibilidades: Victoria, Empate o Derrota.  
