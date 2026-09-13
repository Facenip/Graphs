class Node:
    def __init__(self, id):
        self.id = id
        self.children = []


def decode_tree(code):  #Восстановление
    root = Node(0)
    stack = [root]
    next_id = 1

    for bit in code:
        if bit == "1":
            child = Node(next_id)
            stack[-1].children.append(child)
            stack.append(child)
            next_id += 1
        else:
            stack.pop()

    return root


def export_to_dot(root, filename): #Экспорт в DOT
    lines = ["digraph Tree {", "    node [shape=circle];"]

    def dfs(node):
        for child in node.children:
            lines.append(f"    n{node.id} -> n{child.id};")
            dfs(child)

    dfs(root)
    lines.append("}")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    code = "110110001100"
    tree = decode_tree(code)
    export_to_dot(tree, "example_tree.dot")