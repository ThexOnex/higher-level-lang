class Interface:
c'est une class contrat qui contient une ensemble de methodes que les class doivent implementer# ABC, doesnt have attributs, no instanciation,only to implement from it not herited from

variable statique:
c'est une variable qui conserve sa valeur et commune a toute la class
@staticmethod ==== className.vairableName

method statique:
c'est une methode n'a pas accee a une instance ou ces attributs, son contenue ne depend pas a l'etat de l'instance

method de class:
c'est une methode qui prend le mot cle CLS en tant que 1er parametre, on peut appeler cette methode a travers une instance ou a travers le nom de la class
@classmethode (cls)
