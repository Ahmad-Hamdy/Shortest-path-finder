# Shortest-path-finder
an implementation for a robot that finds the shortest path between 2 points.

The robot finds the path using "A* searching algorithm", the bot is given a matrix of 0s and 1s 
where zeros represents the obstacles (walls, rivers, ....etc) and the ones represents points(pixels)
available for movements.

The path is found by calculating the g-cost for the neigbouring points of each point visited,
where the g-cost is the sum of 2 distances, the distance traveled from the starting point until 
the point currently checking is visited, plus the absolute distance between this point and the end point
and this is often referred to as the heuristic, which is nothing but a kind of smart guess, as the real 
distance is not yet known.

After calculating the g-cost of each neighbouring point, the one with the lowest g-cost is checked and
the same process is repeated for it until the target point is found.
