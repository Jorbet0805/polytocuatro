
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

import numpy as np
import os
import time

#import pdb
#poly4pru

def ajuste_geometrico(coordenadas):
     #coordenadas = "79.8985,10.2574,0 79.8473,10.9633,0 79.8526,11.3755,0 79.7555,11.6591,0 79.8696,12.0481,0 80.116,12.4761,0 80.2414,12.8522,0 80.3074,13.3028,0 80.2995,13.4365,0 80.0472,13.5634,0 79.7358,12.6135,0 79.486,11.6118,0 79.6058,10.2699,0 79.8985,10.2574,0"
     coordenadas = coordenadas.strip(' ');
     coordenadas = coordenadas.strip('\t')
     coordenadas = coordenadas.strip('\n')
     coordenadas = coordenadas.strip('\t')
     coordenadas = coordenadas.strip('\n')
     coordenadas = coordenadas.strip('\t')
     coordenadas = coordenadas.strip('\n')
     coordenadas = coordenadas.strip(' '); 

     
     coordenadas = coordenadas.split(" ");
     
     if len(coordenadas) != 5:
     
        coordenadas = [coordenadas[nc].split(",") for nc in range(len(coordenadas))]
        for nc in range(len(coordenadas)):
            coordenadas[nc] = [ float(coordenadas[nc][nc_2]) for nc_2 in range(3) ]
        
        coordenadas = np.array(coordenadas)

        Long_max = coordenadas[:,0].max()  
        Long_min = coordenadas[:,0].min()
        Lat_max = coordenadas[:,1].max()
        Lat_min = coordenadas[:,1].min()
         
        nuevas_coordenadas = [ [ Long_min,Lat_max,0],
                           [ Long_max,Lat_max,0],
                           [ Long_max,Lat_min,0],
                           [ Long_min,Lat_min,0],
                           [ Long_min,Lat_max,0] ]
        
        string_coordenadas = '' 
        
        for nc in range(len(nuevas_coordenadas)):
            for nc_2 in range(3):
                 if nc_2 == len(range(3))-1:
                    string_coordenadas = string_coordenadas + str(nuevas_coordenadas[nc][nc_2]) + ' '
                 else:
                     string_coordenadas = string_coordenadas + str(nuevas_coordenadas[nc][nc_2]) + ','
        
        string_coordenadas = string_coordenadas.strip(' ')   
        return string_coordenadas
     
     else:
         string_coordenadas = '' 
         return string_coordenadas
         

def polytocuatro():

    path_kml =  os.path.join( os.path.dirname ( os.path.abspath(__file__) ) , 'contenedor' )  
    
    #nombre_kml = 'primary-790.kml'
    nombre_kml = input('Introducir el nombre del archivo: ')
    nombre_kml = nombre_kml + ".kml"

    print(path_kml+'\\'+nombre_kml)
    time.sleep(3)

    with open (path_kml+'\\'+nombre_kml,"r") as archivo_kml_original:
         contenido_kml_original = archivo_kml_original.read()
     
    contenido_kml_modificado = contenido_kml_original     
     
    #print(contenido_kml_original)
    # Modificacion de Archivo kml original

    localizacion_inicio = 0
    localizacion_fin = 0
    while  True:
       
           etiqueta_coordenadas_inicio = contenido_kml_original.find('<coordinates>',localizacion_inicio)
           etiqueta_coordenadas_fin = contenido_kml_original.find('</coordinates>',localizacion_fin)
       
           if etiqueta_coordenadas_inicio == -1:
              break
       
           incio_coordenada = etiqueta_coordenadas_inicio+len('<coordinates>')
           fin_coordenada = etiqueta_coordenadas_fin
       
       
           coordenadas = contenido_kml_original [incio_coordenada:fin_coordenada]
       
           string_coordenadas = ajuste_geometrico(coordenadas)
       
           if len(string_coordenadas) > 0: 
              contenido_kml_modificado = contenido_kml_modificado.replace(coordenadas, string_coordenadas)
       
           localizacion_inicio = etiqueta_coordenadas_inicio + 1
           localizacion_fin = etiqueta_coordenadas_fin + 1
       
#print(contenido_kml_modificado)  
    

    print(path_kml+'\\'+'convertido'+'\\'+ nombre_kml+'_modificado.kml')
    time.sleep(3)

    with open (path_kml+'\\'+'convertido'+'\\'+ nombre_kml+'_modificado.kml',"w+") as archivo_kml_modificado:    
         archivo_kml_modificado.write(contenido_kml_modificado)
     
    #print("File one __name__ is set to: {}" .format(__name__))