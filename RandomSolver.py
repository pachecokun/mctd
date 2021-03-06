from Equation import Equation
from LinearProblem import LinearProblem
import random
import itertools

class RandomSolver():

	global VECTORS
	VECTORS = 100
	global ITERATIONS
	ITERATIONS = 100	
			
	@staticmethod
	def solve(lp):
	
	
		#Encontrar valores limite de las variables
		randLimits = []
		for i in range(0, lp.nvars):
			minVal = -100
			maxVal = 100
			possibleValues = []
			for eq in lp.conditions:
				l = eq.getLimits()[i]
				if l is not None:
					if eq.ctype == Equation.LESS_EQUAL:
						maxVal = min(l,maxVal)
					elif eq.ctype == Equation.GREATER_EQUAL:
						minVal = max(l,minVal)
			randLimits.append((minVal,maxVal))
		print randLimits
		
		pMax = None
		pMin = None
		vMax = None
		vMin = None
		zFinal = None
		vFinal = None
		itMax = None
		itMin = None
		#inicia iteracion
		for i in range (0, ITERATIONS):
			vectors = []
			iterationValues = []
			iterationResults = []
			
			
			for j in range (0, VECTORS):
				#inicializamos el vector con valores aleatorios
				v = []
				for k in range(0, lp.nvars):
					v.append(randLimits[k][0]+random.random()*float(randLimits[k][1]-randLimits[k][0]))
				
				#print v
				
				#evaluamos que el valor cumpla las condiciones
				valid = True
				for eq in lp.conditions:
					valid = valid and eq.isValid(v)
				
				#Si las cumple, agregamos el valor a las condiciones
				if valid:
					iterationValues.append(v)
					iterationResults.append(lp.z.value(v))
					
			if iterationResults:
				itMax = max(iterationResults)
				itMin = min(iterationResults)				

			if itMax:
				if pMax is None:
					pMax = itMax
					vMax = iterationValues[iterationResults.index(pMax)]
				elif itMax > pMax:
					pMax = itMax
					vMax = iterationValues[iterationResults.index(pMax)]
			if itMin:
				if pMin is None:
					pMin = itMin
					vMin = iterationValues[iterationResults.index(pMin)]
				elif itMin < pMin:
					pMin = itMin
					vMin = iterationValues[iterationResults.index(pMin)]

		if lp.ptype == LinearProblem.MIN:
			zFinal = pMin
			vFinal = vMin
		else:
			zFinal = pMax
			vFinal = vMax
		
		return vFinal, zFinal

#prueba
"""
problem = LinearProblem(
	Equation([50,65]), #Funcion objetivo
	[
		Equation([20,15],Equation.LESS_EQUAL,450),  #Condiciones
		Equation([2,2],Equation.LESS_EQUAL,54),
		Equation([6,0],Equation.LESS_EQUAL,120),
		Equation([0,8],Equation.LESS_EQUAL,180),
		Equation([1,0],Equation.GREATER_EQUAL,0),
		Equation([0,1],Equation.GREATER_EQUAL,0)
	],
	LinearProblem.MAX #tipo de problema
)

print AnalyticSolver.solve(problem)
print RandomSolver.solve(problem) #devuelve punto y valor
"""

