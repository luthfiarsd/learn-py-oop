class Buah:

    # INISIALISASI PERTAMA KALI OBJEK
    def __init__(self, nama, jumlah) -> None:
        self.nama = nama
        self.jumlah = jumlah

    # MODIFIKASI KETIKA PRINT OBJEK
    def __repr__(self) -> str:
        return f"DEBUG$$> INI ADALAH {self.nama.upper()}, DENGAN JUMLAH {self.jumlah}"

    # SAMA DENGAN REPR, DIPAKAI DALAM PRODUCTION, SEDANGKAN REPR SAAT DEBUGGING
    def __str__(self) -> str:
        return f"PROD$$> INI ADALAH {self.nama.upper()}, DENGAN JUMLAH {self.jumlah}"

    # ARITMATIKA
    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    # MANIPULASI DICT
    def __dict__(self):
        pass

    # DAN MAGIC METHOD LAINNYA


mangga = Buah("Mangga", 10)
stroberi = Buah("Stroberi", 59)

print(repr(mangga))
print(mangga)

print(mangga + stroberi)
# SAMA DENGAN print(mangga.jumlah + stroberi.jumlah)
