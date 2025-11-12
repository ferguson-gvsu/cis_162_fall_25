class Plant:
	def __init__(self, species):
		print(f'Species: {species}')
		self.species = species
		self.age = 0
		print(self)
		
	def greet(self):
		print(f"Hello! I am a {self.species}")

plant_1 = Plant("rose")
plant_2 = Plant("bamboo")
plant_1.greet()
print(plant_1.species)
plant_1.name = 'steve'
print(plant_1.name)