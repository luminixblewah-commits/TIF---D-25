"""
Modul untuk kelas Transaksi
"""
from datetime import datetime, timedelta

class Transaksi:
    def __init__(self, id_transaksi, id_buku, id_anggota):
        self.__id_transaksi = id_transaksi
        self.__id_buku = id_buku
        self.__id_anggota = id_anggota
        self.__tanggal_pinjam = datetime.now().strftime("%Y-%m-%d")
        self.__tanggal_kembali = None
        self.__status = "Dipinjam"
        self.__denda = 0
    
    def kembalikan_buku(self):
        """Mengembalikan buku dan hitung denda jika terlambat"""
        self.__tanggal_kembali = datetime.now().strftime("%Y-%m-%d")
        self.__status = "Dikembalikan"
        
        # Hitung denda jika terlambat (lebih dari 7 hari)
        tanggal_pinjam = datetime.strptime(self.__tanggal_pinjam, "%Y-%m-%d")
        tanggal_kembali = datetime.strptime(self.__tanggal_kembali, "%Y-%m-%d")
        selisih_hari = (tanggal_kembali - tanggal_pinjam).days
        
        if selisih_hari > 7:
            self.__denda = (selisih_hari - 7) * 2000  # Denda Rp 2.000 per hari
        
        return self.__denda
    
    def to_dict(self):
        return {
            'id_transaksi': self.__id_transaksi,
            'id_buku': self.__id_buku,
            'id_anggota': self.__id_anggota,
            'tanggal_pinjam': self.__tanggal_pinjam,
            'tanggal_kembali': self.__tanggal_kembali,
            'status': self.__status,
            'denda': self.__denda
        }
    
    @classmethod
    def from_dict(cls, data):
        transaksi = cls(
            data['id_transaksi'],
            data['id_buku'],
            data['id_anggota']
        )
        transaksi.__tanggal_pinjam = data['tanggal_pinjam']
        transaksi.__tanggal_kembali = data['tanggal_kembali']
        transaksi.__status = data['status']
        transaksi.__denda = data['denda']
        return transaksi
