def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y: parent[y] = x
    else: parent[x] = y

if __name__ == "__main__":
    #Create graph
    # 
    # 
