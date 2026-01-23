# Untuk Visualisasi graf
import matplotlib.pyplot as plt
import networkx as nx

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

# ===== VISUALISASI GRAF =====

# Membuat graf asli (semua edges)
G = nx.Graph()
for cost, u, v in edges:
    G.add_edge(u, v, weight=cost)

# Membuat graf MST
MST = nx.Graph()
for u, v, cost in mst:
    MST.add_edge(u, v, weight=cost)

# Membuat figure dengan 2 subplot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Layout untuk kedua graf (menggunakan layout yang sama)
pos = nx.spring_layout(G, seed=42, k=2)

# --- GRAF ASLI (KIRI) ---
ax1.set_title('Graf Asli (Semua Jalur)', fontsize=14, fontweight='bold')
nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                       node_size=2000, ax=ax1)
nx.draw_networkx_labels(G, pos, font_size=10, 
                        font_weight='bold', ax=ax1)
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, 
                       edge_color='gray', ax=ax1)

# Label edge dengan biaya
edge_labels_full = {(u, v): cost for cost, u, v in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels_full, 
                             font_size=9, ax=ax1)

ax1.axis('off')

# --- MST (KANAN) ---
ax2.set_title(f'Minimum Spanning Tree (Biaya Total: {total_cost})', 
             fontsize=14, fontweight='bold')
nx.draw_networkx_nodes(MST, pos, node_color='lightgreen', 
                       node_size=2000, ax=ax2)
nx.draw_networkx_labels(MST, pos, font_size=10, 
                        font_weight='bold', ax=ax2)
nx.draw_networkx_edges(MST, pos, width=3, alpha=0.8, 
                       edge_color='darkgreen', ax=ax2)

# Label edge MST dengan biaya
edge_labels_mst = {(u, v): cost for u, v, cost in mst}
nx.draw_networkx_edge_labels(MST, pos, edge_labels_mst, 
                             font_size=9, ax=ax2)

ax2.axis('off')

plt.tight_layout()
plt.show()

