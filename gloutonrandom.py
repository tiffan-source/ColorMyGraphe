from utils import *

def gloutonrandom(graphe):
    grapheResultat = [[]]
    candidatsList = [i for i in range(len(graphe))]
    
    for candidat in candidatsList:
        grapheResultat = colorierRandom(candidat, graphe, grapheResultat)
        pourcentage = (candidatsList.index(candidat) + 1) / len(candidatsList) * 100
        print(f"Percentage done: {pourcentage:.2f}%")
        

    return grapheResultat