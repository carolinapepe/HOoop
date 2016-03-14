import matplotlib.pyplot as pp
import numpy as np
"""
Define el similador del Radar
"""


class Radar(object):


    def __init__(self, generador, detector):
        self.generador = generador
        self.detector = detector


    def detectar(self, medio, tiempo_inicial, tiempo_final):

        """
        Detecta si hay un blanco en un medio, en un intervalo de tiempo.
        """
        
        una_senal = self.generador.generar(tiempo_inicial, tiempo_final)
        
        tiempoInicialSegundos = tiempo_inicial.hour*3600+tiempo_inicial.minute*60+tiempo_inicial.second
	tiempoFinalSegundos = tiempo_final.hour * 3600 + tiempo_final.minute * 60 + tiempo_final.second
	tiempos = np.linspace(tiempoInicialSegundos, tiempoFinalSegundos, len(una_senal))

        self.plotear_senal(una_senal, tiempos)
	
        una_senal_reflejada = medio.reflejar(una_senal, tiempo_inicial, \
        tiempo_final)
	
        senal_detectada =  self.detector.detectar(una_senal_reflejada)
        self.plotear_senal_detectada(senal_detectada, tiempos)
        
        
        return senal_detectada
        

    #TODO agregar el metodo plotear_senal
    
    def plotear_senal(self, senial, tiempos):
	
	pp.figure()
	pp.plot(tiempos, senial, color='r',label='Signal VS')
	pp.ylabel('Amplitude')
	pp.grid(True)
	pp.xlabel('time (s)')
	pp.title('Senial generada')
	pp.draw()
	
    def plotear_senal_detectada(self, senial, tiempos):
	
	pp.figure()
	pp.plot(tiempos, senial, color='r',label='Signal VS')
	pp.ylabel('Amplitude')
	pp.grid(True)
	pp.xlabel('time (s)')
	pp.title('Senial detectada')
	pp.show()    
	
