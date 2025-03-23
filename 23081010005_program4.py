def rekomendasi_minuman(cuaca, aktivitas):
    # Aturan berdasarkan cuaca dan aktivitas
    if cuaca == "panas":
        if aktivitas == "olahraga":
            return "Minumlah air dingin agar tetap segar!"
        elif aktivitas == "santai":
            return "Minumlah es teh untuk menyegarkan hari Anda."
        elif aktivitas == "kerja":
            return "Minumlah kopi dingin agar tetap fokus."
    
    elif cuaca == "dingin":
        if aktivitas == "olahraga":
            return "Minumlah susu hangat agar tubuh tetap bertenaga."
        elif aktivitas == "santai":
            return "Minumlah coklat panas untuk menghangatkan tubuh."
        elif aktivitas == "kerja":
            return "Minumlah kopi panas agar tetap semangat bekerja."
    
    elif cuaca == "hujan":
        if aktivitas == "olahraga":
            return "Minumlah jahe hangat untuk menjaga daya tahan tubuh."
        elif aktivitas == "santai":
            return "Minumlah teh hangat agar lebih rileks."
        elif aktivitas == "kerja":
            return "Minumlah kopi panas agar tetap fokus."

    return "Silakan pilih cuaca dan aktivitas yang valid."

# Contoh penggunaan
cuaca = input("Masukkan kondisi cuaca (panas/dingin/hujan): ").lower()
aktivitas = input("Masukkan aktivitas (olahraga/santai/kerja): ").lower()

print(rekomendasi_minuman(cuaca, aktivitas))
