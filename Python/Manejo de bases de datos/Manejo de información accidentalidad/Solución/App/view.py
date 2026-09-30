import sys
import App.logic as logic
from DataStructures.Tree import red_black_tree as bst
from datetime import datetime
from tabulate import tabulate
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
    print("10- Encontrar por ID")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    
    """
    filename = "accidents-large.csv"
    size,control = logic.load_data(control,filename) 
    encabezado_1 = [["ID", "Fecha", "Ciudad & Estado", "Descripción", "Tiempo (h)"]]
    encabezado_2 = encabezado_1.copy()
   
    ult = size - 5
    for i in range(0,5):
        
        
        
        dicc = bst.get(control["Orden"],i+1)
        dicc_ult = bst.get(control["Orden"],i+ult)
        tiempo = datetime.strptime(dicc["End_Time"], '%Y-%m-%d %H:%M:%S') - datetime.strptime(dicc["Start_Time"], '%Y-%m-%d %H:%M:%S')
        tiempo = tiempo.total_seconds()/3600
        
        tiempo_ult = datetime.strptime(dicc_ult["End_Time"], '%Y-%m-%d %H:%M:%S') - datetime.strptime(dicc_ult["Start_Time"], '%Y-%m-%d %H:%M:%S')
        tiempo_ult = tiempo_ult.total_seconds()/3600
        lista_1 = [dicc["ID"],dicc["Start_Time"], str(dicc["City"])+" "+str(dicc["State"]),dicc["Description"],tiempo]
        lista_2 = [dicc_ult["ID"],dicc_ult["Start_Time"], str(dicc_ult["City"])+" "+str(dicc_ult["State"]),dicc_ult["Description"],tiempo_ult]
        encabezado_1.append(lista_1)
        encabezado_2.append(lista_2)
    
    
    return size, encabezado_1, encabezado_2


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    
    encabezado = [["ID", "Fecha", "Ciudad & Estado", "Descripción", "Tiempo (h)", "Ingresos"]]
    dicc = logic.get_data(control,id)
    lista =[dicc["release_date"],dicc["title"], dicc["original_language"],dicc["runtime"],dicc["budget"],dicc["revenue"], dicc["ganancias"]]
    encabezado.append(lista)
    
def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control,rango,estados):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    encabezado_prim = [["Estado","Total", "Prom Visibilidad","Prom Distancia"]]
    encabezado_sec = [["Estado", "ID","Visibilidad","Distancia"]]
  
    tam,lis = logic.req_2(control,rango,estados)

 
    if lis is not None:
         
        for estado in list(lis.keys()):
            dicc = lis[estado]
            lista = [estado,dicc["Accidentes"],dicc["Promedio_v"],dicc["Promedio_d"] ]
            #lista = sorted(lista, key=lambda x:( x["Total"]) )
            encabezado_prim.append(lista)
            
            val =[estado,dicc["Mayor"],dicc["sv"],dicc["distancia"]]
            #val = sorted(val, key=lambda x:( x["Total"]) )
            encabezado_sec.append(val)
        
    return tam, encabezado_prim,encabezado_sec
def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control,i,f):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    encabezado = [["Nombre", "Ciudad","Condado","Estado", "Severidad", "Prom Visi"]]
    final = []
    lis,tot = logic.req_4(control,i,f)

    if lis is not None:
         
        lista =[{"Nombre": dicc["Nombre"],"Ciudad":dicc["Ciudad"], "Condado": dicc["Condado"],"Estado": dicc["Estado"],"Severidad":dicc["Severidad"],"Prom":dicc["Prom_Visi"]}for dicc in lis]
   
        lista = sorted(lista, key=lambda x:(x["Estado"], x["Condado"], x["Ciudad"], x["Nombre"]) )
    
        for dicc in lista:
            val =[dicc["Nombre"],dicc["Ciudad"], dicc["Condado"],dicc["Estado"],dicc["Severidad"],dicc["Prom"]]
            encabezado.append(val)
        
        
        
        for sub in encabezado:
            if sub not in final:
                final.append(sub)


        


    
        tot_3 = tot[0]
        tot_4 = tot[1]
    
    return final, tot_3, tot_4

def print_req_5(control,fechai,fechaf,clima):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    encabezado = [["Franja horaria","Hora" ,"Numero Total","Promedio","Condicion Climatica"]]
    rta = logic.req_5(control,fechai,fechaf,clima)
    
    for franja, estado in rta.items():
        x = [franja,estado['Zona'],estado['Numero'],estado['Promedio'],estado['Mayor Condicion']]
        encabezado.append(x)
    encabezado = [encabezado[0]] + sorted(encabezado[1:], key=lambda row: (row[2],row[3]),reverse=True)
    return encabezado
def print_req_6(control,i,f,cond,umbral_H, umbral_T):
    """ 
        Función que imprime la solución del Requerimiento 6 en consola
    """
    encabezado_lis = [["Condado", "Total","Temp Prom","Hum Prom", "Vel Prom", "Dist Prom"]]
    encabezado_grave = [["Condado", "ID","Fecha", "Temperatura", "Humedad","Distancia","Descripción"]]
    encabezado_final = [["Condado","ID","Fecha", "Humedad", "Temperatura","Distancia","Descripción"]]
    
    lis,grave, final = logic.req_6(control,i,f,cond,umbral_H, umbral_T)
    if lis is not None:
        
        for dicc in lis:
            
            lista =[{"Condado": dicc["Condado"],"Total":dicc["Número de Accidentes"], "Temp": dicc["Temperatura Prom"],"Hum": dicc["Humedad Prom"],"Vel":dicc["Velocidad Prom Viento"],"Dist":dicc["Distancia Prom (mi)"]}]
   
            lista = sorted(lista, key=lambda x:( x["Total"]) )
    
            for dicc in lista:
                val =[dicc["Condado"],dicc["Total"], dicc["Temp"],dicc["Hum"],dicc["Vel"],dicc["Dist"]]
                encabezado_lis.append(val)
        
    if grave is not None:
        for dicc in grave:
            lista =[{"Condado": dicc["Condado"],"ID":dicc["ID"], "Fecha": dicc["Fecha Inicio"],"Temp": dicc["Temperatura(F)"],"Hum": dicc["Humedad(%)"],"Dist":dicc["Distancia Afectada"],"Desc":dicc["Descripción del accidente"]}]
            lista = sorted(lista, key=lambda x:( x["Condado"]) )
            for dicc in lista:
                val =[dicc["Condado"],dicc["ID"], dicc["Fecha"],dicc["Temp"],dicc["Hum"],dicc["Dist"],dicc["Desc"]]
                encabezado_grave.append(val)
    
    if final is not None:  
        for i in range(0,len(final)):
            dicc = final[i]
            valor = list(dicc.values())
            valor = valor[0]
            for dicc in valor:
                lista =[{"Condado":dicc["Condado"],"ID":dicc["ID"], "Fecha": dicc["Fecha Inicio"],"Hum": dicc["Humedad(%)"],"Temp": dicc["Temperatura(F)"],"Dist":dicc["Distancia Afectada"],"Desc":dicc["Descripción del accidente"]}]
                lista = sorted(lista, key=lambda x:( x["Fecha"], x["Condado"]) )
                for dicc in lista:
                    val =[dicc["Condado"],dicc["ID"], dicc["Fecha"],dicc["Hum"],dicc["Temp"],dicc["Dist"],dicc["Desc"]]
                    encabezado_final.append(val)

    
    return encabezado_lis, encabezado_grave, encabezado_final


def print_req_7(control,la_minima, la_maxima,lo_minima, lo_maxima):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    encabezado = [["Fecha", "ID","Ciudad","Estado","Descripcion","Duracion","Latitud inicial","latitud final","longitud inicial", 'longitud final']]
    lista = logic.req_7(control,la_minima, la_maxima,lo_minima, lo_maxima)
    x = 0
 
    if lista['elements'] is not None:
        for dic in lista['elements']:
            x = [dic[1],dic[0],dic[2],dic[3],dic[4],dic[5],dic[6],dic[7],dic[8],dic[9]]
            encabezado.append(x)
    encabezado = [encabezado[0]] + sorted(encabezado[1:], key=lambda row: (row[6],row[7],row[8],row[9]),reverse=True)
    return lista['size'], encabezado




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
            tam,prim,ult = load_data(control)
            print("Total de películas cargadas: " + str(tam)+"\n")
            print("Información de las 5 primeras películas....\n")
            print(tabulate(prim, headers="firstrow", tablefmt="pipe")+"\n")
            print("Información de las 5 últimas películas....\n")
            print(tabulate(ult, headers="firstrow", tablefmt="pipe")+"\n")
            
            
        elif int(inputs) == 2:
            
            print_req_1(control)
            start = logic.get_time()
          
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")


        elif int(inputs) == 3:
            
            rango = input("Ingrese rango de visibildad: ")
            if "," in rango:
                
                rango = rango.split(",")
            else:
                rango = [rango]
            
            estados = input("Ingrese lista de estados: ")
            
            if "," in estados:
                
                estados = estados.split(",")
            else:
                estados = [estados]
            
            
            start = logic.get_time()
            tam,prim,sec = print_req_2(control,rango,estados)
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Total accidentes: " + str(tam)+"\n")
            print("Accidentes por Estado: \n")
            print(tabulate(prim, headers="firstrow", tablefmt="pipe")+"\n")
            print("Accidente más Grave por Estado: \n")
            print(tabulate(sec, headers="firstrow", tablefmt="pipe")+"\n")
            
            
            
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")


        elif int(inputs) == 4:
            print_req_3(control)
            start = logic.get_time()
          
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")

        elif int(inputs) == 5:
            i = input("Ingrese fecha inicial: ")
            f = input("Ingrese fecha final: ")
            start = logic.get_time()
            lis, tot_3, tot_4 = print_req_4(control,i,f)
            end = logic.get_time()
            print("Total de vías con severidad 3: " + str(tot_3)+"\n")
            print("Total de vías con severidad 4: " + str(tot_4)+"\n")
            print(tabulate(lis, headers="firstrow", tablefmt="pipe")+"\n")
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
            

        elif int(inputs) == 6:
            #entra una lista de condados, creo la lista
            fechai = input('Digte la fecha inicial: ')
            fechaf = input('Digte la fecha Final: ')
            clima = input('Digite los climas que desea buscar: ')
            if "," in clima:
                clima = clima.split(",")
            else:
                clima = [clima]
            start = logic.get_time()
            lis = print_req_5(control,fechai,fechaf,clima)
            end = logic.get_time()
            print(tabulate(lis, headers="firstrow", tablefmt="pipe")+"\n")
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
            
        elif int(inputs) == 7:
            i = input("Ingrese fecha inicial: ")
            f = input("Ingrese fecha final: ")
            cond = (input("Ingrese la lista de condados: "))
            if "," in cond:
                
                cond = cond.split(",")
            else:
                cond = [cond]
            umbral_H = input("Ingrese el umbral para la humedad: ")
            umbral_T = input("Ingrese el umbral para la temperatura: "+"\n")
            start = logic.get_time()
            lista,grave,final = print_req_6(control,i,f,cond,umbral_H, umbral_T)
            end = logic.get_time()
            print("Información de los accidentes por Condado \n")
            print(tabulate(final, headers="firstrow", tablefmt="pipe")+"\n")
            print("Información Promedio de los Condados \n")
            print(tabulate(lista, headers="firstrow", tablefmt="pipe")+"\n")
            print("Información del accidente más grave por Condado \n")
            print(tabulate(grave, headers="firstrow", tablefmt="pipe")+"\n")
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
        
        elif int(inputs) == 8:
            
            la_minima=  input("Ingrese latitud mínima:")
            la_maxima = input("Ingrese latitud máxima:")
            lo_minima= input("Ingrese longitud mínima:")
            lo_maxima= input("Ingrese longitud máxima: ")
            
            start = logic.get_time()
            t , tabla = print_req_7(control,la_minima, la_maxima,lo_minima, lo_maxima)
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print(t)
            if t > 10:
                print(tabulate(tabla[:6], headers="firstrow", tablefmt="pipe")+"\n")
                print(tabulate(tabla[-6:], headers="firstrow", tablefmt="pipe")+"\n")
            else:   
                print(tabulate(tabla, headers="firstrow", tablefmt="pipe")+"\n")
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")


        elif int(inputs) == 9:
            print_req_8(control)
            start = logic.get_time()
          
            end = logic.get_time()
            result = logic.delta_time(start,end)
            print("Tiempo de ejecución:", f"{result:.3f}", "[ms]"+"\n")
            
        elif int(inputs)==10:
            datos = print_data(control)
            print(tabulate(datos, headers="firstrow", tablefmt="pipe")+"\n")


        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
