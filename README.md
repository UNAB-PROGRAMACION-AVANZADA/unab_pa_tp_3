 ## Taller POO - Clase 3
Ejercicios de Programación Orientada a Objetos en Python. Cada clase está en su propio archivo dentro de src/.
Integrantes

Jorge Ordoñez

# Estructura
--  src/punto.py
--  src/linea.py
--  src/cancion.py
--  src/Libro.py
--  src/Persona.py
--  main.py
# Ejercicios

##  Punto
Representa un punto en el plano con coordenadas x e y. Tiene métodos para obtener cada eje, imprimir las coordenadas y calcular el punto opuesto.

##   Linea
Representa una línea formada por dos objetos Punto. Permite moverla en las cuatro direcciones pasando una distancia como parámetro.

##  Cancion
Modela una canción con título, autor y duración. Le agregué algunas cosas por mi cuenta que estuve viendo en clase: un contador automático que asigna un ID a cada canción, la fecha de creación usando datetime, y un método guardar_json() que guarda las canciones en un archivo sin pisar las anteriores.

 ## Libro
Modela un libro con todos sus datos bibliográficos. El atributo autor es un objeto de tipo Persona, lo que me permitió aplicar composición de clases. Tiene métodos separados para leer y mostrar la información.
Cómo ejecutar
bashpython main.py