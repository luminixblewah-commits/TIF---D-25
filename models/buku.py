"""
Modul untuk kelas Buku dengan konsep encapsulation
"""
class Buku:
    def __init__(self, id_buku, judul, penulis, tahun_terbit, kategori, stok):
        # Atribut private (encapsulation)
        self.__id_buku = id_buku
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun_terbit = tahun_terbit
        self.__kategori = kategori
        self.__stok = stok
    
    # Getter methods
    def get_id_buku(self):
        return self.__id_buku
    
    def get_judul(self):
        return self.__judul
    
    def get_penulis(self):
        return self.__penulis
    
    def get_tahun_terbit(self):
        return self.__tahun_terbit
    
    def get_kategori(self):
        return self.__kategori
    
    def get_stok(self):
        return self.__stok
    
    # Setter methods
    def set_judul(self, judul):
        self.__judul = judul
    
    def set_penulis(self, penulis):
        self.__penulis = penulis
    
    def set_stok(self, stok):
        self.__stok = stok
    
    def to_dict(self):
        """Mengubah objek buku menjadi dictionary"""
        return {
            'id_buku': self.__id_buku,
            'judul': self.__judul,
            'penulis': self.__penulis,
            'tahun_terbit': self.__tahun_terbit,
            'kategori': self.__kategori,
            'stok': self.__stok
        }
    
    @classmethod
    def from_dict(cls, data):
        """Membuat objek buku dari dictionary"""
        return cls(
            data['id_buku'],
            data['judul'],
            data['penulis'],
            data['tahun_terbit'],
            data['kategori'],
            data['stok']
        )
