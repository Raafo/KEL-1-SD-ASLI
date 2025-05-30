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
    {"judul": "The Shining", "author": "Stephen King", "kategori": "Horror", "harga": 55000, "stok": 5},
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
    while True:
        judul = input("Judul buku: ")
        if judul.strip()=="":
            print("input tidak boleh kosong.")
        else:
            break
    while True:
        author = input("Nama author: ")
        if any(str.isdigit() for str in author):
            print("Nama author tidak boleh mengandung angka.")
        elif author.strip()=="":
            print("input tidak boleh kosong.")
        else:
            break
    while True:
        kategori = input("Kategori: ")
        if any(char.isdigit() for char in kategori):
            print("Kategori tidak boleh mengandung angka.")
        elif kategori.strip()=="":
            print("input tidak boleh kosong.")
        else:
            break
    while True:
        try:
            harga = int(input("Harga: Rp"))
            break
        except ValueError:
            print("Input tidak valid. Harga harus berupa angka. Coba lagi.")    
    while True:
        try:
            stok = int(input("Jumlah Stok: "))
            break
        except ValueError:
            print("Input tidak valid. Jumlah stok harus berupa angka. Coba lagi.")
            
    buku_list.append({"judul": judul, "author": author, "kategori": kategori, "harga": harga, "stok": stok})
    print(f"Buku '{judul}' berhasil ditambahkan.")
    input("Tekan Enter untuk ke menu..")

#Tambah Stok
def tambah_stok():
    clear_screen()
    list_buku()

    while True:
        try:
            idx = int(input("Pilih nomor buku: "))
            if idx < 1:
                print("\n❌ Nomor buku tidak ditemukan. Silahkan coba lagi.\n")
                continue

            # Navigasi ke node yang dimaksud
            current = buku_list.head
            count = 1
            while count < idx and current is not None:
                current = current.next
                count += 1

            if current is None:
                print("\n❌ Nomor buku tidak ditemukan. Silakan coba lagi.\n")
                continue

            # Validasi input stok tambahan
            while True:
                try:
                    tambahan = int(input("Jumlah stok yang akan ditambahkan: "))
                    if tambahan <= 0:
                        print("❌ Jumlah stok harus lebih dari 0. Coba lagi.\n")
                    else:
                        break
                except ValueError:
                    print("⚠️ Input tidak valid. Masukkan angka yang benar.\n")

            current.data['stok'] += tambahan
            print(f"\n✅ Stok buku '{current.data['judul']}' sekarang: {current.data['stok']}\n")
            break

        except ValueError:
            print("⚠️ Input tidak valid. Masukkan angka yang sesuai.\n")

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
        kategori = input("Masukkan kategori buku (Fantasy, Horror, Romance, Slice of Life): ")
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
    
    keranjang = []  # keranjang pembeli

    while True:
        list_buku()
        try:
            idx = int(input("Pilih nomor buku yang akan dijual (0 untuk selesai): "))
            if idx == 0:
                break  # Finish adding books
            if 1 <= idx <= buku_list.length():
                current = buku_list.head
                for i in range(1, idx):
                    current = current.next
                buku_dipilih = current.data

                print(f"\nAnda memilih buku: '{buku_dipilih['judul']}' - Stok: {buku_dipilih['stok']}")

                while True:
                    try:
                        jumlah = int(input("Jumlah yang akan dibeli: "))
                        if jumlah <= 0:
                            print("Jumlah harus lebih dari 0.")
                        elif buku_dipilih['stok'] < jumlah:
                            print("Stok tidak mencukupi. Silakan masukkan jumlah yang lebih kecil.")
                        else:
                            # Check if book already in cart
                            found_in_cart = False
                            for item in keranjang:
                                if item['judul'] == buku_dipilih['judul']:
                                    # Update jumlah jika sudah ada di keranjang
                                    if buku_dipilih['stok'] < item['jumlah'] + jumlah:
                                        print(f"Jumlah total melebihi stok. Maksimum yang bisa dibeli adalah {buku_dipilih['stok'] - item['jumlah']}.")
                                        break
                                    item['jumlah'] += jumlah
                                    found_in_cart = True
                                    break
                            if not found_in_cart:
                                keranjang.append({
                                    'judul': buku_dipilih['judul'],
                                    'harga': buku_dipilih['harga'],
                                    'jumlah': jumlah,
                                    'node': current  # menyimpan referensi node untuk update stok nanti
                                })
                            print(f"Berhasil menambahkan {jumlah} buku '{buku_dipilih['judul']}' ke keranjang.\n")
                            break
                    except ValueError:
                        print("Input tidak valid. Jumlah harus berupa angka. Coba lagi.")

            else:
                print("Nomor buku tidak ditemukan. Coba lagi.")
        except ValueError:
            print("Input tidak valid! Nomor buku harus berupa angka. Coba lagi.")

    if not keranjang:
        print("Keranjang kosong. Tidak ada buku yang dijual.\n")
        return

    # Hitung total harga semua buku di keranjang
    total = sum(item['harga'] * item['jumlah'] for item in keranjang)
    print("\n--- Keranjang Belanja ---")
    for item in keranjang:
        print(f"{item['judul']} - {item['jumlah']} x Rp{item['harga']} = Rp{item['harga'] * item['jumlah']}")
    print(f"Total yang harus dibayar: Rp{total}")

    while True:
        try:
            uang = int(input("Masukkan uang pembeli: Rp"))
            if uang < total:
                print("Uang tidak mencukupi. Silakan masukkan uang yang cukup.")
            else:
                kembalian = uang - total
                # Update stok dan catat riwayat penjualan
                for item in keranjang:
                    item['node'].data['stok'] -= item['jumlah']
                    riwayat_penjualan.append({
                        "judul": item['judul'],
                        "jumlah": item['jumlah'],
                        "total": item['harga'] * item['jumlah'],
                        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                global total_keuntungan
                total_keuntungan += total
                print(f"Pembayaran berhasil. Kembalian: Rp{kembalian}\n")
                break
        except ValueError:
            print("Input tidak valid. Masukkan angka dalam bentuk uang.")

    input("Tekan Enter untuk kembali ke menu...")

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
