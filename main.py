from chargeGraphe import chargeGraphe
from glouton1 import glouton1
from glouton2 import glouton2
from gloutonrandom import gloutonrandom
from utils import *
from os import listdir


with open('resultat.txt', 'a') as f:
    for file in listdir('graphes'):
        graphe = chargeGraphe(f'graphes/{file}')
        result = glouton1(graphe)
        cout = coutCouleur(result)
        print(f'Fichier: {file}')
        
        f.write(f'Fichier: {file}\n')
        f.write('Algo 1\n')
        f.write(f'Cout: {cout}, Nombre de couleurs: {len(result)}\n')
        
        result = glouton2(graphe)
        cout = coutCouleur(result)
        f.write('Algo 2\n')
        f.write(f'Cout: {cout}, Nombre de couleurs: {len(result)}\n')
        
        result = gloutonrandom(graphe)
        cout = coutCouleur(result)
        f.write('Algo random\n')
        f.write(f'Cout: {cout}, Nombre de couleurs: {len(result)}\n')