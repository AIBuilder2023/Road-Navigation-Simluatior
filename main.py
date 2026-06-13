from core.road import *
import core.car as car
import algorithm.astar as astar
import visualize.road_draw
import core.processing as processing
import time
import random
from attributes import *
from tqdm import tqdm
import imageio




G = create_road_graph(NUM_NODES,MAX_DEGREE,EDGE_PROB)
pos = nx.spring_layout(G, seed=114514,weight="weight")

edges = G.edges()
nodes = G.nodes()
#print(edges)
cars = []
num_cars = 0
for i in range(NUM_CARS_INITIALLY):
    cars.append(car.car(NUM_NODES,pos))
    astarres = astar.astar(G,cars[i].startPt, cars[i].endPt,pos)
    cars[i].route = astarres
    num_cars += 1
    #print(f"{i}车想从{cars[i].startPt}前往{cars[i].endPt}，他的最优A*路径是${astarres}")

frames = []
for t in tqdm(range(FRAMES)):
    processing.whole_process(G,cars,FPS,SPEED)
    visualize.road_draw.draw(G,cars,t,frames)
    if random.random() < NEW_CAR_PROB:
        #+print("NEW CAR")
        cars.append(car.car(NUM_NODES, pos))
        astarres = astar.astar(G, cars[num_cars].startPt, cars[num_cars].endPt, pos)
        cars[num_cars].route = astarres
        num_cars += 1
    #frames.append(imageio.imread(f"logs/frame{t}.png"))
    #print(f"frame {t}")
if GENERATE_GIF:
    imageio.mimsave("traffic.gif", frames, fps=FPS)