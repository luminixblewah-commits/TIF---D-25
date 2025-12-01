"""
Modul untuk validasi input
"""
import re

def validasi_email(email):
    """Memvalidasi format email"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validasi_telepon(no_telepon):
    """Memvalidasi format nomor telepon"""
    pattern = r'^[0-9]{10,13}$'
    return re.match(pattern, no_telepon) is not None

def validasi_tahun(tahun):
    """Memvalidasi tahun"""
    try:
        tahun_int = int(tahun)
        return 1000 <= tahun_int <= 2100
    except:
        return False
