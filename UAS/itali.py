# Penyusunan jaringan transportasi menggunakan Algoritma Kruskal

# Definisi edge: (biaya, kota1, kota2)
edges = [
    (3, 'Brescia', 'Verona'),
    (2, 'Bologna', 'Modena'),
    (3, 'Modena', 'Parma'),
    (4, 'Parma', 'Bologna'),
    (5, 'Verona', 'Modena'),
    (6, 'Verona', 'Bologna'),
    (7, 'Brescia', 'Parma')
]

# Semua vertex
vertices = ['Brescia', 'Verona', 'Parma', 'Modena', 'Bologna']

# Struktur parent untuk Union-Find
parent = {v: v for v in vertices}

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])  # path compression
    return parent[v]

def union(u, v):
    root_u = find(u)
    root_v = find(v)
    parent[root_v] = root_u

# Implementasi Algoritma Kruskal
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

print("Minimum Spanning Tree (Jaringan Transportasi):")
total_cost = 0
for u, v, cost in mst:
    print(f"{u} - {v} : {cost}")
    total_cost += cost

print(f"Total Biaya Minimum: {total_cost}")
