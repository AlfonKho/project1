meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tanggapan terhadap lelucon",
            "SHEESH": "Sedikit ketidaksetujuan",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif/marah",
            }

word = input("Ketik kata yang tidak kamu ngerti (ketik menggunakan huruf kapital semua): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Kata tidak ditemukan di kamus")
