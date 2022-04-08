# Les packages du pythagore
import math
import matplotlib.pyplot as plt

# Requete
Requete = input("Voulez vous calculez le pythagore ou crée le graphique ? Calcul/Perimetre/Graphique : ")

# Les calculs du pythagore
if Requete == "Calcul":
    AC = input("Entrées une valeur : ")
    AB = input("Entrées une valeur : ")
    Hypo = pow(int(AC),2) + pow(int(AB),2)
    print(Hypo)
    
elif Requete == "Perimetre":
    A = input("Entrées une valeur : ")
    B = input("Entrées une valeur : ")
    C = input("Entrées une valeur : ")
    Perimetre = int(A) + int(B) + int(C)
    print(Perimetre)

elif Requete == "Graphique":
    A = input("Entrées une valeur : ")
    B = input("Entrées une valeur : ")
    C = input("Entrées une valeur : ")
    #plt.plot([AC, -AB], [AB, -AC])
    x = [A, 0, 0, B]
    y = [0, A, 0, B]
    plt.plot(x, y)
    plt.ylabel('Test')
    plt.show()