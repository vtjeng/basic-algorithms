import queue

def bfs(source, target, neigbours):
    """

    :param source:
    :param target:
    :param neigbours:
    :return: Path from source to target.
    """
    visited_nodes = set()
    parent_node = dict()
    q = queue.Queue()
    visited_nodes.add(source)
    parent_node[source] = None
    q.put(source)
    while not q.empty():
        v = q.get()
        for u in neigbours[v]:
            if u not in visited_nodes:
                visited_nodes.add(u)
                parent_node[u] = v
                q.put(u)
            # Note: you could do a check here and break early if you've found the target

    print(parent_node)
    current_node = target
    reverse_path = []
    while current_node is not None:
        reverse_path.append(current_node)
        current_node = parent_node[current_node]

    return list(reversed(reverse_path))

print(bfs(1, 4, {1: [2, 3, 4], 2: [1, 3, 4], 3:[1, 2, 4], 4:[1, 2, 3]}))
print(bfs(1, 4, {1: [2], 2: [1, 3], 3:[2, 4], 4:[3]}))