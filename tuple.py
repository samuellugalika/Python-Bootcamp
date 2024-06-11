# Tuple vide
tuple1 = ()
print(tuple1)
# Tuple avec un élément
tuple2 = (10,)
print(tuple2)
# Tuple avec plusieurs éléments
tuple3 = (5, "Hello", True)
print(tuple3)
# Tuple avec un élément
tuple4 = ("World",)
print(tuple4)
# Tuple avec plusieurs éléments
tuple5 = 5, "Bonjour", 3.5
print(tuple5)
# acces aux elements du tuple
tuple3 = (5, "Hello", True)
# Accéder au premier élément
element1 = tuple3[0]  # element1 = 5
print(element1)
# Accéder au dernier élément
element2 = tuple3[-1]  # element2 = True
print(element2)
# Accéder à une plage d'éléments
sous_tuple = tuple3[1:3]  # sous_tuple = ("Hello", True)
print(sous_tuple)