class Plant:
	def __init__(self, species):
		self.species = species
		self.height = 0
		#print(f"In __init__: {self}")

	def grow(self, amount):
		self.height += amount

	def print_info(self):
		print(f'Species: {self.species}')
		print(f'Height: {self.height} inches')


plant_1 = Plant('poppy')
plant_1.grow(5)
plant_1.print_info()
plant_1.grow(10)
plant_1.print_info()
plant_1.species = 'hi'
plant_1.print_info()
plant_1.name = 'jake'
print(plant_1.name)

#plant_2 = Plant('akdhjsf;kasdfhjo')
#print(plant_2.name)

#print("Printing plant_1 at the bottom")
#print(plant_1)