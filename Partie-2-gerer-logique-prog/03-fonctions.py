
 
    
# Définissez une fonction

## Utilisez une fonction sans paramètres


# On definit la fonction qui  s'appelle  afficher_message  
# et ne prend aucun paramètre en entrée, . 
# Elle n'a pas de valeur de retour car elle se contente d'afficher un message à l'écran en utilisant la fonction  print()  .


def afficher_message():
   print("Bonjour, comment ça va ?")

# on appelle cette fonction 
afficher_message()

##  Utilisez une fonction avec paramètres

# On peut également créer une fonction avec des paramètres, 
# qui permettent de transmettre des valeurs à la fonction. 
# Les paramètres sont simplement listés entre parenthèses, séparés par des virgules.
# Voici un exemple d'une fonction qui prend deux paramètres, un nom et un prénom, et qui les affiche ensuite.


def afficher_nom_prenom(nom, prenom):
   print("Nom :", nom)
   print("Prénom :", prenom)


afficher_nom_prenom("Dupont", "Jean")

def calculer_somme(a, b):
    resultat = a + b
    return resultat

somme = calculer_somme(2, 3)

print(somme) #Ce print affichera 5

print(f"La somme de 2 et 3 = {somme} ")
print(f"La somme de 2 et 3 = {calculer_somme(2, 3)} ")

# TODO print("La somme de 2 et 3 = {somme} ") #Ce print affichera 5

 #Utilisez une fonction avec une valeur de retour
# Une fonction avec une valeur de retour est une fonction qui peut prendre des paramètres et effectuer des opérations, 
# mais qui renvoie également une valeur à la fin. Cette valeur peut être utilisée à d'autres endroits du programme. 
# Par exemple, si nous avons une fonction qui calcule la somme de deux nombres, 
#  nous pouvons stocker le résultat dans une variable pour l'utiliser plus tard dans notre programme.
