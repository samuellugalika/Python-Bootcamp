# definition et appel d'une fonction 
def dire_bonjour():
      print("Bonjour")
dire_bonjour()

# Arguments d'une fonction
def saluer(nom):
      print(f"Bonjour, {nom}")
saluer("Sam")
saluer("Jean")

# Valeur de retour : RETURN 
def addition(a,b):
      return a+b
result = addition(4,6)
print(result)

# Arguments par défaut et nommés
def salutation(nom, msg = "Bonjour"):
      print(f"{msg}, {nom}")
salutation("Sam")
salutation("Grace", "Salut")

#python_bootcamp_GDSC_UCB
