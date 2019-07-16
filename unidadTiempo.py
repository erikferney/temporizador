class UnidadTiempo:
	def __init__(self):
		self.valor = 0
		self.tope = 0
		
	def iniciar(self, valor):
		self.valor = valor
	
	def reiniciar(self, valor):
		self.valor = valor
	
	def retroceder(self):
		self.valor -= 1
		
		if self.valor < 0:
			self.reiniciar(self.tope)

class Hora(UnidadTiempo):
	def __init__(self):
		self.valor = 0
		self.tope = 23

class Minuto(UnidadTiempo):
	def __init__(self):
		self.valor = 0
		self.tope = 59

class Segundo(UnidadTiempo):
	def __init__(self):
		self.valor = 0
		self.tope = 59