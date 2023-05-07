"""
Made by Etienne Le Bellec
Programme pour estimer le coût d'une impression 3D.

"""

import os
clear = lambda: os.system('cls') #Permettera de réinitialiser l'affichage

prix_energie = 0.2062   # prix actuel du kWh     ancien prix : 0.1740 / 0.1557
consomation = 0.209     # Kw 
cout_bobine = 20        # kg
taille_bobine = 330     # m
poids_bobine = 1000     # kg


def menu(): # Afficher le menu de séléction
    fin = int
    while (fin != -1):
        print("-1 : Stop")
        print("0 : Une seule pièce")
        print("1 : Plusieurs pièces")
        print("2 : Prix d'un échantillon au poids")
        print("3 : Prix d'un échantillon à la distance")
        fin = int(input("Choisir un nombre : "))
        if fin ==-1:
            print("Fin du programme à bientôt")
        elif fin == 0:
            clear()
            unique()
        elif fin == 1:
            clear()
            multiple()
        elif fin == 2:
            clear()
            poids_echantillon = float(input("Poids de filament à calculer (g) : "))
            print("\n---------------------------------------------------------------------\nLe prix de l'échantillon est de :", round(((cout_bobine*poids_echantillon)/poids_bobine), 2), "€\nSoit une distance de", round(((poids_echantillon*taille_bobine)/poids_bobine), 2), "m\n---------------------------------------------------------------------\n")

        elif fin == 3:
            clear()
            taille_echantillon = float(input("Distance de filament à calculer (m) : "))
            print("\n---------------------------------------------------------------------\nLe prix de l'échantillon est de :", round(((cout_bobine*taille_echantillon)/taille_bobine),2), "€\nSoit un poids de", round(((poids_bobine*taille_echantillon)/taille_bobine), 2), "g\n---------------------------------------------------------------------\n")
        #print("---------------------------------------------------------------------")
            
def unique(): # Calcule le prix d'une seule pièce
    affichage(calcul(saisie()))
     
def saisie(): # Permet de saisir les valeurs puis les renvoies dans un tableau
    
    tab = [0, float, float]
    """
    tab[0] correspond au temps total en minutes
    tab[1] correspond à la distance de filament utilisée
    tab[2] correspond au poids de filament utilisée
    """

    tab[2] = float(input("Poids de l'impression (g) : ")) # On demande le poids de l'impression
    tab[1] = float(input("Distance du filament (m) : "))  # On demande la distance de filment utilisée

    # On demande le temps total de l'impression puis on stocke la réponse dans une chaîne de caractère
    chaine_temps = input("Temps d'impression (Jou Heu Min) : ")
    # Sépare la chaîne de caractère grâce les espaces espace puis renvoie tout sous forme de tableau
    tableau_temps = chaine_temps.split(' ') 

    """ Désormais on travaille sur le tableau : tableau_temps
    On prend le temps total pour le mettre en minutes
    1. On vérifie s'il y a 3 valeurs max dans notre tableau, s'il y en a plus, on les supprimes
    2. Le dernier indice du tableau est forcément le temps en minutes
    3. Si le tableau a une taille de 3 : 
        indice 1 : Jours
        indice 2 : Heures
        indice 3 : Minutes
    4. Si le tableau a une taille de 2 : 
        indice 1 : Heures
        indice 2 : Minutes
    """

    # 2. temps en minutes
    tab[0] += int(tableau_temps[len(tableau_temps)-1])/60 
    
    # 3. si 3 valeurs rentrées
    if len(tableau_temps) == 3:
        tab[0] += int(tableau_temps[1])    # Temps heures
        tab[0] += int(tableau_temps[0])*24 # Temps jours

    # 4. si 2 valeures rentrées
    elif len(tableau_temps) == 2:
        tab[0] += int(tableau_temps[0]) # Temps heures

    return tab

def calcul (tab): # prend le tableau des valeurs, calcule et retourne le tableau de tout les prix
    """
    tab[0] correspond au temps total en minutes
    tab[1] correspond à la distance de filament utilisée
    tab[2] correspond au poids de filament utilisée
    """
    prix_temps = round(consomation*(tab[0])*prix_energie, 2) #tab 0,1,2 respectivement temps en secondes, minutes, heures
    prix_distance = round((cout_bobine*tab[1])/taille_bobine, 2)    #prix à la distance
    prix_poids = round((cout_bobine*tab[2])/poids_bobine, 2)     #prix au poids
    return [prix_temps, prix_distance, prix_poids]

def affichage(tab): # Affiche le prix d'une pièce
    print("")
    print("---------------------------------------------------------------------")
    print("Coût en énergie", tab[0])
    print("Coût en filament à la distance", tab[1],"et au poids", tab[2])
    print("Coût total à la distance", tab[0]+tab[1], "et au poids", tab[0]+tab[2])
    print("---------------------------------------------------------------------")
    print("")

def multiple(): # Calcule le prix de plusieurs pièces
    stop = int() # Notre condition, aurait pu être un booléen
    tab = list() # Tableau qui stockera les informations pour chaques pièces
    i = 0
    while stop != -1:
        tab.append(calcul(saisie()))    # On saisit la pièce
        affichage(tab[i])               # On affiche la pièce précédement saisie
        i += 1
        stop = int(input("Saisir -1 pour finir : "))
    affichageMultiple(tab)           # On affiche la liste de tout les prix des pièces 

def affichageMultiple(tab): # Affiche les résultats de plusieurs pièces
    
    clear()
    sommeEnergie = 0.0
    sommeDistance = 0.0
    sommePoids = 0.0
    i=0

    for i in range (len(tab)) : # On affiche un résumé court de chaque pièce
        print("Coût de la pièce N°", i+1, "coût énergie |", tab[i][0], "| coût filament(distance) |", tab[i][1], "| coût filament(poids) |", tab[i][2])
    
    for e in tab: # On calcule le prix final de l'ensemble des pièces
        sommeEnergie += e[0]
        sommeDistance += e[1]
        sommePoids += e[2]

    print("--------------------------------------------------------------------------------------------------------------------")
    print("Coût Energie : |", sommeEnergie, "| Coût filament(distance) |", sommeDistance, "| Coût filament(poids) |", sommePoids)
    print("Total(distance) |", round(sommeEnergie + sommeDistance, 3))
    print("Total(poids) |", round(sommeEnergie + sommePoids, 3))
    print("--------------------------------------------------------------------------------------------------------------------")
    print("")    
    
clear()    
menu()
