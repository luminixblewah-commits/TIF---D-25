"""
Modul untuk kelas Anggota dengan inheritance
"""
from datetime import datetime, timedelta

class Anggota:
    def __init__(self, id_anggota, nama, email, no_telepon):
        self.__id_anggota = id_anggota
        self.__nama = nama
        self.__email = email
        self.__no_telepon = no_telepon
        self.__tanggal_daftar = datetime.now().strftime("%Y-%m-%d")
        self.__status = "Aktif"
    
    # Getter methods
    def get_id_anggota(self):
        return self.__id_anggota
    
    def get_nama(self):
        return self.__nama
    
    def get_email(self):
        return self.__email
    
    def get_status(self):
        return self.__status
    
    # Setter methods
    def set_status(self, status):
        self.__status = status
    
    def to_dict(self):
        return {
            'id_anggota': self.__id_anggota,
            'nama': self.__nama,
            'email': self.__email,
            'no_telepon': self.__no_telepon,
            'tanggal_daftar': self.__tanggal_daftar,
            'status': self.__status
        }
    
    @classmethod
    def from_dict(cls, data):
        anggota = cls(
            data['id_anggota'],
            data['nama'],
            data['email'],
            data['no_telepon']
        )
        anggota.__tanggal_daftar = data['tanggal_daftar']
        anggota.__status = data['status']
        return anggota


# Inheritance: AnggotaPremium mewarisi dari Anggota
class AnggotaPremium(Anggota):
    def __init__(self, id_anggota, nama, email, no_telepon, level_premium):
        super().__init__(id_anggota, nama, email, no_telepon)
        self.__level_premium = level_premium
        self.__batas_pinjaman = 10  # Anggota premium bisa pinjam lebih banyak
        self.__masa_berlaku = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
    
    def get_batas_pinjaman(self):
        return self.__batas_pinjaman
    
    def get_level_premium(self):
        return self.__level_premium
    
    def get_masa_berlaku(self):
        return self.__masa_berlaku
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'level_premium': self.__level_premium,
            'batas_pinjaman': self.__batas_pinjaman,
            'masa_berlaku': self.__masa_berlaku,
            'tipe_anggota': 'premium'
        })
        return data
    
    @classmethod
    def from_dict(cls, data):
        anggota = cls(
            data['id_anggota'],
            data['nama'],
            data['email'],
            data['no_telepon'],
            data['level_premium']
        )
        anggota.__batas_pinjaman = data['batas_pinjaman']
        anggota.__masa_berlaku = data['masa_berlaku']
        return anggota
