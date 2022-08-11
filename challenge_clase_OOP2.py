# Ejercicio de creacion de objetos del modulo clase_OOP2mails.py
# 1. Crear cartas (5)
# 2. Agragar cartas a sobres
# 3. Agregar sobre el buzon
# 4. Sacar uana carta del buzon
# 5. Leer buzon completo

class Carta:
	mensaje: ''
	tipo_papel = ''
	carta_count = 0

	def write_letter(self, message):
		print(f'Escribiendo el mensaje: {message}')
		self.mensaje = message

		self.carta_count += 1
		print(f'Vamos en la carta: {self.carta_count}')
			


tipo_papel = input('Que tipo de papel quieres utilizar para la carta: ')
mensaje = input('Escribe lo que quieres que diga la carta: ')

la_letter = Carta()
print(la_letter)
la_letter.write_letter(mensaje)