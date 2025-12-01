"""
Modul service untuk operasi CRUD pada anggota
"""
from models.anggota import Anggota, AnggotaPremium
from utils.validasi import validasi_email, validasi_telepon
from utils.helper import generate_id

class ManajemenAnggota:
    def __init__(self, database):
        self.db = database
    
    def daftar_anggota(self):
        """Mengembalikan daftar semua anggota"""
        data_anggota = self.db.get_data('anggota')
        anggota_list = []
        
        for anggota_data in data_anggota:
            if anggota_data.get('tipe_anggota') == 'premium':
                anggota_list.append(AnggotaPremium.from_dict(anggota_data))
            else:
                anggota_list.append(Anggota.from_dict(anggota_data))
        
        return anggota_list
    
    def tambah_anggota(self, nama, email, no_telepon, tipe='regular'):
        """Menambahkan anggota baru"""
        if not validasi_email(email):
            return None, "Email tidak valid!"
        
        if not validasi_telepon(no_telepon):
            return None, "Nomor telepon tidak valid!"
        
        id_anggota = generate_id('AGT')
        
        if tipe == 'premium':
            anggota_baru = AnggotaPremium(id_anggota, nama, email, no_telepon, "Gold")
        else:
            anggota_baru = Anggota(id_anggota, nama, email, no_telepon)
        
        if self.db.tambah_data('anggota', anggota_baru.to_dict()):
            return anggota_baru, "Anggota berhasil ditambahkan!"
        
        return None, "Gagal menambahkan anggota!"
