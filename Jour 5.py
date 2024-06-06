#Calculatrice basique
def add(a,b):
      return a + b
def sub(a,b):
      return a - b
def mult(a,b):
      return a * b
def div(a,b):
      if b == 0:
            return "Erreur : Division par zero impossible"
      return a / b

def calculatrice():
      print("Calculatrice basique!")
      num1 = float(input("Entrez un nombre : "))
      num2 = float(input("Entrez un nombre : "))
      operation = input("Choissisez une operation : +; -; *; / : ")
      
      if operation == "+" :
            print("Resultat : ", add(num1,num2))
      elif operation == "-" : 
            print("Resultat : ", sub(num1,num2))
      elif operation == "*" : 
            print("Resultat : ", mult(num1,num2))
      elif operation == "/" : 
            print("Resultat : ", div(num1,num2))
      else:
            print("Opération invalide")
            
calculatrice()

#python_bootcamp_GDSC_UCB