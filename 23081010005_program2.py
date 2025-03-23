from collections import deque

# Definisi graf sebagai adjacency list
graf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Algoritma Breadth-First Search (BFS)
def bfs(graf, mulai, tujuan):
    antrian = deque([[mulai]])  # Antrian BFS (queue), mulai dari node awal
    dikunjungi = set()  # Menyimpan node yang sudah dikunjungi

    while antrian:
        jalur = antrian.popleft()  # Ambil jalur pertama dari antrian
        simpul = jalur[-1]  # Ambil simpul terakhir dari jalur

        if simpul in dikunjungi:
            continue  # Lewati jika sudah dikunjungi

        dikunjungi.add(simpul)

        if simpul == tujuan:
            return jalur  # Jika ketemu tujuan, kembalikan jalurnya

        for tetangga in graf.get(simpul, []):  # Tambahkan jalur baru ke antrian
            jalur_baru = list(jalur) + [tetangga]
            antrian.append(jalur_baru)

    return None  # Jika tidak ada jalur ke tujuan

# Algoritma Depth-First Search (DFS)
def dfs(graf, mulai, tujuan):
    tumpukan = [[mulai]]  # Tumpukan DFS (stack), mulai dari node awal
    dikunjungi = set()  # Menyimpan node yang sudah dikunjungi

    while tumpukan:
        jalur = tumpukan.pop()  # Ambil jalur terakhir dari tumpukan
        simpul = jalur[-1]  # Ambil simpul terakhir dari jalur

        if simpul in dikunjungi:
            continue  # Lewati jika sudah dikunjungi

        dikunjungi.add(simpul)

        if simpul == tujuan:
            return jalur  # Jika ketemu tujuan, kembalikan jalurnya

        for tetangga in reversed(graf.get(simpul, [])):  # Tambahkan jalur baru ke tumpukan
            jalur_baru = list(jalur) + [tetangga]
            tumpukan.append(jalur_baru)

    return None  # Jika tidak ada jalur ke tujuan

# Contoh penggunaan
mulai = 'A'
tujuan = 'G'

hasil_bfs = bfs(graf, mulai, tujuan)
hasil_dfs = dfs(graf, mulai, tujuan)

print("Pencarian BFS (Breadth-First Search):", hasil_bfs)
print("Pencarian DFS (Depth-First Search):", hasil_dfs)
