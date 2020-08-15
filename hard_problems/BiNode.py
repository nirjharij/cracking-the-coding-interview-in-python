class Binode:
    def __init__(self, val=None):
        self.node1 = Binode()
        self.node2 = Binode()
        self.val = val


class NodePair:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


def convert(root):
    if root is None:
        return None

    left_part = convert(root.node1)
    right_part = convert(root.node2)

    if left_part:
        concat(left_part.tail, root)

    if right_part:
        concat(root, right_part.head)

    head = root if left_part is None else left_part.head
    tail = root if right_part is None else right_part.tail
    return NodePair(head, tail)


def concat(x, y):
    x.node2 = y
    y.node1 = x
