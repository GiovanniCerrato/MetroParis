import time
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