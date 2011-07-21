from ashu import timer

class Node:
    data = None 
    nodes = []
    def __init__(self,data):
        self.data = data
    def __str__(self):
        return str(self.data)

def suckup_nodes():
    f = open('./18/file.txt')
    first_node = Node(int(f.readline()))
    previous_nodes = [first_node] 
    
    for line in f.readlines():
        line = line.strip()
        current_nodes = map(lambda x:Node(int(x)),line.split())
        for node,i in zip(previous_nodes,range(0,len(previous_nodes))):
            node.nodes = [current_nodes[i],current_nodes[i+1]]
        previous_nodes = current_nodes
    return first_node

def memoize(find_max_sum_fn):
    cache = {}
    def memoized_find_max_sum(node):
        if node in cache:
            return cache[node]
        else:
            max_sum = find_max_sum_fn(node)
            cache[node] = max_sum
            return max_sum
    return memoized_find_max_sum

@memoize
def find_max_sum(node):
    if len(node.nodes) == 0:
        return node.data
    else:
        return node.data + max(map(find_max_sum,node.nodes))
@timer
def euler():
    root = suckup_nodes()
    return find_max_sum(root)
    

if __name__ == '__main__':
    print euler()
