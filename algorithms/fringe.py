# see https://en.wikipedia.org/wiki/Fringe_search pseudocode
import pygame
from components.grid import reconstruct_path_fringe
from algorithms.a_star import h # same heuristic function


def fringe_algo(draw, grid, start, end):
    fringe = []
    cache = {}
    cache[start] = (0, None)
    fringe.append(start)
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
                reconstruct_path_fringe(cache, end, draw)
                end.make_end()
                start.make_start()
                return True

            draw()
            if node != start:
                node.make_closed()

            for child in node.neighbors:
                g_child = g + 1
                # If the child node has already been seen
                if child in cache:
                    g_cached, _ = cache[child]
                    if g_child >= g_cached:
                        continue

                if child in fringe:
                    fringe.remove(child)
                fringe.append(child)
                cache[child] = (g_child, node)

                if not child.is_start() and not child.is_end():
                    child.make_open()
            fringe.remove(node)
        f_limit = f_min

    return False
