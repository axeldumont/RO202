import numpy as np
import graph
import sys

def main():
    print("Executer krustal pour :")
    print("enter 1 for ex 1")
    print("enter 2 for fig 1 gauche")
    print("enter 3 for fig 1 droite")

    n = int(input())

    # Le poids des arcs de ce graphe correspondent aux capacités
    if n == 1:
        g = graph_ex1()
    elif n == 2:
        g = graph_fig1g()
    elif n == 3:
        g = graph_fig1d()

    # Le poids des arcs de ce graphe correspondent au flot
    flow = fordFulkerson(g, "s", "t")

    print(flow)
    
# Fonction créant un graphe sur lequel sera appliqué l'algorithme de Ford-Fulkerson
def graph_ex1():
        
    g = graph.Graph(np.array(["s", "a", "b", "c", "d", "e", "t"]))

    g.addArc("s", "a", 8)
    g.addArc("s", "c", 4)
    g.addArc("s", "e", 6)
    g.addArc("a", "b", 10)
    g.addArc("a", "d", 4)
    g.addArc("b", "t", 8)
    g.addArc("c", "b", 2)
    g.addArc("c", "d", 1)
    g.addArc("d", "t", 6)
    g.addArc("e", "b", 4)
    g.addArc("e", "t", 2)
    
    return g

def graph_fig1g():
    g = graph.Graph(np.array(["s", "1", "2", "3", "4", "t"]))

    g.addArc("s", "1", 16)
    g.addArc("s", "2", 13)
    g.addArc("2", "1", 4)
    g.addArc("1", "2", 10)
    g.addArc("1", "3", 12)
    g.addArc("3", "2", 9)
    g.addArc("2", "4", 14)
    g.addArc("4", "3", 7)
    g.addArc("4", "t", 4)
    g.addArc("3", "t", 20)
    
    return g


def graph_fig1d():
    g = graph.Graph(np.array(["s", "A", "B", "C", "D", "E", "F", "t"]))

    g.addArc("s", "A", 10)
    g.addArc("s", "C", 12)
    g.addArc("s", "E", 15)
    g.addArc("A", "C", 4)
    g.addArc("A", "D", 15)
    g.addArc("A", "B", 9)
    g.addArc("B", "D", 15)
    g.addArc("B", "t", 10)
    g.addArc("C", "E", 4)
    g.addArc("C", "D", 8)
    g.addArc("D", "t", 4)
    g.addArc("D", "F", 20)
    g.addArc("E", "F", 16)
    g.addArc("F", "t", 10)
    g.addArc("F", "C", 10)
    
    return g

# Fonction appliquant l'algorithme de Ford-Fulkerson à un graphe
# Les noms des sommets sources est puits sont fournis en entrée
def fordFulkerson(g, sName, tName):

    """
    Marquage des sommets du graphe:
     - mark[i] est égal à +j si le sommet d'indice i peut être atteint en augmentant le flot sur l'arc ji
     - mark[i] est égal à -j si le sommet d'indice i peut être atteint en diminuant le flot de l'arc ji
     - mark[i] est égal à sys.float_info.max si le sommet n'est pas marqué
    """
    mark = [0] * g.n
    
    # Récupérer l'indice de la source et du puits
    s = g.indexOf(sName)
    t = g.indexOf(tName)
    
    # Créer un nouveau graphe contenant les même sommets que g
    flow = graph.Graph(g.nodes)

    # Récupérer tous les arcs du graphe 
    arcs = g.getArcs()

    while mark[t] != sys.float_info.max:
        mark = [sys.float_info.max] * g.n # Retirer toutes les marques
        mark[s] = 0 # 0 pour marquer '+' le sommet s
        mark2 = True
        while mark2 and mark[t] == sys.float_info.max:
            mark2 = False
            for arc in arcs:
                # i est marqué, j non marqué, (ij) non saturé
                if mark[arc.id1] != sys.float_info.max and mark[arc.id2] == sys.float_info.max and flow.adjacency[arc.id1][arc.id2] < arc.weight:
                    mark[arc.id2] = arc.id1 # Marque '+i' 
                    mark2 = True      
                # i non marqué, j est marqué, (ij) a un flux non nul
                if mark[arc.id1] == sys.float_info.max and mark[arc.id2] != sys.float_info.max and flow.adjacency[arc.id1][arc.id2] > 0:
                    mark[arc.id1] = -arc.id2 #Marque '-j' 
                    mark2 = True
        if mark[t] != sys.float_info.max:
            m = 1e5
            current = t
            while current != s and current != sys.float_info.max:
                new = abs(mark[current])
                if mark[current] >= 0:
                    m = min(m, g.adjacency[new][current] - flow.adjacency[new][current])
                else:
                    m = min(m, flow.adjacency[current][new])
                current = new
            if m == 0:
                break
            current = t
            while current != s and current != sys.float_info.max:
                new = abs(mark[current])
                if mark[current] >= 0:
                    flow.adjacency[new][current] += m
                else:
                    flow.adjacency[current][new] -= m

                current = new
    return flow
   
if __name__ == '__main__':
    main()