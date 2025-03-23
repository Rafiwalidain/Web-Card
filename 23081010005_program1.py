# Seorang petani ingin memindahkan dirinya, seekor serigala, seekor ayam gemuk, dan seikat padi menyeberangi sungai. 
# Sayangnya kapasitas perahu terbatas, perahu hanya dapat membawa satu objek untuk menyeberangi sungai dalam satu waktu.
# Selain kapasitas perahu, petani tidak dapat meninggalkan serigala dengan ayam, atau ayam dengan padi.
# Buatlah program yang menampilkan langkah-langkah pemindahan petani, serigala, ayam, dan padi
# dari sisi awal ke sisi seberang sungai dengan memperhatikan aturan tersebut.
from collections import deque

# Keadaan awal (1 = di sisi awal, 0 = di sisi seberang)
keadaan_awal = (1, 1, 1, 1)  # (Petani, Serigala, Ayam, Padi)
keadaan_tujuan = (0, 0, 0, 0)  # Semua harus sampai di seberang

# Aturan perpindahan yang diperbolehkan
perpindahan_valid = {
    (1, 0, 0, 0): "Petani menyeberang sendiri",
    (1, 1, 0, 0): "Petani membawa Serigala",
    (1, 0, 1, 0): "Petani membawa Ayam",
    (1, 0, 0, 1): "Petani membawa Padi"
}

# Fungsi untuk mengecek apakah keadaan valid (tidak melanggar aturan)
def keadaan_valid(keadaan):
    # Jika petani tidak ada di sisi yang sama, ayam tidak boleh sendirian dengan serigala atau padi
    if keadaan[0] != keadaan[1] and keadaan[1] == keadaan[2]:  # Serigala dan ayam bersama tanpa petani
        return False
    if keadaan[0] != keadaan[2] and keadaan[2] == keadaan[3]:  # Ayam dan padi bersama tanpa petani
        return False
    return True

# Algoritma BFS untuk mencari solusi
def cari_solusi():
    antrian = deque([(keadaan_awal, [], "Mulai dari sisi awal")])  # (keadaan sekarang, langkah-langkah, deskripsi)
    telah_dikunjungi = set()
    
    while antrian:
        keadaan_sekarang, langkah, deskripsi = antrian.popleft()
        
        if keadaan_sekarang == keadaan_tujuan:
            return langkah + [(keadaan_tujuan, "Semua telah sampai di seberang")]  # Jika sampai tujuan, kembalikan jalur
        
        if keadaan_sekarang in telah_dikunjungi:
            continue
        telah_dikunjungi.add(keadaan_sekarang)
        
        for pindah, deskripsi_pindah in perpindahan_valid.items():
            keadaan_baru = tuple(keadaan_sekarang[i] - pindah[i] if keadaan_sekarang[i] == 1 else keadaan_sekarang[i] + pindah[i] for i in range(4))
            if keadaan_valid(keadaan_baru):
                antrian.append((keadaan_baru, langkah + [(keadaan_baru, deskripsi_pindah)], deskripsi_pindah))  # Tambahkan ke jalur
    
    return None  # Tidak ada solusi

# Jalankan pencarian solusi
solusi = cari_solusi()
if solusi:
    print("Langkah-langkah pemindahan:")
    print("Format: (Petani, Serigala, Ayam, Padi) - Keterangan")
    print("-" * 50)
    for langkah, keterangan in solusi:
        print(f"{langkah} -> {keterangan}")
else:
    print("Tidak ada solusi yang ditemukan.")