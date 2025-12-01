"""
Modul service untuk operasi peminjaman dan pengembalian
"""
from models.transaksi import Transaksi
from utils.helper import generate_id

class ManajemenPeminjaman:
    def __init__(self, database):
        self.db = database
    
    def pinjam_buku(self, id_buku, id_anggota):
        """Meminjam buku"""
        # Cek ketersediaan buku
        data_buku = self.db.get_data('buku')
        buku_dipinjam = None
        buku_index = -1
        
        for i, buku in enumerate(data_buku):
            if buku['id_buku'] == id_buku and buku['stok'] > 0:
                buku_dipinjam = buku
                buku_index = i
                break
        
        if not buku_dipinjam:
            return None, "Buku tidak tersedia!"
        
        # Kurangi stok buku
        buku_dipinjam['stok'] -= 1
        self.db.update_data('buku', buku_index, buku_dipinjam)
        
        # Buat transaksi
        id_transaksi = generate_id('TRX')
        transaksi_baru = Transaksi(id_transaksi, id_buku, id_anggota)
        
        if self.db.tambah_data('peminjaman', transaksi_baru.to_dict()):
            return transaksi_baru, "Peminjaman berhasil!"
        
        return None, "Gagal mencatat transaksi!"
    
    def kembalikan_buku(self, id_transaksi):
        """Mengembalikan buku"""
        data_peminjaman = self.db.get_data('peminjaman')
        
        for i, transaksi_data in enumerate(data_peminjaman):
            if transaksi_data['id_transaksi'] == id_transaksi and transaksi_data['status'] == 'Dipinjam':
                # Update transaksi
                transaksi = Transaksi.from_dict(transaksi_data)
                denda = transaksi.kembalikan_buku()
                
                # Kembalikan stok buku
                data_buku = self.db.get_data('buku')
                for j, buku in enumerate(data_buku):
                    if buku['id_buku'] == transaksi_data['id_buku']:
                        buku['stok'] += 1
                        self.db.update_data('buku', j, buku)
                        break
                
                # Update data transaksi
                if self.db.update_data('peminjaman', i, transaksi.to_dict()):
                    return transaksi, denda
        
        return None, 0
