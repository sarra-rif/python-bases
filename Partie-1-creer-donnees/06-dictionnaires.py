
# **Enregistrez des données complexes avec des dictionnaires**


### **Qu’est-ce qu’un dictionnaire ?**

"""
    Parfois vous avez besoin de représenter des données plus complexes que des nombres, des chaînes ou des listes.


    Un dictionnaire est une structure de données qui enregistre des données dans des **paires clés-valeurs**. Voici un exemple d’une clé et d’une valeur :  



"responsable_de_campagne": "Jeanne d'Arc"




    La **clé** est   `"responsable_de_campagne"`  et la **valeur** est   `"Jeanne d'Arc"`  .** **

"""
### **Créez un dictionnaire**


# On peut sauvegarder un dictionnaire comme ça :



nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}



"""  Vous pouvez aussi créer un nouveau dictionnaire avec des accolades vides  `{}`  ou la fonction  `dict()`  ,
et avec des paires clés-valeurs comme indiqué ci-dessous :

"""

taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

taux_de_conversion2 = dict()
taux_de_conversion2['facebook'] = 3.4
taux_de_conversion2['instagram'] = 1.2




### **Accédez à une valeur dans un dictionnaire**


# Pour accéder aux différentes valeurs, vous pouvez utiliser la clé pour chacune des paires clés-valeurs.



nouvelle_campagne['responsable_de_campagne']
taux_de_conversion['facebook']




### **Réalisez des opérations courantes avec les dictionnaires**


#### **Ajoutez une paire clé-valeur**

"""
    Le code suivant crée un dictionnaire appelé   `infos_labradoodle`  ,
    et enregistre des informations à propos du poids et de l’origine des labradoodles, un croisement de chiens.

"""

infos_labradoodle = {
   "poids": "13 à 16 kg",
   "origine": "États-Unis"
}



"""
    Pour ajouter une nouvelle paire clé-valeur, comme le nom scientifique du labradoodle, ajoutez simplement :

"""

infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris"



"""
    Maintenant,   `infos_labradoodle`  renvoie :

"""

print(infos_labradoodle)



"""
    Si vous écrivez   `infos_labradoodle["poids"] = "45 kg"`  , la valeur existante sera écrasée, et le résultat sera donc :

"""

infos_labradoodle["poids"]
"45 kg"




#### **Supprimez une paire clé-valeur**

"""
    Pour supprimer une paire clé-valeur, vous pouvez utiliser le mot-clé  `del`  et la clé que vous voulez supprimer, ou encore la méthode   `pop`  . Pour supprimer la paire clé-valeur  `"origine"`  de la paire  `clé-valeur`  , écrivez :

"""

del infos_labradoodle["origine"]
print(infos_labradoodle)
"""
{ "poids": "13 à 16 kg",
"nom_scientifique": "Canis lupus familiaris"}

    Certains mots font partie du langage Python, et ne peuvent pas être utilisés comme noms de variables. Par exemple, **<code>del</code>  </strong>, <strong><code>if</code>  </strong>et <strong><code>else</code>  </strong>. Ces mots sont connus comme étant des <strong>mots réservés</strong> ou des <strong>mots-clés</strong>.<strong> </strong>


    Voici encore quelques méthodes couramment utilisées pour manipuler des dictionnaires :
"""


#### **Vérifiez l’existence d’une clé spécifique**

"""
    Par exemple, si vous voulez voir si la clé « poids » existe dans votre dictionnaire   `infos_labradoodle`  , écrivez le code qui suit : 

"""

"poids" in infos_labradoodle
True
"race" in infos_labradoodle
False




### **À vous de jouer ! **

"""
    Maintenant que vous vous êtes familiarisé avec quelques opérations, [pratiquez la manipulation de dictionnaire](https://replit.com/team/PythonBasics2-5/Enregistrez-des-donnees-avec-dictionnaires-Exercice-1) en utilisant toutes les méthodes vues précédemment. 😁


    Si vous n’arrivez pas à accéder aux exercices, vérifiez que vous avez bien suivi les **[instructions de connexion](https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python?status=draft)** tout au début du cours. 


### **En résumé**



* Un **dictionnaire **est un moyen d’enregistrer des **paires clés-valeurs** qui représentent un objet plus grand.
* Vous pouvez créer un dictionnaire avec des **accolades `{}`**  , et y mettre toutes les clés-valeurs dès le début, ou les ajouter au fur et à mesure.
* Chaque clé dans un dictionnaire doit être **unique.**
"""

### **Résumé de la partie 1**

"""
    Félicitations ! Vous avez atteint la fin de la partie 1 du cours, et vous pouvez maintenant créer des données, les blocs de code de base du code Python. Vous avez déjà fait beaucoup !



* Vous avez utilisé des **variables** pour enregistrer des informations comme **données** dans le code Python.
* Vous avez utilisé des **types de données** pour classer différents types de données : les entiers, les virgules flottantes, les chaînes de caractères et les booléens.
* Vous avez utilisé des **listes** et des **tuples** pour enregistrer des données qui sont liées.  
* Vous avez utilisé des **dictionnaires** pour enregistrer des données complexes.

    _Vous êtes bien parti pour devenir développeur Python ! Maintenant c’est le moment de tester vos connaissances sur la création de données dans Python ! Vous allez passer un quiz. _


    _Ensuite, dans la partie 2, vous allez apprendre à gérer la logique du programme._
"""