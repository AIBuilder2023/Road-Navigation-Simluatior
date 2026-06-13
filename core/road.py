import random
import networkx as nx
from attributes import *
def create_road_graph(NUM_NODES,MAX_DEGREE,EDGE_PROB):
        G = nx.Graph()
        G.add_nodes_from(range(NUM_NODES))

        #make sure all nodes are connected together
        nodes = list(G.nodes)
        for i in range(1,NUM_NODES):
            length = random.randint(1, 7)
            capacity = length * random.randint(1, MAX_LANES)
            G.add_edge(i, i-1,
                       weight=1/ length,
                       length=length,
                       capacity=capacity,
                       congestion=0.0,
                       cars=0,
                       congestion_logs=[])

        #ring
        if RING:
            length = random.randint(1, 7)
            capacity = length * random.randint(1, MAX_LANES)
            G.add_edge(0, NUM_NODES-1,
                       weight=1 / length,
                       length=length,
                       capacity=capacity,
                       congestion=0.0,
                       cars=0,
                       congestion_logs=[])

        #random connection
        for i in range(NUM_NODES):
            for j in range(i + 1, NUM_NODES):
                if random.random() < EDGE_PROB:
                    if G.degree[i] < MAX_DEGREE and G.degree[j] < MAX_DEGREE \
                        and abs(i-j)<=CONNECTION_LIMIT \
                        and not i in FORCE_SINGLE_ROAD\
                        and not j in FORCE_SINGLE_ROAD:
                        length = random.randint(1, 7)
                        capacity = length*random.randint(1, MAX_LANES)
                        G.add_edge(i, j,
                                   weight=1/length,
                                   length=length,
                                   capacity=capacity,
                                   congestion=0.0,
                                   cars=0,
                                   congestion_logs=[])

        return G