class LinearProblem:

	#Constantes de tipo de problema
	MIN = 0
	MAX = 1

	"""
		Constructor
		Entradas: 
			z: objeto tipo Equation
			conditions: lista de objetos tipo Equation
			tipo de ecuacion: LinearProblem.MIN o LinearProblem.MAX
	"""
	def __init__(self,z,conditions,ptype):
		self.z = z
		self.conditions = conditions
		self.nvars = len(z.coeficients)
		self.ptype = ptype

	"""
		Devuelve si un punto pertenece al area factible
		Entradas:
			punto: numpy.array
		Salida
			es_valido: booleano
	"""
	def isValid(self,p):
		for c in self.conditions:
			if not c.isValid(p):
				return False
		return True
