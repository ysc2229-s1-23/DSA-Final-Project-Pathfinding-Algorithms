# see https://en.wikipedia.org/wiki/Fringe_search
import pygame
from components.grid import reconstruct_path_fringe
from algorithms.a_star import h # same heuristic function


def fringe_algo(draw, grid, start, end):
    fringe = [start]
    cache = {}
    cache[start] = (0, None)
    f_limit = h(start, end)

    while fringe:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        f_min = float("inf")

        for node in fringe:
            g, _ = cache[node]

            # Get f-score for current node
            f = g + h(node, end)

            # Check if the f-score is greater than the allowed limit
            if f > f_limit:
                f_min = min(f, f_min)
                continue
            if node.is_end():
                f_limit = f_min
                reconstruct_path_fringe(cache, end, draw)
                end.make_end()
                start.make_start()
                return True

            draw()
            if node != start:
                node.make_closed()

            for child in reversed(node.neighbors):
                g_child = g + h(child, start)
                # If the child node has already been seen
                if child in cache and cache[child]!=None:
                    g_cached = cache[child][0]
                    if g_child >= g_cached:
                        continue

                if child in fringe:
                    fringe.remove(child)
                fringe.insert(fringe.index(node), child)
                cache[child] = (g_child, node)

                if not child.is_start() and not child.is_end():
                    child.make_open()
            fringe.remove(node)
        f_limit = f_min

    return False
