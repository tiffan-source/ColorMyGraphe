def betaV(sommet, graphe, grapheResultat):
    indices = [index for index, value in enumerate(graphe[sommet]) if value]
    indicesFinal = [i for i in indices if any(i in data for data in grapheResultat)]
    
    return indicesFinal

def alphaV(sommet, graphe, grapheResultat):
    indices = [index for index, value in enumerate(graphe[sommet]) if value]
    indicesFinal = [i for i in indices if all(i not in data for data in grapheResultat)]
    
    return indicesFinal

def alphaVColoriableWithColor(sommet, graphe, grapheResultat, color):
    indiceCandidates = alphaV(sommet, graphe, grapheResultat)
    result = []
    
    if len(indiceCandidates) == 0:
        return result
    else:
        for indiceCandidate in indiceCandidates:
            adjacentToIndiceCandidate = [index for index, value in enumerate(graphe[indiceCandidate]) if value]
            if not any(adjacent in grapheResultat[color] for adjacent in adjacentToIndiceCandidate):
                result.append(indiceCandidate)
        return result

def alphaVNonColoriableWithColor(sommet, graphe, grapheResultat, color):
    indiceCandidates = alphaV(sommet, graphe, grapheResultat)
    indiceCandidatesColoriable = alphaVColoriableWithColor(sommet, graphe, grapheResultat, color)
    result = [i for i in indiceCandidates if i not in indiceCandidatesColoriable]
    return result
    
def dsatV(sommet, graphe, grapheResultat):
    indicesFinal = betaV(sommet, graphe, grapheResultat)
    
    result = 0
    
    for i in grapheResultat:
        if any(indice in i for indice in indicesFinal):
            result += 1
            
    return result

def coloriableWithColor(sommet, graphe, grapheResultat, color):
    indices = [index for index, value in enumerate(graphe[sommet]) if value]
    for i in indices:
        if len(grapheResultat) <= color and i in grapheResultat[color]:
            return False
    return True

def colorier(sommet, graphe, grapheResultat):
    indices = [index for index, value in enumerate(graphe[sommet]) if value]
    for grapheColor in grapheResultat:
        if all(i not in grapheColor for i in indices):
            grapheColor.append(sommet)
            return grapheResultat
    grapheResultat.append([sommet])
    return grapheResultat

def colorierWithColor(sommet, grapheResultat, color):
    if len(grapheResultat) <= color:
        grapheResultat.append([sommet])
    else:
        grapheResultat[color].append(sommet)
        
    return grapheResultat

def colorierRandom(sommet, graphe, grapheResultat):
    indices = [index for index, value in enumerate(graphe[sommet]) if value]
    
    for grapheColor in grapheResultat:
        if any(i in grapheColor for i in indices):
            continue
        else:
            grapheColor.append(sommet)
            return grapheResultat

    grapheResultat.append([sommet])
    return grapheResultat

def coutCouleur(grapheResultat):
    result = 0
    for index, valeur in enumerate(grapheResultat):
        result += (index + 1) * len(valeur)
        
    return result