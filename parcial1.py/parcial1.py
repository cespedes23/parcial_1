
def obtener_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)

with open(obtener_path_actual("movies.csv"), "r", encoding="utf-8") as archivo:
    peliculas = []
    encabezado = archivo.readline().strip("\n").split(",")

    for linea in archivo.readlines():
        pelicula = {}
        linea = linea.strip("\n").split(",")
    #d_peli, titulo, genero, rating
        id, titulo, genero, rating = linea
        pelicula["id"] = int(id)
        pelicula["titulo"] = titulo
        pelicula["genero"] = genero
        pelicula["rating"] = int(rating)
        peliculas.append(pelicula)


for pelicula in peliculas:
    print(pelicula)




def entero_in_lista_1(lista: list, target: int) -> bool:
    return target in lista

def cargar_lista_rating(lista: list, cantidad: int) -> list:
    from random import randint
    LEGAJO_MIN = 1
    LEGAJO_MAX = 10
    for _ in range(cantidad):
        rating = randint(LEGAJO_MIN, LEGAJO_MAX)
        while entero_in_lista_1(lista, rating):
            rating = randint(LEGAJO_MIN, LEGAJO_MAX)
        lista.append(rating)
    return lista

lista_rating_peliculas = []
lista_rantings_random = cargar_lista_rating(lista_rating_peliculas, 10)









