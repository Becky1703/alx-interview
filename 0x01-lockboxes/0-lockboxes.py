#!/usr/bin/python3
"""Method for unlocking Lockboxes"""


def canUnlockAll(boxes):
    """Method to check if boxes can be unlocked"""

    n = len(boxes)

    # creates a list to track what box has been visited
    visited = set([0])

    # The first box is unlocked
    not_visited = set(boxes[0]).difference(set([0]))

    while len(not_visited) > 0:
        box_idx = not_visited.pop()

        # Check what key is in the current box
        if not box_idx or box_idx >= n or box_idx < 0:
            continue
        # if the key can open a box that hasn't been visited,
        # mark it as visited
        if box_idx not in visited:
            not_visited = not_visited.union(boxes[box_idx])
            visited.add(box_idx)

        # check if all boxes have been visited
        return n == len(visited)
