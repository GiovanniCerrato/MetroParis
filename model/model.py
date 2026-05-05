from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph() #Graph e DiGraph
        self._idMapFermate = {}
        for f in self._fermate:
            self._idMapFermate[f.id_fermata] = f

    def buildGraphPesato(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)
        self.addEdgesPesati()

    def addEdgesPesati(self):
        alledges = DAO.getAllEdges()
        for conn in alledges:
            u = self._idMapFermate[conn.id_stazP]
            v = self._idMapFermate[conn.id_stazA]
            if self._grafo.has_edge(u, v):
                self._grafo[u][v]['weight'] += 1
            else:
                self._grafo.add_edge(u, v, weight=1)

    def addEdgesPesati2(self):
        #delega il calcolo del peso alla query sql
        self._grafo.clear_edges()
        allEdgesWPeso = DAO.getAllEdgesPesati()

        for e in allEdgesWPeso:
            u = self._idMapFermate[e[0]]
            v = self._idMapFermate[e[1]]
            peso = e[2]

            self._grafo.add_edge(u, v, weight=peso)

    def getArchiPesoMaggiore(self):
        edges = self._grafo.edges(data=True)
        edgesMaggiori = []
        for e in edges:
            if self._grafo.get_edge_data(e[0], e[1])["weight"] > 1:
                edgesMaggiori.append(e)
        return edgesMaggiori



    def buildGraph(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._fermate)
        #self.addedges() (corretto ma troppo lento!!) ma buono se il grafo che devo costruire è piccolo!
        #self.addedge2() (molto buono)
        self.addedge3() #(IL MIGLIORE!)

    def addedges(self):
        for u in self._fermate:
            for v in self._fermate:
                if (u != v):
                    if DAO.hasconn(u,v):
                        self._grafo.add_edge(u, v)

    def addedge2(self):
        for u in self._fermate:
            for conn in DAO.getvicini(u):
                v = self._idMapFermate[conn.id_stazA]
                self._grafo.add_edge(u, v)

    def addedge3(self):
        alledges = DAO.getAllEdges()
        for conn in alledges:
            u = self._idMapFermate[conn.id_stazP]
            v = self._idMapFermate[conn.id_stazA]
            self._grafo.add_edge(u, v)

    def getBFSNodesFromEdges(self, source):
        archi = nx.bfs_edges(self._grafo, source)
        nodiBFS = []
        for u, v in archi:
            nodiBFS.append(v)
        return nodiBFS

    def getDFSNodesFromEdges(self, source):
        archi = nx.dfs_edges(self._grafo, source)
        nodiDFS = []
        for u, v in archi:
            nodiDFS.append(v)
        return nodiDFS

    def getBFSNodesFromTree(self, source):
        tree = nx.bfs_tree(self._grafo, source)
        archi = list(tree.edges())
        nodi = list(tree.nodes())
        return nodi[1:]
    def getDFSNodesFromTree(self, source):
        tree = nx.dfs_tree(self._grafo, source)
        archi = list(tree.edges())
        nodi = list(tree.nodes())
        return nodi[1:]






    def get_numnodi(self):
        return len(self._grafo.nodes)

    def get_numarchi(self):
        return len(self._grafo.edges)

    @property
    def fermate(self):
        return self._fermate

if __name__ == "__main__":
    model = Model()
    model.buildGraph()
    print("Numero nodi:",model.getNodi())