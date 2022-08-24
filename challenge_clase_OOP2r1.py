# Ejercicio de creacion de objetos del modulo clase_OOP2mails.py
# 1. Crear cartas (5)
# 2. Agregar cartas a sobres
# 3. Agregar sobres al buzon
# 4. Sacar una carta del buzon
# 5. Leer buzon completo

from clase_OOP2mails import Letter, Envelope, Inbox



carta = Letter('recibo_luz')
print(carta)

carta_sobre = Envelope(carta)
carta_sobre.open()
carta_sobre.append(carta)
print(carta_sobre)

sobre_buzon = Inbox(carta_sobre)
sobre_buzon.open()
sobre_buzon.add(carta_sobre)
print(sobre_buzon)

sobre_buzon.read()
print(sobre_buzon)

sobre_buzon.read_all()
print(sobre_buzon)
