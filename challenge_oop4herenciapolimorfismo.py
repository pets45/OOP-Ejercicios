# Challenge hacer ejemplos de herencia y polimorfismo

class Sport_Player:
	sport = ''

	def __init__(self, sport, is_active=True):
		self.sport = sport

	def play(self):
		print(f'\nEl deportista practica {self.sport}')

	def is_active(self):
		print(f'The sport player from the sport {self.sport} is active and is in shape')


class Basketball_Player(Sport_Player): 
	name = ''
	number = 0
	is_tall = False

	def __init__(self, name, number,is_tall=True):
		self.name = name
		self.number = number
		self.is_tall = is_tall

	def dunk(self):
		print(f'Player number {self.number} is tall {self.is_tall} and can dunk the ball')

	def shoot_three(self):
		print(f'The basketball player {self.name} can shoot from the three point line')

	def is_active(self):
		super().is_active()
		print(f'The basketball player number {self.number} is in good shape')


class Swimmer(Sport_Player):
	name = ''
	nationality = ''

	def __init__(self, name, nationality):
		self.name = name
		self.nationality = nationality

	def swim(self):
		print(f'The swimmer {self.name} knows how to swim')

	def croll(self):
		print(f'The swimmer from {self.nationality} is swimming croll type')

	def is_active(self):
		super().is_active()
		print(f'This swimmer is being active since he was 18 years old')


basketball_sport = Sport_Player('basketball')
basketball_sport.play()
basketball_sport.is_active()

baloncesto_player = Basketball_Player('jordan', 23, True)
baloncesto_player.dunk()
baloncesto_player.shoot_three()
baloncesto_player.is_active()

nadador = Swimmer('aquaman', 'mexico')
nadador.swim()
nadador.croll()
nadador.is_active()




