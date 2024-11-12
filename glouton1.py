from utils import *

def glouton1(graphe):
    grapheResultat = []
    candidatsList = [i for i in range(len(graphe))]
    
    while candidatsList != []:
        candidats = []
        for candidat in candidatsList:
            if len(candidats) == 0:
                candidats.append(candidat)
            elif dsatV(candidat, graphe, grapheResultat) > dsatV(candidats[0], graphe, grapheResultat):
                candidats = [candidat]
            elif dsatV(candidat, graphe, grapheResultat) == dsatV(candidats[0], graphe, grapheResultat):
                candidats.append(candidat)
        
        candidatFinal = candidats[0]
        for candidat in candidats:
            if len(alphaV(candidat, graphe, grapheResultat)) > len(alphaV(candidatFinal, graphe, grapheResultat)):
                candidatFinal = candidat
        
        grapheResultat = colorier(candidatFinal, graphe, grapheResultat)
        
        candidatsList.remove(candidatFinal)
        percent_complete = (len(graphe) - len(candidatsList)) / len(graphe) * 100
        print(f'Progress: {percent_complete:.2f}%')
        
    return grapheResultat