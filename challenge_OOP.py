# Practicar creando/instanciando objetos

class Perro:
	raza: ''
	size: ''
	pelu: False


	def ladrar(self, ladrido):
		print(f'El perro ladra {ladrido}')

	def __str__(self):
		return f'Perro raza {self.raza}, size: {self.size}, pelu: {self.pelu}'

ladrido = 'uau! uau!'

perrote = Perro()
perrote.raza = 'Griffon Korthal'
perrote.size = 'Mediano'
perrote.pelu = True

print(perrote)
print(perrote.raza)
print(perrote.size)
print(perrote.pelu)

perrote.ladrar(ladrido)