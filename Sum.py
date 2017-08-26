class dojo:
	def __init__(self, x, y, s):
		self.menor = x
		self.mayor = y
		self.salto = s
		self.rango = range(menor, mayor, salto)

	def sum(self):
		suma = 0
		for i in self.rango:
			suma += i

		print(suma)
		return suma

print("Ingrese menor")
menor = int(input())

print("Ingrese mayor")
mayor = int(input())

print("Ingrese salto")
salto = int(input())

calcular = dojo(menor, mayor, salto)

print("La suma es: ", calcular.sum())