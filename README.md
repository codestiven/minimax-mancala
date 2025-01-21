![Captura de pantalla](https://github.com/codestiven/minimax-mancala/raw/main/Captura%20de%20pantalla%202025-01-21%20134446.png)



Documentación del Proyecto Mancala
Introducción:
La presente documentacio n detalla el desarrollo y la implementacio n del 
proyecto "Mancala", realizado por el equipo compuesto por los miembros 
mencionados anteriormente. El proyecto Mancala es una implementacio n 
digital del juego de estrategia Mancala, que involucra la movilizacio n de fichas 
en un tablero con el objetivo de capturar la mayor cantidad de fichas posibles. 
Esta documentacio n proporciona una descripcio n exhaustiva de la estructura 
del proyecto, la arquitectura del sistema, los procedimientos implementados, 
los desafí os encontrados, las mejoras propuestas y las limitaciones 
identificadas.
Arquitectura del Sistema Propuesto:
El sistema del proyecto Mancala sigue una arquitectura de cliente-servidor en 
la que se presenta una interfaz gra fica interactiva para que los jugadores 
interactu en con la lo gica del juego. La arquitectura consta de los siguientes 
componentes:
1. Interfaz Gráfica (Cliente): Implementada utilizando la biblioteca 
Tkinter en Python, proporciona una experiencia visual a los jugadores. 
Permite la interaccio n con el tablero de juego, la toma de decisiones de 
movimiento y muestra informacio n relevante sobre el estado del juego.
2. Backend del Juego (Servidor): Contiene la lo gica del juego, incluyendo 
algoritmos de bu squeda (minimax) y evaluacio n para que la IA tome 
decisiones de juego. Maneja las reglas del juego, actualiza el tablero y 
determina el estado del juego.
Diagrama de Flujo de Datos y Proceso:
El flujo de datos y proceso en el proyecto Mancala se desarrolla de la siguiente 
manera:
1. El jugador interactu a con la interfaz gra fica, seleccionando opciones y 
realizando movimientos a trave s de clics en botones.
2. Cuando un jugador realiza un movimiento, se activa el me todo 
correspondiente en el backend del juego.
3. El backend calcula los movimientos va lidos, actualiza el tablero y 
determina el estado del juego, como ganador, empate o juego en curso.
4. La interfaz gra fica se actualiza para reflejar los cambios en el tablero y la 
informacio n del juego.
5. El juego continu a hasta que se cumple una condicio n de finalizacio n, 
momento en el cual se muestra el resultado final.
Procedimiento Realizado para Resolver el Problema:
Para resolver el problema de implementar el juego Mancala, se llevaron a cabo 
los siguientes pasos:
1. Diseño de la Interfaz Gráfica: Se disen o la interfaz gra fica utilizando la 
biblioteca Tkinter, creando botones, etiquetas y elementos visuales que 
permiten a los jugadores interactuar con el juego.
2. Implementación de la Lógica del Juego: Se desarrollo la lo gica del juego 
Mancala, incluyendo las reglas del movimiento de fichas, el ca lculo de 
capturas y el determinar al ganador.
3. Algoritmo Minimax y Evaluación: Se implemento el algoritmo de 
bu squeda Minimax para que la IA tome decisiones estrate gicas. Se disen o 
una funcio n de evaluacio n para evaluar la ventaja de un estado de juego.
4. Integración de la Interfaz y el Backend: Se establecio la comunicacio n 
entre la interfaz gra fica y el backend del juego, asegurando que las 
interacciones del jugador se reflejen en el tablero y viceversa.
5. Pruebas y Depuración: Se realizaron pruebas exhaustivas para 
identificar errores y verificar el correcto funcionamiento del juego en 
diferentes escenarios.
Formato de Salida Propuesto de la Información:
La interfaz gra fica del juego Mancala muestra informacio n relevante en tiempo 
real, incluyendo el jugador en turno, la posibilidad de ganar de la IA, la cantidad 
de fichas en manos del jugador y la dificultad de la IA. Al finalizar el juego, se 
muestra el resultado final, ya sea la victoria de un jugador o un empate.
Roles de los Miembros del Equipo y Trabajo Realizado:
Cada miembro del equipo asumio roles especí ficos para el desarrollo del 
proyecto:
• Stiven: Implemento la lo gica de bu squeda (algoritmo Minimax) y la 
evaluacio n para que la IA tome decisiones estrate gicas.
• Odiseo: Creo la interfaz gra fica interactiva utilizando la biblioteca Tkinter 
y gestiono la comunicacio n entre la interfaz y el backend.
• Idelfonso: Contribuyo en el disen o de la lo gica del juego, incluyendo la 
implementacio n de las reglas y el ca lculo de capturas.
• Yangel: Realizo pruebas exhaustivas para identificar errores y verificar el 
funcionamiento correcto del juego en diferentes situaciones.
Dificultades Encontradas en el Proyecto:
El desarrollo del proyecto Mancala presento ciertos desafí os, tales como:
• Integracio n y coordinacio n de la lo gica del juego entre la interfaz gra fica 
y el backend.
• Implementacio n y ajuste de los algoritmos de bu squeda y evaluacio n para 
lograr un comportamiento estrate gico de la IA.
• Coordinacio n y comunicacio n efectiva entre los miembros del equipo 
para garantizar la coherencia del proyecto.
Mejoras Propuestas en la Propuesta:
Se identificaron posibles mejoras para el proyecto Mancala, como:
• Implementar te cnicas de optimizacio n en los algoritmos de bu squeda 
para mejorar el rendimiento y la eficiencia en situaciones ma s complejas.
• Ampliar las caracterí sticas del juego, como ofrecer niveles ajustables de 
dificultad para la IA, opciones de juego en red y modos de juego 
adicionales.
• Mejorar la interfaz gra fica mediante elementos visuales y animaciones 
que enriquezcan la experiencia de juego.
Riesgos y Limitaciones:
Algunos riesgos y limitaciones identificados en el proyecto incluyen:
• Dependencia de recursos locales para la ejecucio n del juego, lo que podrí a 
limitar la escalabilidad en situaciones de alto tra fico.
• Posibles problemas de usabilidad o errores en la interfaz gra fica que 
podrí an afectar la experiencia del usuario.
• Limitaciones en la capacidad de ca lculo de la IA en situaciones de juego 
complejas.
Conclusiones:
El proyecto Mancala es una implementacio n exitosa de un juego de estrategia 
cla sico en un entorno digital. El equipo enfrento desafí os te cnicos y 
colaborativos, logrando una integracio n efectiva entre la interfaz gra fica y el 
backend del juego. Las mejoras propuestas ofrecen oportunidades para 
enriquecer la experiencia del usuario y expandir las capacidades del juego. El 
proyecto no solo demostro la capacidad del equipo para desarrollar software 
interactivo, sino que tambie n proporciono un espacio para el aprendizaje y la 
aplicacio n de algoritmos de bu squeda en un contexto de juego.
