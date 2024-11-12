from utils import *

def glouton2(graphe):
    grapheResultat = [[]]
    candidatsList = [i for i in range(len(graphe))]
    currentColor = 0
    
    while candidatsList != []:
        
        candidats = [candidat for candidat in candidatsList if coloriableWithColor(candidat, graphe, grapheResultat, currentColor)]
        if len(candidats) == 0:
            currentColor += 1
            continue
        
        selectedCandidat = [candidats[0]]
       
        for candidat in candidats:
            if len(alphaVNonColoriableWithColor(candidat, graphe, grapheResultat, currentColor)) > \
            len(alphaVNonColoriableWithColor(selectedCandidat[0], graphe, grapheResultat, currentColor)):
                selectedCandidat = [candidat]
            elif len(alphaVNonColoriableWithColor(candidat, graphe, grapheResultat, currentColor)) == \
            len(alphaVNonColoriableWithColor(selectedCandidat[0], graphe, grapheResultat, currentColor)):
                selectedCandidat.append(candidat)
                
        selectedCandidatFinal = selectedCandidat[0]
        
        for candidat in selectedCandidat:
            if len(alphaVColoriableWithColor(candidat, graphe, grapheResultat, currentColor)) < \
                len(alphaVColoriableWithColor(selectedCandidatFinal, graphe, grapheResultat, currentColor)):
                selectedCandidatFinal = candidat
                
        grapheResultat = colorier(selectedCandidatFinal, graphe, grapheResultat)
        candidatsList.remove(selectedCandidatFinal)
                        
        percent_complete = (len(graphe) - len(candidatsList)) / len(graphe) * 100
        print(f'Progress: {percent_complete:.2f}%')
        
    return grapheResultat