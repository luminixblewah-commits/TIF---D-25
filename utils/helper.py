"""
Modul utilitas helper
"""
import random
import string
from datetime import datetime

def generate_id(prefix):
    """Membuat ID unik dengan prefix tertentu"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{prefix}-{timestamp}-{random_str}"

def format_tanggal(tanggal_str):
    """Memformat tanggal menjadi string yang lebih mudah dibaca"""
    try:
        tanggal = datetime.strptime(tanggal_str, "%Y-%m-%d")
        return tanggal.strftime("%d %B %Y")
    except:
        return tanggal_str

def print_header(teks):
    """Mencetak header dengan format yang rapi"""
    print("\n" + "="*60)
    print(f"{teks:^60}")
    print("="*60)

def print_menu(menu_items):
    """Mencetak menu pilihan"""
    for i, item in enumerate(menu_items, 1):
        print(f"{i}. {item}")
    print("-"*60)
