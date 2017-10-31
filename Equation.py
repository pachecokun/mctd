import numpy as np

class Equation():

	#Constantes de tipo de ecuacion
	LESS = 1
	LESS_EQUAL = 2
	EQUAL = 3
	GREATER_EQUAL = 4
	GREATER = 5

	"""
		Constructor
		Entradas: 
			coeficientes de ecuacion: lista de numeros
			tipo de ecuacion: alguna de las constantes de arriba (default =)
			valor de lado dereho de ecuacion: numero (default 0)
	"""
	def __init__(self,coeficients,ctype=3,limit=0):
		self.coeficients = coeficients
		self.ctype = ctype
		self.limit = limit

	"""
		Devuelve el valor de la ecuacion en un punto
		Entradas:
			punto: numpy.array
		Salida
			valor: numero
	"""
	def value(self,point):
		return np.dot(point,self.coeficients)

	"""
		Devuelve si un punto pertenece a la ecuacion
		Entradas:
			punto: numpy.array
		Salida
			es_valido: booleano
	"""
	def isValid(self,point):
		val = self.value(point)

		isValid = True

		if self.ctype == self.LESS:
			return val < self.limit
		if self.ctype == self.LESS_EQUAL:
			return val <= self.limit
		if self.ctype == self.EQUAL:
			return val == self.limit
		if self.ctype == self.GREATER_EQUAL:
			return val >= self.limit
		if self.ctype == self.GREATER:
			return val > self.limit

	"""
		Encuentra las intersectiones de varias ecuaciones
		Si no encuentra la interseccion devuelve None
	"""
	@staticmethod
	def intersection(conditions):
		m = []
		v = []
		for c in conditions:
			m.append(c.coeficients)
			v.append(c.limit)
		try:
			return np.dot(np.linalg.inv(m),v)
		except:
			return None

	"""
		Convierte a cadena la ecuacion
	"""
	def __str__(self):
		return "--"+str(self.coeficients)+", "+str(self.ctype)+", "+str(self.limit)+"--"
	__repr__ = __str__


