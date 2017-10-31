from Equation import Equation
from LinearProblem import LinearProblem
import itertools

class AnalyticSolver():

	@staticmethod
	def solve(lp):
		eqs_comb = list(itertools.combinations(lp.conditions,lp.nvars))

		points = []
		values = []

		for eqs in eqs_comb:
			intersection = Equation.intersection(eqs)
			if intersection != None and lp.isValid(intersection):
				points.append(intersection)
				values.append(lp.z.value(intersection))

		if len(points)==0:
			return None

		if lp.ptype == LinearProblem.MIN:
			res = min(values)

		elif lp.ptype == LinearProblem.MAX:
			res = max(values)

		return (list(points[values.index(res)]),res)



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

print AnalyticSolver.solve(problem) #devuelve punto y valor

"""