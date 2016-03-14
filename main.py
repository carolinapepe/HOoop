#!/usr/bin/env python

import radar
import medio
import blanco
import generador
import datetime
import detector
import matplotlib.pyplot as pp


# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)

    #tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    #tiempo_final = datetime.datetime(2016, 3, 5, 1, 10)

    import math
    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    #TODO construir un nuevo genrador de senales
    un_generador = generador.Generador(amplitud, fase, frecuencia)
    

    #TODO construir un detector
    un_detector = detector.Detector()
    
    #TODO construir un nuevo radar
    un_radar = radar.Radar(un_generador, un_detector)

    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    #tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 1, 5)
    #tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 1, 7)
  
    #TODO contruir un nuevo blanco
    un_blanco = blanco.Blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco, tiempo_final_del_blanco)

    #TODO contruir un medio
    un_medio = medio.Medio(un_blanco)

    #TODO detectar la senial
    
    senial_detectada = un_radar.detectar(un_medio, tiempo_inicial, tiempo_final)

if __name__ == "__main__":
    main()
