import time

from model.fermata import Fermata
from model.model import Model

tic = time.time()
m = Model()
print(f"Numero nodi: {m.get_numnodi()}")
print(f"Numero archi: {m.get_numarchi()}")
m.buildGraphPesato()
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

print(*(n for n in m.getDFSNodesFromTree(source)))
print(*(n for n in m.getBFSNodesFromTree(source)))

print(len(m.getBFSNodesFromTree(source)))
print(len(m.getDFSNodesFromTree(source)))

print("==========================================")

print("Archi con peso 2")
archiMaggiori = m.getArchiPesoMaggiore()
for a in archiMaggiori:
    print(f"{a[0]} -> {a[1]} : {a[2]}")
print(len(archiMaggiori))
