import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


class NewsVisual:
    def __init__(self):
        self.nodes_from = []
        self.nodes_to = []
        self.node_map = {}
        self.node_size = {}
        self.node_degree = {}

    def increment(self,node):
        if node not in self.node_size:
            self.node_degree[node] = 1
            self.node_size[node] = 10
        else:
            self.node_degree[node] += 1
            self.node_size[node] += 10

    def add_edge(self,a,b):

        self.nodes_from.append(a)
        self.nodes_to.append(b)

        self.increment(a)
        self.increment(b)

    def unique_edges(self):
        nodes_zip = []
        for i,j in zip(self.nodes_from,self.nodes_to):
            if (i,j) not in nodes_zip and (j,i) not in nodes_zip:
                nodes_zip.append((i,j))
        self.nodes_from, self.nodes_to = zip(*nodes_zip)
        self.nodes_from = list(self.nodes_from)
        self.nodes_to = list(self.nodes_to)


    def set_node_map(self,node_map):
        self.node_map = node_map

    def show(self):
        self.unique_edges()

        df = pd.DataFrame({'from': self.nodes_from, 'to': self.nodes_to})


        G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())

        remove = [node for node, degree in dict(G.degree()).items() if degree < 4 or self.node_size[node] < 70]
        G.remove_nodes_from(remove)
        self.nodes = G.nodes()
        self.node_size = {i:self.node_size[i] for i in self.node_size if i in self.nodes}

        if len(self.node_map) ==0:
            self.node_map = {i:"group1" for i in self.nodes}

        carac = pd.DataFrame({'ID': list(self.nodes),
                              'myvalue': [self.node_map[i] for i in self.nodes]})

        # pos = nx.spring_layout(G)
        pos = nx.spring_layout(G,k=0.50,iterations=4)
        # #spec=nx.spectral_layout(G)

        # Here is the tricky part: I need to reorder carac to assign the good color to each node
        carac = carac.set_index('ID')
        carac = carac.reindex(G.nodes())

        # And I need to transform my categorical column in a numerical value: group1->1, group2->2...
        carac['myvalue'] = pd.Categorical(carac['myvalue'])


        # Custom the nodes:
        nx.draw(G, pos,with_labels=True,font_weight="bold",edge_color="gray", nodelist=self.node_size.keys(), node_size=list(self.node_size.values()),
                node_color=carac['myvalue'].cat.codes, cmap=plt.cm.Set1, alpha=0.95)
        plt.show()




