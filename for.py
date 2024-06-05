# Boucle FOR 

fruits = {"Banane" : 100, "ananas" : 250, "orange" : 150 }
total = 0

for fruit, prix in fruits.items():
      print(f"Le prix de {fruit} est {prix} Fc")
      total += prix
      
print(f"Le coût total est {total} Fc")

#python_bootcamp_GDSC_UCB