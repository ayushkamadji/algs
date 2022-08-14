from manim import *
import networkx as nx
import matplotlib.pyplot as plt

class LabeledModifiedGraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        lt = {1: [-1, 0, 0], 2: [0, 0, 0], 3: [1, 0, 0], 4: [-1, -1, 0], 5: [0, -1, 0], 6: [1, -1, 0], 7: [0, -2, 0], 8: [1, -2, 0]}
        g = Graph(vertices, edges, layout=lt, labels=True)
        self.add(g)

def main():
  G=nx.Graph()
  i=1
  G.add_node(i,pos=(i,i))
  G.add_node(2,pos=(2,2))
  G.add_node(3,pos=(1,0))
  G.add_edge(1,2,weight=0.5)
  G.add_edge(1,3,weight=9.8)
  pos=nx.get_node_attributes(G,'pos')
  nx.draw(G,pos)
  labels = nx.get_edge_attributes(G,'weight')
  nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
  plt.savefig("weighted_graph.png")
  print(list(G.edges))

if __name__ == '__main__':
    main()