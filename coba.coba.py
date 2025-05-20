from datetime import datetime

buku = []

#RIWAYAT PENJUALAN
riwayat_penjualan = []
total_keuntungan = 0

#LOGIN ADMIN
admin_data = {"admin": "admin123"}

def login():
    print("\n--- Login Admin ---")
    username = input("Username: ")
    password = input("Password: ")
    if admin_data.get(username) == password:
        return True
    else:
        print("Login gagal.")
        return False

#LIST BUKU
def list_buku():
    print("\nStok Buku:")
    for i, b in enumerate(buku, 1):
        print(f"{i}. {b['judul']} oleh {b['author']} - [{b['Genre']}] - Rp{b['harga']} - Stok: {b['stok']}")

#TAMBAH BUKU
def tambah_buku():
    judul = input("Judul buku: ")
    while True:
        author = input("Nama author: ")
        if any(char.isdigit() for char in author):
            print("Nama author tidak boleh mengandung angka. Coba lagi.")
        else:
            break
    while True:
        Genre = input("Kategori: ")
        if any(char.isdigit() for char in Genre):
            print("Kategori tidak boleh mengandung angka. Coba lagi.")
        else:
            break
    try:
        harga = int(input("Harga: Rp"))
        stok = int(input("Jumlah stok: "))
        buku.append({"judul": judul, "author": author, "Genre": Genre, "harga": harga, "stok": stok})
        print(f"Buku '{judul}' berhasil ditambahkan.")
    except:
        print("Input tidak valid. Pastikan harga dan stok berupa angka.")

#TAMBAH STOK
def tambah_stok():
    list_buku()
    try:
        idx = int(input("Pilih nomor buku untuk menambah stok: ")) - 1
        tambahan = int(input("Jumlah stok yang akan ditambahkan: "))
        if 0 <= idx < len(buku):
            buku[idx]['stok'] += tambahan
            print(f"Stok buku '{buku[idx]['judul']}' ditambah {tambahan}. Total stok: {buku[idx]['stok']}")
        else:
            print("Nomor buku tidak valid.")
    except:
        print("Input tidak valid.")

#PENJUALAN BUKU
def penjualan_buku():
    global total_keuntungan
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
                print(f"Berhasil menjual {jumlah} buku '{buku[idx]['judul']}'. Total: Rp{total}")
            else:
                print("Stok tidak mencukupi.")
        else:
            print("Nomor buku tidak valid.")
    except:
        print("Input tidak valid.")

#LIHAT RIWAYAT PENJUALAN
def lihat_riwayat_penjualan():
    if not riwayat_penjualan:
        print("\nBelum ada penjualan.")
        return
    print("\n--- Riwayat Penjualan ---")
    for i, r in enumerate(riwayat_penjualan, 1):
        print(f"{i}. {r['waktu']} - {r['judul']} x{r['jumlah']} = Rp{r['total']}")
    print(f"\nTotal Keuntungan: Rp{total_keuntungan}")

#MENU ADMIN
def menu_admin():
    while True:
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
        elif pilih == "3":
            tambah_stok()
        elif pilih == "4":
            penjualan_buku()
        elif pilih == "5":
            lihat_riwayat_penjualan()
        elif pilih == "6":
            print("Keluar dari sistem.")
            break
        else:
            print("Menu tidak valid.")

#MAIN FUNCTION
def main():
    print("=== Sistem Manajemen Buku (Admin Only) ===")
    if login():
        menu_admin()

if __name__ == "__main__":
    main()
