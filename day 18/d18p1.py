# this problem is most neatly be handled via a binary tree structure
# as with this entire AoC, recursion aplenty
# the hints for binary tree: very very embedded structures, with only 2 vals per.

# calculates magnitude of smallfish no.
def magnitude(node):
    if isinstance(node, int):
        return(node)
    else:
        return(3*magnitude(node.left)+2*magnitude(node.right))

# nodes have no individual values, only leaves do
class Node:
    def __init__(self, l=None, r=None):
        self.left = l
        self.right = r
    # print tree leaves left to right
    def PrintTree(self, depth=1):
        print(self.left,depth) if isinstance(self.left,int) else self.left.PrintTree(depth+1)
        print(self.right,depth) if isinstance(self.right,int) else self.right.PrintTree(depth+1)
    # gets list of nodes with leaves attached, from left to right
    def GetPointers(self):
        points = []
        if isinstance(self.left,Node):
            points += self.left.GetPointers()
        if isinstance(self.left,int) or isinstance(self.right,int):
            points.append(self)
        if isinstance(self.right,Node):
            points += self.right.GetPointers()
        return(points)

# recursive function to convert a smallfish to a binary tree
def to_tree(arr):
    new = Node()
    new.left = arr[0] if isinstance((arr[0]),int) else to_tree(arr[0])
    new.right = arr[1] if isinstance((arr[1]),int) else to_tree(arr[1])
    return(new)

# add smallfish nos whilst in binary tree structure
def add_nodes(node1,node2):
    if node1 == None:
        return(node2)
    new = Node()
    new.left = node1
    new.right = node2
    return(new)

# takes node of a tree, looks through for a explosive and explodes it.
def explode(node, depth, pointers, exploded):
    # standard in-order traversal
    next=False

    if isinstance(node.left, Node) and not exploded:
        exploded, next = explode(node.left, depth+1, pointers, exploded)
        if exploded and next:
            node.left=0
            next=False

    # explosive discovered, thus explosion occurs
    if depth>4 and isinstance(node.left,int) and isinstance(node.right,int) and not exploded:
        i = pointers.index(node)
        if i > 0:
            if isinstance(pointers[i-1].right,int):
                pointers[i-1].right += node.left
            else:
                pointers[i-1].left += node.left
        if i < len(pointers)-1:
            if isinstance(pointers[i+1].left,int):
                pointers[i+1].left += node.right
            else:
                pointers[i+1].right += node.right
        return(True,True)

    if isinstance(node.right, Node) and not exploded:
        exploded, next = explode(node.right, depth+1, pointers, exploded)
        if exploded and next:
            node.right=0
            next=False

    return(exploded, False)

# goes through all leaves to see if any can split, and splits left-most
# depth unimportant, so we don't need to properly tree traverse
def split(pointers):
    for i in pointers:
        if isinstance(i.left,int) and i.left>9:
            l = int(i.left/2)
            r = (i.left)%2
            i.left = Node(l,l+r)
            return(True)
        elif isinstance(i.right,int) and i.right>9:
            l = int(i.right/2)
            r = (i.right)%2
            i.right = Node(l,l+r)
            return(True)

    return(False)


file = open('./input.txt', 'r')
line = file.readline().strip()
current_tree = None
while line:
    # danger danger eval - but easily the tidiest way of parsing by far
    # I really don't feel like *another* recursive function, so just make sure input is safe
    current_tree = add_nodes(current_tree,to_tree(eval(line)))

    # tries to explode as much as possible, then splits till can explode. Rinse and repeat
    splitted = True
    while splitted:
        exploded = True
        while exploded:
            exploded,_ = explode(current_tree, 1, current_tree.GetPointers(), False)
        splitted = split(current_tree.GetPointers())

    line = file.readline().strip()

print(magnitude(current_tree))
