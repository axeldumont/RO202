import graph
import sys

def main():
    cities = []
    cities.append("Paris")
    cities.append("Hambourg")
    cities.append("Londres")
    cities.append("Amsterdam")
    cities.append("Edimbourg")
    cities.append("Berlin")
    cities.append("Stockholm")
    cities.append("Rana")
    cities.append("Oslo")

    g = graph.Graph(cities)
    
    g.addArc("Paris", "Hambourg", 7)
    g.addArc("Paris",  "Londres", 4)
    g.addArc("Paris",  "Amsterdam", 3)
    g.addArc("Hambourg",  "Stockholm", 1)
    g.addArc("Hambourg",  "Berlin", 1)
    g.addArc("Londres",  "Edimbourg", 2)
    g.addArc("Amsterdam",  "Hambourg", 2)
    g.addArc("Amsterdam",  "Oslo", 8)
    g.addArc("Amsterdam",  "Londres", 1)
    g.addArc("Stockholm",  "Oslo", 2)
    g.addArc("Stockholm",  "Rana", 5)
    g.addArc("Berlin",  "Amsterdam", 2)
    g.addArc("Berlin",  "Stockholm", 1)
    g.addArc("Berlin",  "Oslo", 3)
    g.addArc("Edimbourg",  "Oslo", 7)
    g.addArc("Edimbourg",  "Amsterdam", 3)
    g.addArc("Edimbourg",  "Rana", 6)
    g.addArc("Oslo",  "Rana", 2)
    # Applique l'algorithme de Dijkstra pour obtenir une arborescence
    tree = dijkstra(g, "Paris")
    print(tree)

def argmin(L, v2):
    cand = None

    for i in range(len(L)):
        if i not in v2 and (cand == None or L[cand] > L[i]):
            cand = i
    
    return cand


def dijkstra(g, origin):	
    # Get the index of the origin 
    r = g.indexOf(origin)

    # Next node considered 
    pivot = r

    # Liste qui contiendra les sommets ayant été considérés comme pivot
    v2 = []
    v2.append(r)

    pred = [0] * g.n

    # Les distances entre r et les autres sommets sont initialement infinies
    pi = [sys.float_info.max] * g.n
    pi[r] = 0

    for _ in range(1, g.n):
        for y in [e.id2 for e in g.getArcs() if e.id1 == pivot]:
            if pi[pivot] + g.adjacency[pivot][y] < pi[y]:
                pi[y] = pi[pivot] + g.adjacency[pivot][y]
                pred[y] = pivot

        pivot = argmin(pi, v2)
        v2.append(pivot)

    final = graph.Graph(g.nodes)

    for i in range(len(pi)):
        if g.adjacency[pred[i]][i] < sys.float_info.max:
            final.addArc(g.nodes[pred[i]], g.nodes[i], g.adjacency[pred[i]][i])

    return final

   
if __name__ == '__main__':
    main()
