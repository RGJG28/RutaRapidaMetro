# -*- coding: utf-8 -*-
"""
13-08-2021

@author: RGJG
"""
import pandas as pd
import numpy as np
import matplotlib 
import networkx as nx
import os
def menu():
    print('PROGRAMA QUE DA LA RUTA MAS CORTA EN EL METRO DE LA CDMX')
    print('________________________________________________________')
    print('*Debes ingresar los nombres de las estaciones empezando con mayuscula la primera letra e incluyendo acentos*')
    print('______________________MENÚ______________________________')
    print('1.Ver las estaciones del metro')
    print('2.Ver las aristas de las estaciones del metro')
    print('3.Ver el numero de estaciones sin repeticion')
    print('4.Ver las estaciones que conectan a otras lineas')
    print('5.Ver la ruta mas corta')
    print('6.Ver el grafo de la ruta mas corta')
    print('7.Ver la distancia recorrida en interestaciones')
    print('8.Salir')
    print('________________________________________________________')

    
#SE IMPORTAN LOS DATOS Y SE CONVIERTEN EN UN DATAFRAME
df = pd.read_excel('metro.xlsx')
# los datos se importaron correctamente
df.head()
#SE GENERA EL GRAFO A PARTIR DE LOS DATOS
METRO = nx.from_pandas_edgelist(df,source='Origen',target='Destino',edge_attr='Longitud de interestación')

while True:
    menu()
    opcion=int(input('Ingresa el numero de la opción que deseas ejecutar: '))
    if opcion==1:
        os.system("cls")
        #IMPRIME LOS VERTICES DEL GRAFO 
        print('Las estaciones del metro son:')
        print(METRO.nodes())
    elif opcion==2:
        os.system("cls")
        #IMPRIME LAS ARISTAS ENTRE CADA ESTACION/NODO
        print('\nLas aristas entre cada estacion del metro son:')
        print(METRO.edges())
    elif opcion==3:
        os.system("cls")
        #IMPRIME EL NUMERO DE ESTACIONES
        #solo muestra 163 de las 195 estacuiones ya que no se contempla para el conteo el numero de repeticiones
        print("La red del metro de la CDMX tiene",METRO.order(),"estaciones, sin repetición")
    elif opcion==4:
        os.system("cls")
        #Estaciones que pertenecen a mas de una linea
        print("Las estaciones que conectan con alguna otra linea son: ")
        for i in METRO.nodes():
            if METRO.degree(i)>2:
                print (i)
    elif opcion==5:
        os.system("cls")
        origen=input(str('Ingresa la estacion desde la que vas a iniciar el viaje: '))
        destino=input(str('Ingresa la estacion destino: '))
        djk_path= nx.dijkstra_path(METRO, source=origen, target=destino, weight='Longitud de interestación')
        #NUMERO DE ESTACIONES RECORRIDAS
        num_estaciones=len(djk_path)
        #IMPRESION DELA RUTA 
        print("\nLa ruta mas corta para llegar desde ", origen, "hasta", destino, "es la siguiente: ")
        for i in range(num_estaciones):
            print("Estación número", i+1,":",djk_path[i] )
        print("Tu ruta pasa por", num_estaciones,"estaciones. ¡Buen viaje!")
    elif opcion==6:
        os.system("cls")
        print("\nDEBES FINALIZAR EL PROGRAMA PARA VER EL GRAFO\n")
        ruta=METRO.subgraph(djk_path)
        nx.draw(ruta,with_labels=True)
        matplotlib.pyplot.savefig("Graph.png", format="PNG",dpi=300, bbox_inches='tight')

    elif opcion==7:
        os.system("cls")
        distancia=nx.dijkstra_path_length(METRO, origen, destino, 'Longitud de interestación')
        print("La distancia recorrida en estaciones fue de:",distancia,"metros")
    elif opcion==8:
        break
    else:
        os.system("cls")
        print('Opcion invalida')









