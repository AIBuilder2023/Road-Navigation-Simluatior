from core.road import *
import core.car as car
import algorithm.astar as astar
import visualize.road_draw as visualize
import visualize.result_congestion as result_congestion
import core.processing as processing
from attributes import *

from time import time,localtime,strftime
import random
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

frames = []
for t in tqdm(range(FRAMES)):
    processing.whole_process(G,cars,FPS,SPEED)
    if SHOW_MID_PROCESS and t%FRAMES_PER_OUTPUT==0:
        visualize.draw(G,cars,t,frames)
    if random.random() < NEW_CAR_PROB:
        #+print("NEW CAR")
        cars.append(car.car(NUM_NODES, pos))
        astarres = astar.astar(G, cars[num_cars].startPt, cars[num_cars].endPt, pos)
        cars[num_cars].route = astarres
        num_cars += 1
    #frames.append(imageio.imread(f"logs/frame{t}.png"))
    #print(f"frame {t}")
passed = 0
tot_time = 0
tot_avg_speed = 0
for i in cars:
    if i.destination:
        passed += 1
        tot_time += i.time_cost / FPS
        tot_avg_speed += i.tot_distance / i.time_cost * FPS
avg_time = tot_time/passed
avg_speed = tot_avg_speed / passed
result_congestion.draw(G,passed,avg_time,avg_speed)
if GENERATE_GIF:
    imageio.mimsave(f"logs/gif/traffic{strftime('%Y%m%d-%H%M%S',localtime(time()))}.gif", frames, fps=FPS)