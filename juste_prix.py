from random import randint #importe la finction randint pour générer un entier dans une range donnée
le_juste_prix = randint(1, 1000) #définit la valeur du juste prix
essais = 0 #initialise une variable qui comptes le nombre de tantatives
tant = 0 #initialise la variable tantative du joueur a zero afin que la boucle se lance (sachant que le juste prix ne peut pas etre 0)
while tant != le_juste_prix: #recommence les operation dessous jusqua ce que le joueur trouve le juste prix
    tant = int(input("trouve le juste prix entre 1 et 1000€")) #tant que le juste prix n'est pas trouver la question est poser, il est donc possible d'actualiser la valeur
    if tant < le_juste_prix: #couple de condition afin d'aider le joueur a trouver le juste prix
        print("c'est plus !")
    elif tant > le_juste_prix:
        print("c'est moin !")
    essais += 1 #augmente le nombre de tentatvies de 1 si les conditions ne sont pas remplis, donc que le joueur se trompe.
print("gg mek, le juste pris était bien {}€".format(le_juste_prix)) #2 print pour annoncer le resultat
print("tu l'as trouver en {} tentatives".format(essais))
quit() #quite le programe