class Trabajador:
	name = ''
	no_trabajador = 0
	puesto = ''

	def __init__(self, name, no_trabajador, puesto):
		self.name = name
		self.no_trabajador = no_trabajador
		self.puesto = puesto

	def trabajar(self, tareas):
		print('El trabajador hace sus tareas que son', tareas)

buen_worker = Trabajador('Fulanito', 4513, 'Administrativo')
print(buen_worker)
print(buen_worker.name)
print(buen_worker.no_trabajador)
print(buen_worker.puesto)

tareas = 'enviar correos, tambien contesta llamadas, y hace cheques'

buen_worker.trabajar(tareas)