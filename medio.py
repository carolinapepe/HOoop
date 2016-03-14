class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos


    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
        """
        Los blancos en el medio reflejan la senal
        """

        #TODO reflejar en un medio debe reflejar en todos los blancos de un medio
        #y devolver la senal reflejada
	senial_reflejada = self.blancos.reflejar(una_senal, tiempo_inicial, tiempo_final)
	
	return senial_reflejada
