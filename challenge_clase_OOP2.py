# Ejercicio de creacion de objetos del modulo clase_OOP2mails.py
# 1. Crear cartas (5)
# 2. Agregar cartas a sobres
# 3. Agregar sobres al buzon
# 4. Sacar una carta del buzon
# 5. Leer buzon completo

from clase_OOP2mails import write_letter
from clase_OOP2mails import Envelope
from clase_OOP2mails import Inbox


class Letter:
	content: ''
	tipo_papeles = ''
	carta_count = 0

	def write_letter(self, message):
		for i in range(0, 5):
			content = input(f'Escribe lo que quieres que diga la carta: {message}')
			self.carta_count += 1
			print(f'Vamos en la carta: {self.carta_count}')
			


tipo_papel = input('Que tipo de papel quieres utilizar para la carta: ')
content = input('Mensaje:  ')

la_letter = Letter()
print(la_letter)
la_letter.write_letter(content)

cartas = Letter()
print(cartas)
cartas.__init__()


