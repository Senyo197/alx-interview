#!/usr/bin/python3
"""Determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    queue = [0]
    front = 0

    while front < len(queue):
        current_box = queue[front]
        front += 1
        visited.add(current_box)

        for key in boxes[current_box]:
            if key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
