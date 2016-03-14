import matplotlib.pyplot as pp
import numpy as np

class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        #TODO: completar con la inicializacion de los parametros del objeto
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

    def reflejar(self, senal, tiempo_inicial, tiempo_final):

        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
	senial_reflejada = [0]*len(senal)
	
	#defino los tiempos de generacion de la senial
	tiempoInicialSegundos = tiempo_inicial.hour*3600+tiempo_inicial.minute*60+tiempo_inicial.second
	tiempoFinalSegundos = tiempo_final.hour * 3600 + tiempo_final.minute * 60 + tiempo_final.second

	tiempos = np.linspace(tiempoInicialSegundos, tiempoFinalSegundos, len(senal))
	
	#defino los tiempos de existencia del blanco
	tiempoInicialSegundos = self.tiempo_inicial.hour*3600+self.tiempo_inicial.minute*60+self.tiempo_inicial.second
	tiempoFinalSegundos = self.tiempo_final.hour * 3600 + self.tiempo_final.minute * 60 + self.tiempo_final.second

	senal_array = np.asarray(senal)

	if tiempo_inicial <= self.tiempo_inicial <= tiempo_final or self.tiempo_inicial <= tiempo_inicial <= self.tiempo_final:
	  for index, tiempo in enumerate(tiempos):
	    if tiempoInicialSegundos <= tiempo and tiempo <= tiempoFinalSegundos:
     	      senial_reflejada.pop(index)
     	      senial_reflejada.insert(index, float(senal_array[index])/2.)

	      
	
	pp.figure()
	pp.plot(tiempos, senial_reflejada, color='r',label='Signal VS')
	pp.ylabel('Amplitude')
	pp.grid(True)
	pp.xlabel('Time (s)')
	pp.title('Senial reflejada')
	pp.draw()

        return senial_reflejada
        
