# data buku
class buku:
    def __init__(self, isbn, judul, pengarang, jumlah):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah
        self.terpinjam = 0
        
class pinjam:
    def __init__(self, isbn, status, tanggal_pinjam, tanggal_kembali):
        self.isbn = isbn
        self.status = status
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali


books = [
    {
        "isbn": "9786237121144",
        "judul": "Kumpulan Solusi Pemrograman Python",
        "pengarang": "Budi Raharjo",
        "jumlah": 6,
        "terpinjam": 0
    },
    {
        "isbn": "9786231800718",
        "judul": "Dasar-Dasar Pengembangan Perangkat Lunak",
        "pengarang": "Okta Purnawirawan",
        "jumlah": 15,
        "terpinjam": 0
    },
    {
        "isbn": "9786026163905",
        "judul": "Analisis dan Perancangan Sistem Informasi",
        "pengarang": "Adi Sulistyo Nugroho",
        "jumlah": 2,
        "terpinjam": 1
    },
    {
        "isbn": "9786022912828",
        "judul": "Animal Farm",
        "pengarang": "George Orwell",
        "jumlah": 4,
        "terpinjam": 0
    }
]

# data peminjaman
records = [
    {"isbn":"9786022912828",
     "status":"Selesai",
     "tanggal_pinjam":"2025-03-21",
     "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905",
     "status":"Belum",
     "tanggal_pinjam":"2025-07-22",
     "tanggal_kembali":""}
]

def tampilkan_data():
    print("---=== DATA BUKU ===---")
    print(f"{'No':<3} {'ISBN':<15} {'Judul':<45} {'Pengarang':<25} {'Jumlah':<7} {'Terpinjam':<9}")
    print("-" * 110)
    for i in range(len(books)):
        print(f"{i + 1:<3} {books[i]['isbn']:<15} {books[i]['judul']:<45} {books[i]['pengarang']:<25} {books[i]['jumlah']:<7} {books[i]['terpinjam']:<9}")

def tambah_data():
    print("menambahkan data buku")
    nama_buku = input("Masukkan nama buku: ")
    pengarang = input("Masukkan nama pengarang: ")  
    jumlah = int(input("Masukkan jumlah buku: "))
    isbn = input("Masukkan ISBN buku: ")
    buku_baru = {
        "isbn": isbn,
        "judul": nama_buku,
        "pengarang": pengarang,
        "jumlah": jumlah,
        "terpinjam": 0
    }
    books.append(buku_baru)

def edit_data():
    print("Mengedit data buku")
    tampilkan_data()
    
    index = int(input("Masukkan nomor buku yang ingin diedit: ")) - 1
    
    books[index]["judul"] = input("Masukkan judul baru: ")
    books[index]["pengarang"] = input("Masukkan pengarang baru: ")
    books[index]["jumlah"] = int(input("Masukkan jumlah baru: "))
    books[index]["isbn"] = input("Masukkan ISBN baru: ")
    print("Data buku telah diperbarui.")
    
def hapus_data():
    print("Menghapus data buku")
    tampilkan_data()
    
    index = int(input("Masukkan nomor buku yang ingin dihapus: ")) - 1
    
    books.pop(index)
    print("Data buku telah dihapus.")
def tampilkan_peminjaman():
    print("---=== DATA PEMINJAMAN ===---")
    print(f"{'No':<3} {'ISBN':<15} {'Status':<10} {'Tanggal Pinjam':<15} {'Tanggal Kembali':<15}")
    print("-" * 70)
    for i in range(len(records)):
        print(f"{i + 1:<3} {records[i]['isbn']:<15} {records[i]['status']} {records[i]['tanggal_pinjam']:<15} {records[i]['tanggal_kembali']:<15}")
def tampilkan_belum():
    print("---=== PEMINJAMAN BELUM KEMBALI ===---")
    print(f"{'No':<3} {'ISBN':<15} {'Status':<10} {'Tanggal Pinjam':<15}")
    print("-" * 50)
    for i in range(len(records)):
        if records[i]["status"] == "Belum":
            print(f"{i + 1:<3} {records[i]['isbn']:<15} {records[i]['status']:<10} {records[i]['tanggal_pinjam']:<15}")

def peminjaman():
    print("Proses peminjaman buku")
    tampilkan_data()
    
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    tanggal_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")
    
    for book in books:
        if book["isbn"] == isbn:
            if book["jumlah"] > book["terpinjam"]:
                book["terpinjam"] += 1
                records.append({
                    "isbn": isbn,
                    "status": "Belum",
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": ""
                })
                print("Buku berhasil dipinjam.")
                return
            else:
                print("Maaf, buku sudah habis.")
                return
    print("Buku tidak ditemukan.")

def pengembalian():
    print("Proses pengembalian buku")
    tampilkan_peminjaman()
    
    index = int(input("Masukkan nomor peminjaman yang ingin dikembalikan: ")) - 1
    
    if records[index]["status"] == "Belum":
        records[index]["status"] = "Selesai"
        records[index]["tanggal_kembali"] = input("Masukkan tanggal kembali (YYYY-MM-DD): ")
        
        for book in books:
            if book["isbn"] == records[index]["isbn"]:
                book["terpinjam"] -= 1
                break
        print("Buku berhasil dikembalikan.")
    else:
        print("Buku sudah dikembalikan sebelumnya.")

status = True
while status:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    match menu:
        case "1":
            tampilkan_data()
            
        case "2":
            tambah_data()
            
        case "3":
            edit_data()
            
        case "4":
            hapus_data()
            
        case "5":
            tampilkan_peminjaman()
            
        case "6":
            tampilkan_belum()
            
        case "7":
            peminjaman()
            
        case "8":
            pengembalian()
            
        case "X" | "x":
            status = False