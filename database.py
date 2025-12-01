"""
Modul untuk menyimpan data sementara (sebagai pengganti database)
"""
import json
import os

class Database:
    def __init__(self, filename='data_perpustakaan.json'):
        self.filename = filename
        self.data = self._load_data()
    
    def _load_data(self):
        """Memuat data dari file JSON"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        else:
            return {
                'buku': [],
                'anggota': [],
                'peminjaman': []
            }
    
    def save_data(self):
        """Menyimpan data ke file JSON"""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def tambah_data(self, tipe, data):
        """Menambahkan data baru"""
        if tipe in self.data:
            self.data[tipe].append(data)
            self.save_data()
            return True
        return False
    
    def get_data(self, tipe):
        """Mengambil data berdasarkan tipe"""
        return self.data.get(tipe, [])
    
    def update_data(self, tipe, index, data):
        """Memperbarui data"""
        if tipe in self.data and 0 <= index < len(self.data[tipe]):
            self.data[tipe][index] = data
            self.save_data()
            return True
        return False
