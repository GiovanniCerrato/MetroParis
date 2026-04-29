import time

from model.fermata import Fermata
from model.model import Model

tic = time.time()
m = Model()
print(f"Numero nodi: {m.get_numnodi()}")
print(f"Numero archi: {m.get_numarchi()}")
m.buildGraph()
toc = time.time()
print(f"Numero nodi: {m.get_numnodi()}")
print(f"Numero archi: {m.get_numarchi()}")
print(f"Elapsed time: {toc - tic}")
#print(m._grafo.edges)

source = Fermata(2, "Abbesses", 2.33855, 48.8843)

nodiBFS = m.getBFSNodesFromEdges(source)
print(len(nodiBFS))
for i in range (10):
    print(nodiBFS[i])

nodiDFS = m.getDFSNodesFromEdges(source)
print(len(nodiDFS))
for i in range (10):
    print(nodiDFS[i])
