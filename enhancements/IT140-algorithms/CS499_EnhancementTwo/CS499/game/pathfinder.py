from collections import deque


def find_shortest_path(start_room, target_item):
    """
    Uses Breadth-First Search (BFS) to find the shortest path to a room containing the target item.
    Returns a list of tuples with (room name, direction to next room).

    Args:
        start_room (Room): The starting Room object.
        target_item (str): The item to search for.

    Returns:
        list: A list of tuples (room_name, direction) representing the path.
    """
    queue = deque()
    visited = set()

    # Each queue entry contains: (current_room, path_taken), where path is list of (room, direction)
    queue.append((start_room, []))

    while queue:
        current_room, path = queue.popleft()

        if current_room.name in visited:
            continue

        visited.add(current_room.name)

        if current_room.item and current_room.item.lower() == target_item.lower():
            # Return path plus current room with no direction since it's the goal
            return path + [(current_room.name, None)]

        for direction, neighbor in current_room.connections.items():
            if neighbor.name not in visited:
                # Append current room and direction to path
                queue.append((neighbor, path + [(current_room.name, direction)]))

    return None
