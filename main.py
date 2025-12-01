"""
Program utama Sistem Manajemen Perpustakaan
Menggabungkan modular programming dengan OOP
"""
from database import Database
from services.manajemen_buku import ManajemenBuku
from services.manajemen_anggota import ManajemenAnggota
from services.manajemen_peminjaman import ManajemenPeminjaman
from utils.helper import print_header, print_menu
from utils.validasi import validasi_email, validasi_telepon, validasi_tahun

def main():
    # Inisialisasi database dan services
    db = Database()
    manajemen_buku = ManajemenBuku(db)
    manajemen_anggota = ManajemenAnggota(db)
    manajemen_peminjaman = ManajemenPeminjaman(db)
    
    while True:
        print_header("SISTEM MANAJEMEN PERPUSTAKAAN")
        print_menu([
            "Manajemen Buku",
            "Manajemen Anggota",
            "Peminjaman Buku",
            "Pengembalian Buku",
            "Laporan",
            "Keluar"
        ])
        
        try:
            pilihan = int(input("Pilih menu (1-6): "))
            
            if pilihan == 1:
                menu_manajemen_buku(manajemen_buku)
            elif pilihan == 2:
                menu_manajemen_anggota(manajemen_anggota)
            elif pilihan == 3:
                menu_peminjaman(manajemen_peminjaman, manajemen_buku, manajemen_anggota)
            elif pilihan == 4:
                menu_pengembalian(manajemen_peminjaman)
            elif pilihan == 5:
                menu_laporan(manajemen_buku, manajemen_anggota, manajemen_peminjaman)
            elif pilihan == 6:
                print("\nTerima kasih telah menggunakan sistem!")
                break
            else:
                print("\nPilihan tidak valid!")
        
        except ValueError:
            print("\nInput harus berupa angka!")
        except Exception as e:
            print(f"\nTerjadi kesalahan: {e}")

def menu_manajemen_buku(manajemen_buku):
    """Menu untuk manajemen buku"""
    while True:
        print_header("MANAJEMEN BUKU")
        print_menu([
            "Tambah Buku",
            "Daftar Buku",
            "Cari Buku",
            "Update Stok Buku",
            "Kembali"
        ])
        
        pilihan = int(input("Pilih menu (1-5): "))
        
        if pilihan == 1:
            print("\n--- TAMBAH BUKU BARU ---")
            judul = input("Judul Buku: ")
            penulis = input("Penulis: ")
            tahun_terbit = input("Tahun Terbit: ")
            
            if not validasi_tahun(tahun_terbit):
                print("Tahun tidak valid!")
                continue
                
            kategori = input("Kategori: ")
            stok = int(input("Stok: "))
            
            buku = manajemen_buku.tambah_buku(judul, penulis, tahun_terbit, kategori, stok)
            if buku:
                print(f"Buku berhasil ditambahkan dengan ID: {buku.get_id_buku()}")
            else:
                print("Gagal menambahkan buku!")
        
        elif pilihan == 2:
            print("\n--- DAFTAR BUKU ---")
            buku_list = manajemen_buku.daftar_buku()
            
            if not buku_list:
                print("Tidak ada buku dalam sistem.")
            else:
                for i, buku in enumerate(buku_list, 1):
                    print(f"{i}. {buku.get_judul()} - {buku.get_penulis()} (Stok: {buku.get_stok()})")
        
        elif pilihan == 3:
            keyword = input("\nMasukkan judul atau penulis: ")
            hasil = manajemen_buku.cari_buku(keyword)
            
            if not hasil:
                print("Buku tidak ditemukan.")
            else:
                print(f"Ditemukan {len(hasil)} hasil:")
                for i, buku in enumerate(hasil, 1):
                    print(f"{i}. {buku.get_judul()} - {buku.get_penulis()}")
        
        elif pilihan == 4:
            id_buku = input("\nID Buku: ")
            stok_baru = int(input("Stok Baru: "))
            
            if manajemen_buku.update_stok_buku(id_buku, stok_baru):
                print("Stok berhasil diperbarui!")
            else:
                print("Buku tidak ditemukan!")
        
        elif pilihan == 5:
            break

def menu_manajemen_anggota(manajemen_anggota):
    """Menu untuk manajemen anggota"""
    print("\nFitur manajemen anggota...")
    # Implementasi lengkap dapat ditambahkan di sini

def menu_peminjaman(manajemen_peminjaman, manajemen_buku, manajemen_anggota):
    """Menu untuk peminjaman buku"""
    print("\nFitur peminjaman buku...")
    # Implementasi lengkap dapat ditambahkan di sini

def menu_pengembalian(manajemen_peminjaman):
    """Menu untuk pengembalian buku"""
    print("\nFitur pengembalian buku...")
    # Implementasi lengkap dapat ditambahkan di sini

def menu_laporan(manajemen_buku, manajemen_anggota, manajemen_peminjaman):
    """Menu untuk laporan"""
    print("\nFitur laporan...")
    # Implementasi lengkap dapat ditambahkan di sini

if __name__ == "__main__":
    main()
