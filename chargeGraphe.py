def chargeGraphe(filename):
    dataGraphe = []
    with open(filename, 'r') as file:
        col, row = None, None
        for line in file:
            if line.startswith('p'):
                col, row = map(int, line.split()[2:])
                dataGraphe = [[False for _ in range(col)] for _ in range(col)]
            elif line.startswith('e'):
                u, v = map(int, line.split()[1:])
                dataGraphe[u-1][v-1] = True
                dataGraphe[v-1][u-1] = True
    return dataGraphe