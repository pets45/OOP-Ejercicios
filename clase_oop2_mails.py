class Letter:
	content = ''

	def __init__(self, content):
		self.content = content

	def fold(self):
		pass

	def __str__(self):
		return self.content

class Envelope:
	content = None
	is_open = False

	def open(self):
		self.is_open = True

	def close(self):
		self.close = False

	def append(self, content):
		if self.is_open:
			if not self.content:
				self.content = content
			else:
				print('Ya tiene correo')
		else:
			print('Aaabrela papa!')


	def __str__(self):
		return self.content

class Inbox:
	envelopes = []
	is_open = True

	def open(self):
		self.is_open = True

	def close(self):
		self.is_open = False

	def add(self,envelope):
		if self.is_open:
			self.envelopes.append(envelope)
			print('Se guardo el sobre')

	def read(self):
		if self.is_open:
			print('Leyendo el ultimo correo que llego....')
			envelope = self.envelopes.pop()
			return envelope

	def read_all(self):
		inbox_size = len(self.envelopes)
		for i in range(inbox_size):
			print(f'\nRecuperando sobre {i + 1}')
			envelope = self.envelopes.get(i)
			print(envelope)