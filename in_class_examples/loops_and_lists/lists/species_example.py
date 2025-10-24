species_1 = ["capybara", "mammal", 4, True]
species_2 = ["monitor lizard", "reptile", 4, True]
species_3 = ["chimpanzee", "mammal", 2, True]
species_4 = ["velociraptor", "reptile", 2, False]


species_data = [species_1, species_2, species_3, species_4]
print(f"original species_data: {species_data}")
#print(species_data[2])
#print(species_data[2][0])
#print(species_data[2][0][0])

for species_details in species_data:
    print(f"The species {species_details[0]} walks on {species_details[2]} legs!")