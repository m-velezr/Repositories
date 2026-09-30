import sys
import App.logic as logic
import os
import time
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-1/movies-90.csv'
    size = logic.load_data(control, data_dir)
    return size

def print_elements(catalog):
    
    prim, ult = logic.elements(catalog)
    print("\nLas primeras 5 películas cargadas son: \n")

    print(prim)
    
    
    print("\nLas últimas 5 películas cargadas son: \n")

    print(ult)
    
    
    
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    movie = logic.get_data(control, id)
    print("\nLa película buscada es: \n")
    
    print(movie)

def print_req_1(control, tiempo):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    peli, total = logic.req_1(control,tiempo)
    
    if peli == "":
        print("No se encuentran películas con un tiempo de duración mayor o igual a  " + str(time) )
    else:
        print( 'Tiempo de duración en minutos de la película: ' + peli['runtime'] + '  Fecha de publicación de la película: ' +
                  peli['release_date'] + ' Título original de la película : ' + 
                  peli['title'] + " Presupuesto destinado a la realización de la película: " + peli["budget"] +
                  " Dinero recaudado neto por la pelicula :" + peli["revenue"] + " Ganancia de final de película : " + peli["ganancias"] +
                  " Puntaje de calificación de la película :" + peli["vote_average"] + " Idioma original de publicación: " + peli["original_language"])
        print(str(total) + "  películas cumplen con el tiempo")


def print_req_2(control, idioma):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    peli, total = logic.req_2(control,idioma)
    
    if peli == "":
        print("No se encuentran películas con un tiempo de duración mayor o igual a  " + str(idioma) )
    else:
        print( 'Tiempo de duración en minutos de la película: ' + peli['runtime'] + '  Fecha de publicación de la película: ' +
                  peli['release_date'] + 'Título original de la película : ' + 
                  peli['title'] + "Presupuesto destinado a la realización de la película: " + peli["budget"] +
                  " Dinero recaudado neto por la pelicula :" + peli["revenue"] + "Ganancia de final de película : " + peli["ganancias"] +
                  "Puntaje de calificación de la película :" + peli["vote_average"] + " Idioma original de publicación: " + peli["original_language"])
        print(str(total) + "  películas cumplen con el tiempo")




def print_req_3(catalog,idioma,fecha_inicial,fecha_final):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    if idioma == '' or fecha_final < fecha_inicial:
        return 'Los parametro no fueron validos'
    rta = logic.req_3(catalog,idioma,fecha_inicial,fecha_final)
    if rta['Numero_peliculas'] > 20:
        rta = rta['peliculas'][:5]
    print('la informacion resultante entre los años establecidos: ', rta)
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control, fech_inf, fech_sup, t_inf, t_sup):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    peli, total, promedio = logic.req_5(control,fech_inf, fech_sup, t_inf, t_sup)
    if len(peli) > 20:
        peli = peli[:5]
        
    if len(peli) == 0:
        print("No se encuentran películas con estas características  " )
    else:
        print("Listado de películas: " + str(peli )+ "\n")
        print("Número total de películas que cumplen con las características: " + str(total) +  "\n" )
        print("Duración promedio de las películas: " + str(promedio) +  "\n" )

def print_req_6(control,idioma, anio_inicial,anio_final):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    if idioma == '' or anio_final < anio_inicial:
        return 'Los parametro no fueron validos'
    rta = logic.req_6(control,idioma,anio_inicial,anio_final)
    if len(rta)> 20:
        rta = rta[:5]+rta[len(rta)-6:]
    print('la informacion resultante entre los años establecidos: ', rta)
    


def print_req_7(catalog,productora, anio_inicial,anio_final):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    if productora == '' or anio_final < anio_inicial:
        return 'Los parametro no fueron validos'
    rta = logic.req_7(control,productora,anio_inicial,anio_final)
    print(rta)
    if len(rta) > 20:
        rta = rta[:5]+rta[len(rta)-6:]
    print('la informacion resultante entre los años establecidos: ', rta)
    

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            print("Películas cargadas:" + str(data))
            print_elements(control)
        
        elif int(inputs) == 2:
            tiempo = input("Digite el tiempo mínimo de duración: ")
            inicio = time.time()
            print_req_1(control, tiempo)
            fin = time.time()
            tiempo_ejecucion = fin - inicio
            
            print("Tiempo de ejecución en seg req. 1 : " + str(tiempo_ejecucion))

        elif int(inputs) == 3:
            
           
            print_req_2(control)

        elif int(inputs) == 4:
            idioma = input('Digite el idioma para la busqueda: ')
            fecha_inicial = input('Digite la fecha en la que se comienza a buscar: ')
            fecha_final = input('Digite la fehca en la que termina la busqueda: ')
            
            inicio = time.time()
            print_req_3(control,idioma,fecha_inicial,fecha_final)
            fin = time.time()
            tiempo_ejecucion = fin - inicio
            
            print("Tiempo de ejecución en seg req. 3 : " + str(tiempo_ejecucion))


        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            fech_inf = input("Ingresa la fecha inferior: ")


            fech_sup = input("Ingresa la fecha superior: ")
            t_inf = input("Ingresa el tiempo mínimo de duración: ")
            t_sup = input("Ingresa el tiempo máximo de duración: ")
            inicio = time.time()
            print_req_5(control, fech_inf, fech_sup, t_inf, t_sup)
            fin = time.time()
            tiempo_ejecucion = fin - inicio
            
            print("Tiempo de ejecución en seg req. 5 : " + str(tiempo_ejecucion))

        elif int(inputs) == 7:
            idioma = input('Digite el idioma para la busqueda: ')
            anio_inicial = input('Digite el año en la que se comienza a buscar: ')
            anio_final = input('Digite el año en la que termina la busqueda: ')
            
            inicio = time.time()
            print_req_6(control,idioma, anio_inicial,anio_final)
            fin = time.time()
            tiempo_ejecucion = fin - inicio
            print(tiempo_ejecucion)
        elif int(inputs) == 8:
            productora = input('Digite la productora para la busqueda: ')
            anio_inicial = input('Digite el año en la que se comienza a buscar: ')
            anio_final = input('Digite el año en la que termina la busqueda: ')
            
            inicio = time.time()
            print_req_7(control,productora, anio_inicial,anio_final)
            fin = time.time()
            tiempo_ejecucion = fin - inicio
            print(tiempo_ejecucion)

        elif int(inputs) == 9:
            print_req_8(control)
        
        elif int(inputs) == 10:
            id = input("Escriba el ID de la película que busca: ")
            print_data(control, id)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
