import sys
import App.logic as logic
from DataStructures.Graph import adj_list_graph as graph
from datetime import datetime
from tabulate import tabulate

def new_logic():
    """
        Se crea una instancia del controlador
    """
    catalog = logic.new_logic()
    return catalog

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
    rela = "relationships_large.csv"
    users = "users_info_large.csv"
    tot_usu, conexiones, basic, premium, dic_conexiones, lis_ciudad = logic.load_data(control,rela,users) 
    encabezado = [["Usuario", "Prom Seguidores"]]
    
    
    for val in dic_conexiones:
        lista = [val, dic_conexiones[val]]
        encabezado.append(lista)
    
    
    
    print("Número total de usuarios en la red :" + str(tot_usu) + "\n")
    print("Número de conexiones entre los usuarios :" + str(conexiones) + "\n")
    print("Número de usuarios con cuenta Basic :" + str(basic) + "\n")
    print("Número de usuarios con cuenta Premium :" + str(premium) + "\n")
    print("Ciudad con mayor cantidad de usuarios :" + lis_ciudad[0] + "  y Número de usuarios : " + str(lis_ciudad[1]) + "\n")
    print(tabulate(encabezado[0:5], headers="firstrow", tablefmt="pipe")+"\n")
    
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control,v1,v2):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    rta, m1,m2= logic.req_1(control,v1,v2)
    if rta == False:
        print('No se encontro camino')
    else:
        print('Si se encontro camino')
        print(m1)
        print(m2)

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control,ID):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    tot,amigo=logic.req_3(control,ID)
    print("Amigo con mayor número de seguidores :" + amigo + "\n")
    print("Número total de seguidores:" + str(tot) + "\n")


def print_req_4(control,ID1,ID2):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    print(logic.req_4(control,ID1,ID2))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control,num):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    cuentas, conectado = logic.req_6(control,num)
    print(cuentas)
    print(conectado)

def print_req_7(control,hobby,ID):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    
    imp,hob_imp,prof_imp, exp,hob_ex,prof_ex= logic.req_7(control,ID,hobby)
    encabezado_exp = [["ID", "Nivel Profundidad","Hobbies"]]
    encabezado_imp = [["ID", "Nivel Profundidad","Hobbies"]]
    
    if len(exp) !=0:
        for i in range(0,len(exp)):
            lis_exp = []
            lis_exp.append(exp[i])
            lis_exp.append(prof_ex[i])
            lis_exp.append(hob_ex[i])
            encabezado_exp.append(lis_exp)
    
    if len(imp) !=0:
        for i in range(0,len(imp)):
            lis_imp = []
            lis_imp.append(imp[i])
            lis_imp.append(prof_imp[i])
            lis_imp.append(hob_imp[i])
            encabezado_imp.append(lis_imp)
            
    return encabezado_exp,encabezado_imp        
            
    
    

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    


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
            load_data(control)
        elif int(inputs) == 2:
            
            v1= input('Digite el primer vertice: ')
            v2 = input('Digite el segundo vertice: ')
            start = logic.get_time()
            print_req_1(control,v1,v2)
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
            
        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            ID = input("Ingrese ID de la persona: ")
            start = logic.get_time()
            print_req_3(control,ID)
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
            

        elif int(inputs) == 5:
            
            ID1 = input('Digite el primer ID: ')
            ID2 = input('Digite el segundo: ')
            start = logic.get_time()
            print_req_4(control,ID1,ID2)
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
            
        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            num = input('Digte cuantas cuentas quiere: ')
            start = logic.get_time()
            print_req_6(control,num)
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")

        elif int(inputs) == 8:
            hobby = input('Digite los hobbies que desea buscar: ')
            ID = input("Ingrese ID de la persona: ")
            if "," in hobby:
                hobby = hobby.split(",")
            else:
                hobby = [hobby]    
            start = logic.get_time()
            exp,imp = print_req_7(control,hobby,ID)
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Seguidores Explícitos: \n")
            print(tabulate(exp, headers="firstrow", tablefmt="pipe")+"\n")
            print("Seguidores Implícitos: \n")
            print(tabulate(imp, headers="firstrow", tablefmt="pipe")+"\n")
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
            

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
