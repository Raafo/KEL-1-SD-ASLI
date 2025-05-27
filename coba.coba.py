import os
from datetime import datetime

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def search_by_judul(self, judul_awal):
        current = self.head
        found = False
        while current:
            if current.data['judul'].lower().startswith(judul_awal.lower()):
                b = current.data
                print(f"Ditemukan: {b['judul']} oleh {b['author']} - [{b['kategori']}] - Rp{b['harga']} - Stok: {b['stok']}")
                found = True
            current = current.next
        if not found:
            print("Buku tidak ditemukan.")

    def filter_by_kategori(self, kategori):
        current = self.head
        result = []
        while current:
            if current.data['kategori'].lower() == kategori.lower():
                result.append(current.data)
            current = current.next
        return result

buku_list = LinkedList()

inisial_books = [
    {"judul": "Harry Potter", "author": "J.K. Rowling", "kategori": "Fantasy", "harga": 60000, "stok": 10},
    {"judul": "The Hobbit", "author": "J.R.R. Tolkien", "kategori": "Fantasy", "harga": 50000, "stok": 8},
    {"judul": "The Shining", "author": "Stephen King", "kategori": "Horor", "harga": 55000, "stok": 5},
    {"judul": "Me Before You", "author": "Jojo Moyes", "kategori": "Romance", "harga": 45000, "stok": 12},
    {"judul": "Your Name", "author": "Makoto Shinkai", "kategori": "Slice of Life", "harga": 40000, "stok": 7}
]

for book in inisial_books:
    buku_list.append(book)

#Riwayat Penjualan
riwayat_penjualan = []
total_keuntungan = 0

admin_data = {"admin": "admin123"}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Login Admin
def login():
    print("\n--- Login Admin ---")
    username = input("Username: ")
    password = input("Password: ")
    return admin_data.get(username) == password

#List Buku
def list_buku():
    clear_screen()
    print("\nStok Buku:")
    current = buku_list.head
    index = 1
    while current:
        b = current.data
        print(f"{index}. {b['judul']} oleh {b['author']} - [{b['kategori']}] - Rp{b['harga']} - Stok: {b['stok']}")
        current = current.next
        index += 1

#Tambah buku
def tambah_buku():
    clear_screen()
    judul = input("Judul buku: ")
    while True:
        author = input("Nama author: ")
        if any(char.isdigit() for char in author):
            print("Nama author tidak boleh mengandung angka.")
        else:
            break
    while True:
        kategori = input("Kategori: ")
        if any(char.isdigit() for char in kategori):
            print("Kategori tidak boleh mengandung angka.")
        else:
            break
    try:
        harga = int(input("Harga: Rp"))
        stok = int(input("Jumlah stok: "))
        buku_list.append({"judul": judul, "author": author, "kategori": kategori, "harga": harga, "stok": stok})
        print(f"Buku '{judul}' berhasil ditambahkan.\n")
    except ValueError:
        print("Input tidak valid. Harga dan stok harus berupa angka.\n")
    input("\nTekan enter untuk kembali ke menu..")

#Tambah Stok
def tambah_stok():
    clear_screen()
    list_buku()
    try:
        idx = int(input("Pilih nomor buku: "))
        tambahan = int(input("Jumlah stok yang akan ditambahkan: "))
        current = buku_list.head
        for i in range(1, idx):
            current = current.next
        current.data['stok'] += tambahan
        print(f"Stok buku '{current.data['judul']}' sekarang: {current.data['stok']}\n")
    except:
        print("Input tidak valid atau nomor buku tidak ditemukan.\n")

#Cari judul buku
def cari_judul_buku():
    clear_screen()
    while True:
        judul = input("Masukkan awal judul buku yang dicari: ")
        buku_list.search_by_judul(judul)
        lagi = input("Apakah Anda masih ingin mencari judul buku? (y/n): ")
        if lagi.lower() != 'y':
            break

#Cari kategori buku
def cari_kategori_buku():
    clear_screen()
    while True:
        kategori = input("Masukkan kategori buku: ")
        hasil = buku_list.filter_by_kategori(kategori)
        if hasil:
            for b in hasil:
                print(f"{b['judul']} oleh {b['author']} - Rp{b['harga']} - Stok: {b['stok']}")
        else:
            print("Kategori tidak ditemukan.")
        lagi = input("Apakah Anda ingin melihat kategori lain? (y/n): ")
        if lagi.lower() != 'y':
            break

#Penjualan Buku
def penjualan_buku():
    global total_keuntungan
    while True:
        list_buku()
        try:
            idx = int(input("Pilih nomor buku yang akan dijual: "))
            jumlah = int(input("Jumlah yang terjual: "))
            current = buku_list.head
            for i in range(1, idx):
                current = current.next
            if current.data['stok'] >= jumlah:
                total = jumlah * current.data['harga']
                uang = int(input(f"Total: Rp{total}. Masukkan uang pembeli: Rp"))
                if uang >= total:
                    kembalian = uang - total
                    current.data['stok'] -= jumlah
                    total_keuntungan += total
                    riwayat_penjualan.append({
                        "judul": current.data['judul'],
                        "jumlah": jumlah,
                        "total": total,
                        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    print(f"Berhasil menjual {jumlah} buku '{current.data['judul']}'. Kembalian: Rp{kembalian}\n")
                else:
                    print("Uang tidak mencukupi.\n")
            else:
                print("Stok tidak mencukupi.\n")
        except:
            print("Input tidak valid.\n")
        lagi = input("Ingin menjual buku lain? (y/n): ")
        if lagi.lower() != 'y':
            break

#Riwayat penjualan
def lihat_riwayat_penjualan():
    clear_screen()
    if not riwayat_penjualan:
        print("\nBelum ada penjualan.\n")
        return
    print("\n--- Riwayat Penjualan ---")
    for i, r in enumerate(riwayat_penjualan, 1):
        print(f"{i}. {r['waktu']} - {r['judul']} x{r['jumlah']} = Rp{r['total']}")
    print(f"\nTotal Keuntungan: Rp{total_keuntungan}\n")

#Menu admin
def menu_admin():
    while True:
        clear_screen()
        print("\n--- Menu Admin ---")
        print("1. Tambah Buku")
        print("2. Lihat Stok Buku")
        print("3. Tambah Stok Buku")
        print("4. Cari Buku Berdasarkan Judul")
        print("5. Cari Buku Berdasarkan Kategori")
        print("6. Penjualan Buku")
        print("7. Riwayat Penjualan")
        print("8. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            tambah_buku()
        elif pilih == "2":
            list_buku()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilih == "3":
            tambah_stok()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilih == "4":
            cari_judul_buku()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilih == "5":
            cari_kategori_buku()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilih == "6":
            penjualan_buku()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilih == "7":
            lihat_riwayat_penjualan()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilih == "8":
            print("Keluar dari sistem.\n")
            break
        else:
            print("Menu tidak valid.\n")
            input("\nTekan Enter untuk kembali ke menu...")

#Main Fuction
def main():
    clear_screen()
    print("=== Sistem Manajemen Buku (Admin Only) ===")
    if login():
        menu_admin()
    else:
        print("Username atau password salah.\n")

if __name__ == "__main__":
    main()
