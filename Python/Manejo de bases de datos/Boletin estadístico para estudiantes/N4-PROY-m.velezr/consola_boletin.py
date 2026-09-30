# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletin Estadistico
Consola.

Temas:
* Recorridos de Matrices.
* Librerias de Matplotlib.
@author: Cupi2


"""

import boletin as be

def mostrar_menu() -> None:
    """Imprime las opciones de ejecucion disponibles para el usuario."""
    
    print("\nOpciones")
    print("1. Cargar archivos")
    print("2. Consultar puestos estudiante atendidos por una facultad")
    print("3. Consultar puestos estudiante ocupados por una facultad")
    print("4. Consultar la facultad mas servicial ")
    print("5. Consultar si existe una facultad generosa")
    print("6. Calcular el porcentaje de autocubrimiento ") 
    print("7. Consultar el doble progama mas popular")
    print("8. Mostrar PGA promedio de facultades")
    print("9. Mostrar puestos usados por Estudios Dirigidos")  
    print("10. Salir de la aplicacion")
 
    
def ejecutar_cargar_matriz_estadisticas() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de estadisticas de facultades y la carga.
    Retorno: list
        La matriz de estadisticas de las facultades.
    """
    estadisticas = list()
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de estadisticas: ")
    estadisticas = be.cargar_matriz_estadisticas(str(archivo)+".csv") 
    if len(estadisticas) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de estadisticas")
    else:
        print("Se cargo la matriz de estadisticas")
    return estadisticas    


def ejecutar_cargar_matriz_puestos() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de los puestos estudiante y la carga.
    Retorno: list
        La matriz de los puestos estudiante.
    """
    puestos = list()
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de puestos estudiante: ")
    puestos = be.cargar_matriz_puestos(str(archivo)+".csv")
    if len(puestos) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de puestos estudiante")
    else:
        print("Se cargo la matriz de puestos estudiante")
        

    return puestos    


def ejecutar_cargar_matriz_dobles() -> list:
    """Solicita al usuario que ingrese el nombre de un archivo CSV con los datos de
    la matriz de dobles programas y la carga.
    Retorno: list
        La matriz de los dobles programas entre las carreras.
    """
    dobles = list()
    archivo = input("Por favor ingrese el nombre del archivo CSV con la matriz de dobles programas: ")
    dobles = be.cargar_matriz_dobles(str(archivo)+".csv") 
    if len(dobles) == 0:
        print("El archivo seleccionado no es valido. No se pudo cargar la matriz de dobles programas")
    else:
        print("Se cargo la matriz de dobles programas")
    
  
    
    return dobles
        


def ejecutar_puestos_atendidos(puestos:list) -> None:
    """ Ejecuta la opcion de consultar los puestos estudiantes atendidos
    por una facultad en especifico
    """   
    facultad = input("Ingrese la facultad de su interes. La primera letra de cada facultad debe estar en mayúscula : ")#Preguntar sobre esto
    puestos=ejecutar_cargar_matriz_puestos()
    cantidad=be.puestos_ofrecidos_por_facultad(puestos, facultad)
    if cantidad==None:
        print("La facultad seleccionada no se encuentra.")
    else:
        print("La facultad de "+str(facultad)+"  tiene una cantidad de "+str(cantidad)+ "  puestos ofrecidos")
    
    


def ejecutar_puestos_ocupados(puestos:list) -> None:
    """ Ejecuta la opcion de consultar los puestos estudiantes ocupados
    por una facultad en especifico
    """   
    facultad = input("Ingrese la facultad de su interes: ")
    puestos=ejecutar_cargar_matriz_puestos()
    cantidad=be.puestos_ocupados_facultad(puestos, facultad)
    if cantidad==None:
        print("La facultad seleccionada no se encuentra.")
    else:
        print("La facultad de "+str(facultad)+"  tiene ocupados "+str(cantidad)+ "  por estudiantes")
    

    
def ejecutar_facultad_mas_servicial(puestos:list) -> None:
    """ Ejecuta la opcion de consultar la facultad mas servicial
    """
   
    puestos=ejecutar_cargar_matriz_puestos()
    servicial=be.facultad_mas_servicial(puestos)
    print("La facultad mas servicial es "+str(servicial))
   
 
def ejecutar_hay_facultad_generosa(puestos:list) -> None:
    """ Ejecuta la opcion de consultar si existe una facultad generosa
    para una facultad en especifico
    """
    
    facultad = input("Ingrese la facultad de su interes: ")
    porcentaje = float(input("Ingrese el porcentaje de su interes: "))
    puestos=ejecutar_cargar_matriz_puestos()
    generosa=be.facultad_generosa(puestos, facultad, porcentaje)
    print(generosa)
 
def ejecutar_calcular_autocubrimiento(puestos:list, estadisticas:list) -> None:
    """ Ejecuta la opcion de calcular el autocubrimiento para todas
    las facultades
    """
    puestos=ejecutar_cargar_matriz_puestos()
    estadistica=ejecutar_cargar_matriz_estadisticas()
    modificada=be.autocubrimiento(puestos, estadistica)
    print(modificada)
    
   
    
    
def ejecutar_doble_mas_comun(dobles:list) -> None: 
    """ Ejecuta la opcion de consultar el doble programa mas comun
    """
    dobles=ejecutar_cargar_matriz_dobles()
    popular=be.doble_mas_popular(dobles)
    print(popular)
    
    
    

def ejecutar_mostrar_pga_promedio()->None:
    """
        Ejecuta la opción de mostrar el PGA promedio por facultad,
        ordenado de menor a mayor
    """
    ruta_archivo_estadisticas = input("Ingrese el nombre del archivo de estadísticas: ")
    PGA=be.PGA__promedio(str(ruta_archivo_estadisticas)+".csv")
    
    return PGA
    
    

def ejecutar_mostrar_puestos_estudios_dirigidos()->None:
    """
        Ejecuta la opción de mostrar los puestos ocupados por Estudios Dirigidos
        en todas las facultades
    """
    ruta_archivo_puestos = input("Ingrese el nombre del archivo de puestos: ")
    ocupados=be.puestos_usados_estudios_dirigidos(str(ruta_archivo_puestos)+".csv")
    return ocupados
    
    
    
    
def iniciar_aplicacion():
    """Ejecuta el programa para el usuario."""
    continuar = True
    dobles = list()
    estadisticas = list()
    puestos = list()
    while continuar:
        mostrar_menu()
        opcion_seleccionada = input("Por favor seleccione una opcion: ")
        if opcion_seleccionada == "1":
            dobles=ejecutar_cargar_matriz_dobles()
            estadisticas=ejecutar_cargar_matriz_estadisticas()
            puestos=ejecutar_cargar_matriz_puestos()
            
        elif opcion_seleccionada == "2":
            ejecutar_puestos_atendidos(puestos)
        elif opcion_seleccionada == "3":
            ejecutar_puestos_ocupados(puestos)            
        elif opcion_seleccionada == "4":
            ejecutar_facultad_mas_servicial(puestos)
        elif opcion_seleccionada == "5":
            ejecutar_hay_facultad_generosa(puestos)
        elif opcion_seleccionada == "6":
            ejecutar_calcular_autocubrimiento(puestos,estadisticas)                   
        elif opcion_seleccionada == "7":
            ejecutar_doble_mas_comun(dobles)
        elif opcion_seleccionada == "8":
            ejecutar_mostrar_pga_promedio()           
        elif opcion_seleccionada == "9":
            ejecutar_mostrar_puestos_estudios_dirigidos()            
        elif opcion_seleccionada == "10":
            continuar = False
        else:
            print("Por favor seleccione una opcion valida.")

#PROGRAMA PRINCIPAL
iniciar_aplicacion()