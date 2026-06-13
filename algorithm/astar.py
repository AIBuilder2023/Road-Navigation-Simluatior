import heapq
import math

def heuristic(pos, a, b):
    """欧几里得距离"""
    x1, y1 = pos[a]
    x2, y2 = pos[b]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def astar(G, start, goal, pos):
    """
    G: networkx graph
    start: 起点
    goal: 终点
    pos: 节点坐标 {node: (x, y)}
    """

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}

    g_score = {node: float('inf') for node in G.nodes}
    g_score[start] = 0

    f_score = {node: float('inf') for node in G.nodes}
    f_score[start] = heuristic(pos, start, goal)

    while open_set:

        _, current = heapq.heappop(open_set)

        if current == goal:
            # 重建路径
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in G.neighbors(current):

            # 边权重（你可以改成 congestion-aware）
            edge_data = G[current][neighbor]
            cost = edge_data.get("length", 1)

            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(pos, neighbor, goal)

                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None