import networkx as nx
from attributes import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import imageio
from io import BytesIO
import sys

def get_car_position_on_graph(G,car):
    pos = nx.spring_layout(G, seed=114514, weight="weight")
    fromPt = car.route[car.progress]
    toPt = car.route[car.progress+1]
    fromPos = pos[fromPt]
    toPos = pos[toPt]
    return fromPos[0] + car.distance * (toPos[0] - fromPos[0]), fromPos[1]+car.distance * (toPos[1] - fromPos[1])

def draw(G,cars,t,frames):
    #position
    pos = nx.spring_layout(G, seed=114514,weight="weight")
    #pos = nx.shell_layout(G)
    edges = G.edges()

    #color
    cmap = cm.RdYlGn_r
    norm = mcolors.Normalize(vmin=0, vmax=1)
    colors = [cmap(norm(G[e[0]][e[1]]["congestion"])) for e in edges]

    #label
    edge_labels = nx.get_edge_attributes(G, "length")

    #draw
    plt.figure(figsize=(15, 11.25))
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color="lightblue")
    nx.draw_networkx_labels(G, pos, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,font_size=19)
    nx.draw_networkx_edges(G, pos, width=2.5, alpha=0.6, edge_color=colors)

    change = False
    for i in cars:
        if not i.destination and i.route[i.progress] != i.endPt:
            x,y = get_car_position_on_graph(G,i)
            plt.scatter(x,y,color="red",s=50,zorder=10)
            change = True
    """
    if not change:
        sys.exit()
    """

    plt.title("Traffic")
    plt.axis("off")
    plt.show()
    if GENERATE_GIF:
        buf = BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)

        frames.append(imageio.v2.imread(buf))
    else:
        plt.savefig(f"logs/frame{t}.png")

    plt.close('all')