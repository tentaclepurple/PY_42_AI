def get_vector(a, b):
	"""		crea una lista de listas con floats (un vector columna)
			lista de comprension equivale a:
			self.values = []
			for i in range(0, values + 1):
				self.values.append([float(i)])
	"""
	return [[float(i)] for i in range(a, b)]

class Vector:
	def __init__(self, values):
		"""
			inicializar vector values y shape segun se reciba el parametro en forma de:
			tamaño: (3)
			rango: (1, 4) 
			vector fila
			vector columna
			se usa all() y comprensiones de lista para verificar las instancias los contenidos de las listas recibidas
		"""
		if isinstance(values, int) and values > 0:
			self.values = get_vector(0, values + 1)
			self.shape = (len(self.values), 1)		
		elif isinstance(values, tuple) and all(isinstance(element, int) for element in values) and values[0] < values[1]:
			self.values = get_vector(values[0], values[1])
			self.shape = (len(self.values), 1)
		elif isinstance(values, list) and all(isinstance(element, float) for element in values):
			self.values = values
			self.shape = (1, len(self.values))
		elif isinstance(values, list) and all(isinstance(sublist, list) and len(sublist) == 1 and isinstance(sublist[0], float) for sublist in values):
			self.values = values
			self.shape = (len(self.values), 1)
		else:
			print("Invalid input")
			return

	def __str__(self):
		return f"Vector({self.values})"
	def __repr__(self):
		return str(self)
	def dot(self, v):
		if isinstance(v, Vector) and self.shape == v.shape:
			if self.shape[0] == 1:
				result = sum([self.values[i] * v.values[i] for i in range(len(self.values))])
			elif self.shape[1] == 1:
				result = sum([self.values[i][0] * v.values[i][0] for i in range(len(self.values))])
		else:
			print("Shapes don´t match. Dot product failed.")
		return result
	def T(self):
		if self.shape[0] == 1:
			""" 
				es lo mismo que:
				result = []
        		for i in self.value:
            		result.append([i])
			"""
			result = [[i] for i in self.values]
			return Vector(result)  #aqui devuelve una instancia de Vector en vez de solamente un lista
		elif self.shape[1] == 1:
			result = [sublist[0] for sublist in self.values]
			return Vector(result)		
	def __add__(self, v):
		if isinstance(self, Vector) and isinstance(v, Vector):
			if self.shape == v.shape:
				if isinstance(self.values[0], float) and isinstance(v.values[0], float):
					result = [self.values[i] + v.values[i] for i in range(len(self.values))]	
				elif isinstance(self.values[0], list) and isinstance(v.values[0], list):
					result = [[self.values[i][0] + v.values[i][0]] for i in range(len(self.values))]
				else:
					print("Vector shapes don´t match")
					return
			else:
				print("Vector shapes don´t match")
				return
			return Vector(result)
		else:
			print("Add only possible between vectors")
			return
	
	def __radd__(self, v):
		return self.__add__(v)

	def __sub__(self, v):
		if isinstance(self, Vector) and isinstance(v, Vector):
			if self.shape == v.shape:
				if isinstance(self.values[0], float) and isinstance(v.values[0], float):
					result = [self.values[i] - v.values[i] for i in range(len(self.values))]	
				elif isinstance(self.values[0], list) and isinstance(v.values[0], list):
					result = [[self.values[i][0] - v.values[i][0]] for i in range(len(self.values))]
				else:
					print("Vector shapes don´t match")
					return
			else:
				print("Vector shapes don´t match")
				return
			return Vector(result)
		else:
			print("Substract only possible between vectors")
	
	def __rsub__(self, v):
		return self.__sub__(v)

	def __truediv__(self, b):
		if isinstance(self, Vector) and isinstance(b, (int, float)):
			try:
				if b == 0:
					raise ZeroDivisionError
				if isinstance(self.values[0], float):
					result = [self.values[i] / b for i in range(len(self.values))]
				elif isinstance(self.values[0], list):
					result = [[self.values[i][0]] for i in range(len(self.values))]
			except ZeroDivisionError:
				print("ZeroDivisionError: division by zero.")
				return
			return Vector(result)
		else:
			print("Division not possible")
			return
		
	def __rtruediv__(self, b):
		try:
			raise NotImplementedError
		except NotImplementedError:
			print("NotImplementedError: Division of a scalar by a Vector is not defined here.")
			return

	def __mul__(self, b):
		if isinstance(self, Vector) and isinstance(b, (float, int)):
			if isinstance(self.values[0], float):
				result = [self.values[i] * b for i in range(len(self.values))]
			elif isinstance(self.values[0], list):
				result = [[self.values[i][0] * b] for i in range(len(self.values))]
			return Vector(result)
		else:
			print("Multiplication not posible. Must be a vector and a scalar")
	
	def __rmul__(self, b):
		return self.__mul__(b)

			



