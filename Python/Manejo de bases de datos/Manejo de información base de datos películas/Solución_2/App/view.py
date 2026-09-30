import sys
import App.logic as logic
import os
import time
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
from tabulate import tabulate
from DataStructures.Map import map_linear_probing as mp

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
    print("10- Ejecutar Cargar Información Según ID")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-2/movies-large.csv'
    size = logic.load_data(control, data_dir)
    
    encabezado_1 = [["Fecha", "Título", "Idioma", "Duración", "Presupuesto", "Ingresos", "Ganancias"]]
    encabezado_2 = encabezado_1.copy()
   
    ult = size - 5
    for i in range(0,5):
        
        
        
        dicc = mp.get(control["movie_order"],i+1)
        dicc_ult = mp.get(control["movie_order"],i+ult)
        
        lista_1 = [dicc["release_date"],dicc["title"], dicc["original_language"],dicc["runtime"],dicc["budget"],dicc["revenue"], dicc["ganancias"]]
        lista_2 = [dicc_ult["release_date"],dicc_ult["title"], dicc_ult["original_language"],dicc_ult["runtime"],dicc_ult["budget"],dicc_ult["revenue"], dicc_ult["ganancias"]]
        encabezado_1.append(lista_1)
        encabezado_2.append(lista_2)
    
    
    return size, encabezado_1, encabezado_2


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
     
    encabezado = [["Fecha", "Título", "Idioma", "Duración", "Presupuesto", "Ingresos", "Ganancias"]]
    dicc = logic.get_data(control,id)
    if dicc != None :
        
        lista= [dicc["release_date"],dicc["title"], dicc["original_language"],dicc["runtime"],dicc["budget"],dicc["revenue"], dicc["ganancias"]]
        encabezado.append(lista)
        return encabezado
    else:
        return None

def print_req_1(control,nombre, idioma):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    encabezado = [["Fecha", "Título", "Idioma", "Duración", "Presupuesto", "Ingresos", "Puntaje","Ganancias"]]
    dicc = logic.req_1(control,nombre,idioma)
    if len(dicc) != 0 :
        
        for i in range(0,len(dicc)):
            
            lista= [dicc[i]["release_date"],dicc[i]["title"], dicc[i]["original_language"],dicc[i]["runtime"],dicc[i]["budget"],dicc[i]["revenue"], dicc[i]["vote_average"],dicc[i]["ganancias"]]
            encabezado.append(lista)
        return encabezado
    else:
        return None
        
    


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control,idioma,fecha_i,fecha_f):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    lista = logic.req_3(control,idioma,fecha_i,fecha_f)
    if lista["size"] >0:
        return lista
    


def print_req_4(control,produccion,fecha_i,fecha_f):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    lista = logic.req_4(control,fecha_i,fecha_f,produccion)
    return lista



def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control,idioma, fech_inf,fech_sup):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    dicc = logic.req_6(control,idioma,fech_inf,fech_sup)
    return dicc

def print_req_7(control,compania,fecha_i,fecha_f):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    lista = logic.req_7(control,fecha_i,fecha_f,compania)
    return lista
def print_req_8(control,fecha_i,genero):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    lista =  logic.req_8(control,fecha_i,genero)
    return lista

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
            tam, prim,ult = load_data(control)
            print("Total de películas cargadas: " + str(tam)+"\n")
            print("Información de las 5 primeras películas....\n")
            print(tabulate(prim, headers="firstrow", tablefmt="pipe")+"\n")
            print("Información de las 5 últimas películas....\n")
            print(tabulate(ult, headers="firstrow", tablefmt="pipe")+"\n")
            

            
        elif int(inputs) == 2:
            nombre = input("Ingrese el título de la película a buscar: ")
            idioma = input("Ingrese el idioma de la película a buscar: ")
            start =  logic.get_time()
            lista = print_req_1(control, nombre, idioma)
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")

            if lista != None:
                
                print("Información de la película buscada....\n")
                print(tabulate(lista, headers="firstrow", tablefmt="pipe")+"\n")
            else:
                 print("No se encuentra pelicula")


        elif int(inputs) == 3:
            idioma = input("Digite el idioma a buscar: ")
            fecha_i = input("Digite la fecha para empezar: ")
            fecha_f = input("Digite la fecha para termianr: ")
            print_req_3(control,idioma,fecha_i,fecha_f)

        elif int(inputs) == 4:
            idioma = input("Digite el idioma a buscar: ")
            fecha_i = input("Digite la fecha para empezar: ")
            fecha_f = input("Digite la fecha para termianr: ")
            start = logic.get_time()
            x = print_req_3(control,idioma,fecha_i,fecha_f)
            end = logic.get_time()
            print(x["size"])
            print(x["elements"])
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
        elif int(inputs) == 5:
            status = input("Digite el estado de la pelicula: ")
            fecha_i = input("Digite la fecha para empezar: ")
            fecha_f = input("Digite la fecha para termianr: ")
            start = logic.get_time()
            x = print_req_4(control,status,fecha_i,fecha_f)
            end = logic.get_time()
            print(x["size"])
            print(x['elements'])
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            fech_inf = int(input("Ingrese la fecha inferior: "))
            fech_sup = int(input("Ingrese la fecha superior: "))
            idioma = input("Ingrese el idioma de la película a buscar: ")
            start = logic.get_time()
            lista = print_req_6(control,idioma, fech_inf,fech_sup)
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
            
            if lista != None:
                print("Información de las peliculas buscadas....\n")
                print(tabulate(lista, headers="firstrow", tablefmt="pipe")+"\n")
            else:
                 print("No se encuentra pelicula")
                

        elif int(inputs) == 8:
            fecha_i = int(input("Ingrese la fecha inferior: "))
            fecha_f = int(input("Ingrese la fecha superior: "))
            productora = input("Ingrese la productora: ")
            start = logic.get_time()
            rta = print_req_7(control,productora,fecha_i,fecha_f)
            end = logic.get_time()
            print(rta)
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
            
        elif int(inputs) == 9:
            fecha_i = int(input("Ingrese la fecha inferior: "))
            genero = input("Ingrese el genero: ")
            start = logic.get_time()
            rta = print_req_8(control,fecha_i,genero)
            end = logic.get_time()
            print(rta)
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
        
        elif int(inputs) == 10:
            id = input("Ingrese el ID de la película a buscar: ")
            lista = print_data(control, id)
            print("Información de la película....\n")
            if lista != None:
                
                print(tabulate(lista, headers="firstrow", tablefmt="pipe"+"\n"))
            else:
                print("No se encuentro pelicula")

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
