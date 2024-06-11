# Exemple 2 : Développer un programme qui calcule la moyenne et la médiane d'une liste de nombres.

def moyenne(nombres):
  if not nombres:
    return None
  return sum(nombres) / len(nombres)

def mediane(nombres):
  if not nombres:
    return None
  nombres_tries = sorted(nombres)
  longueur = len(nombres_tries)
  milieu = longueur // 2
  if longueur % 2 == 0:
    return (nombres_tries[milieu - 1] + nombres_tries[milieu]) / 2
  else:
    return nombres_tries[milieu]

def main():
  # Fonction principale.
  nombres = []
  while True:
    nombre_str = input("Entrez un nombre (ou vide pour terminer) : ")
    if not nombre_str:
      break
    try:
      nombre = float(nombre_str)
      nombres.append(nombre)
    except ValueError:
      print("Entrée invalide. Veuillez entrer un nombre.")
  if nombres:
    print(f"Moyenne : {moyenne(nombres)}")
    print(f"Médiane : {mediane(nombres)}")
  else:
    print("Aucune donnée entrée.")

if __name__ == "__main__":
  main()
