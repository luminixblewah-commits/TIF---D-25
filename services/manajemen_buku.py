"""
Modul service untuk operasi CRUD pada buku
"""
from models.buku import Buku

class ManajemenBuku:
    def __init__(self, database):
        self.db = database
    
    def tambah_buku(self, judul, penulis, tahun_terbit, kategori, stok):
        """Menambahkan buku baru ke sistem"""
        from utils.helper import generate_id
        
        id_buku = generate_id('BUK')
        buku_baru = Buku(id_buku, judul, penulis, tahun_terbit, kategori, stok)
        
        if self.db.tambah_data('buku', buku_baru.to_dict()):
            return buku_baru
        return None
    
    def daftar_buku(self):
        """Mengembalikan daftar semua buku"""
        data_buku = self.db.get_data('buku')
        buku_list = []
        
        for buku_data in data_buku:
            buku_list.append(Buku.from_dict(buku_data))
        
        return buku_list
    
    def cari_buku(self, keyword):
        """Mencari buku berdasarkan judul atau penulis"""
        hasil_pencarian = []
        data_buku = self.db.get_data('buku')
        
        for buku_data in data_buku:
            buku = Buku.from_dict(buku_data)
            if (keyword.lower() in buku.get_judul().lower() or 
                keyword.lower() in buku.get_penulis().lower()):
                hasil_pencarian.append(buku)
        
        return hasil_pencarian
    
    def update_stok_buku(self, id_buku, stok_baru):
        """Memperbarui stok buku"""
        data_buku = self.db.get_data('buku')
        
        for i, buku_data in enumerate(data_buku):
            if buku_data['id_buku'] == id_buku:
                buku = Buku.from_dict(buku_data)
                buku.set_stok(stok_baru)
                return self.db.update_data('buku', i, buku.to_dict())
        
        return False
