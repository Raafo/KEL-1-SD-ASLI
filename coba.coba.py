import os
from datetime import datetime

buku = []

#RIWAYAT PENJUALAN
riwayat_penjualan = []
total_keuntungan = 0

#LOGIN ADMIN
admin_data = {"admin": "admin123"}

#CLEAR SCREEN
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#LOGIN ADMIN
def login():
    print("\n--- Login Admin ---")
    username = input("Username: ")
    password = input("Password: ")
    return admin_data.get(username) == password

#LIST BUKU
def list_buku():
    clear_screen()
    print("\nStok Buku:")
    for i, b in enumerate(buku, 1):
        print(f"{i}. {b['judul']} oleh {b['author']} - [{b['Genre']}] - Rp{b['harga']} - Stok: {b['stok']}")

#TAMBAH BUKU
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
        Genre = input("Genre: ")
        if any(char.isdigit() for char in Genre):
            print("Genre tidak boleh mengandung angka.")
        else:
            break
    try:
        harga = int(input("Harga: Rp"))
        stok = int(input("Jumlah stok: "))
        buku.append({"judul": judul, "author": author, "Genre": Genre, "harga": harga, "stok": stok})
        print(f"Buku '{judul}' berhasil ditambahkan.\n")
    except ValueError:
        print("Input tidak valid. Harga dan stok harus berupa angka.\n")

#TAMBHA STOK
def tambah_stok():
    clear_screen()
    list_buku()
    try:
        idx = int(input("Pilih nomor buku: ")) - 1
        tambahan = int(input("Jumlah stok yang akan ditambahkan: "))
        if 0 <= idx < len(buku):
            buku[idx]['stok'] += tambahan
            print(f"Stok buku '{buku[idx]['judul']}' sekarang: {buku[idx]['stok']}\n")
        else:
            print("Nomor buku tidak valid.\n")
    except ValueError:
        print("Input harus berupa angka.\n")

#PENJUALAN BUKU
def penjualan_buku():
    clear_screen()
    global total_keuntungan
    while True:
        list_buku()
        try:
            idx = int(input("Pilih nomor buku yang akan dijual: ")) - 1
            jumlah = int(input("Jumlah yang terjual: "))
            if 0 <= idx < len(buku):
                if buku[idx]['stok'] >= jumlah:
                    buku[idx]['stok'] -= jumlah
                    total = jumlah * buku[idx]['harga']
                    total_keuntungan += total
                    riwayat_penjualan.append({
                        "judul": buku[idx]['judul'],
                        "jumlah": jumlah,
                        "total": total,
                        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    print(f"Berhasil menjual {jumlah} buku '{buku[idx]['judul']}'. Total: Rp{total}\n")
                else:
                    print("Stok tidak mencukupi.\n")
            else:
                print("Nomor buku tidak valid.\n")
        except ValueError:
            print("Input harus berupa angka.\n")

        lagi = input("Ingin menjual buku lain? (y/n): ")
        if lagi.lower() != 'y':
            break

#RIWAYAT PENJUALAN
def lihat_riwayat_penjualan():
    clear_screen()
    if not riwayat_penjualan:
        print("\nBelum ada penjualan.\n")
        return
    print("\n--- Riwayat Penjualan ---")
    for i, r in enumerate(riwayat_penjualan, 1):
        print(f"{i}. {r['waktu']} - {r['judul']} x{r['jumlah']} = Rp{r['total']}")
    print(f"\nTotal Keuntungan: Rp{total_keuntungan}\n")

#MENU ADMIN
def menu_admin():
    while True:
        clear_screen()
        print("\n--- Menu Admin ---")
        print("1. Tambah Buku")
        print("2. Lihat Stok Buku")
        print("3. Tambah Stok Buku")
        print("4. Penjualan Buku")
        print("5. Riwayat Penjualan")
        print("6. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            tambah_buku()
        elif pilih == "2":
            list_buku()
            input("\nTekan Enter untuk ke menu")
        elif pilih == "3":
            tambah_stok()
            input("\nTekan Enter untuk ke menu")
        elif pilih == "4":
            penjualan_buku()
            input("\nTekan Enter untuk ke menu")
        elif pilih == "5":
            lihat_riwayat_penjualan()
            input("\nTekan Enter untuk ke menu")
        elif pilih == "6":
            print("Keluar dari sistem.\n")
            break
        else:
            print("Menu tidak valid.\n")
            input("\nTekan Enter untuk ke menu")

#MAIN FUNCTION
def main():
    clear_screen()
    print("=== Sistem Manajemen Buku (Admin Only) ===")
    if login():
        menu_admin()
    else:
        print("Username atau password salah.\n")

if __name__ == "__main__":
    main()
