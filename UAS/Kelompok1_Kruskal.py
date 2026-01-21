# Penyusunan jaringan infrastruktur menggunakan Kruskal

# Definisi edge: (biaya, titik1, titik2)
edges = [
    (4, 'A', 'B'),
    (3, 'A', 'C'),
    (2, 'B', 'C'),
    (5, 'B', 'D'),
    (7, 'C', 'D'),
    (8, 'C', 'E'),
    (6, 'D', 'E')
]

# Semua vertex
vertices = ['A', 'B', 'C', 'D', 'E']

# Struktur parent untuk union-find
parent = {v: v for v in vertices}

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])  # path compression
    return parent[v]

def union(u, v):
    root_u = find(u)
    root_v = find(v)
    parent[root_v] = root_u

# Kruskal algorithm
def kruskal(vertices, edges):
    mst = []
    edges_sorted = sorted(edges)  # urutkan berdasarkan biaya
    
    for cost, u, v in edges_sorted:
        if find(u) != find(v):
            mst.append((u, v, cost))
            union(u, v)
    
    return mst

# Menjalankan Kruskal
mst = kruskal(vertices, edges)

print("Minimum Spanning Tree (Jaringan Infrastruktur):")
total_cost = 0
for u, v, cost in mst:
    print(f"{u} - {v} : {cost}")
    total_cost += cost
print(f"Total Biaya: {total_cost}")
