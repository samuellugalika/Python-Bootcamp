from collections import deque

nombres_premiers = deque([1, 3, 5, 7])
# Ajouter les éléments au dernière index de la liste
nombres_premiers.append(11)
print(nombres_premiers)
nombres_premiers.append(13)
print(nombres_premiers)
# sorti des permiers éléments de la liste
nombres_premiers.popleft()
print(nombres_premiers)
nombres_premiers.popleft()
print(nombres_premiers)
nombres_premiers.popleft()
print(nombres_premiers)