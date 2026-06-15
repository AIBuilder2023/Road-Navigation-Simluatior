"""Change the attributes of the program here"""
""" ROAD GENERATION """
#Number of nodes in the diagram
NUM_NODES = 30
#Maximum lanes a road can have
#The capacity of the road = length * lanes
MAX_LANES = 5
#The maximum nodes a node can connect to
MAX_DEGREE = 4
#The probability of generating a connection to other nodes
EDGE_PROB = 0.1
#The ID of a list of nodes forcing to have a maximum degree of 2
FORCE_SINGLE_ROAD = [12, 13, 14, 15, 16]
#The connection limit of a node
#e.g. if it is 4, then node 12 cannot connect with node 20 as is it too far apart
CONNECTION_LIMIT = 4
#whether to make a ring connection.
#this will force to create a connection between the first node and the last node
RING = True

""" CARS """
#Number of cars generated when the simulation starts
NUM_CARS_INITIALLY = 50
#The probability of generating a car every FRAME
NEW_CAR_PROB = 0.1

#pic
#Frame per second
#This will affect the speed of car per frame and the generation of GIF file
FPS = 30
#The speed of car per frame
#When there is no congestion, the distance moved is SPEED/FPS
SPEED = 1
#The total frames in the simulatiom
FRAMES = 6000
#The scale of every PNG file generated
PIC_SCALE = 2
#Whether generate pictures of the mid-process in the simulation
SHOW_MID_PROCESS = False
#The frequency of generating mid-process pictures
#This will only be effective when SHOW_MID_PROCESS is True
FRAMES_PER_OUTPUT = 20
#Whether automatically generate GIF file when the simulating
#This will only be effective when SHOW_MID_PROCESS is True
#If it is true, the mid-process pictures will not be generated
GENERATE_GIF = False
