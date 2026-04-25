# Program Sistem Diskon Toko Elektronik

# Input data pembeli
nama = input("Masukkan nama pembeli: ")
status_member = input("Apakah member? (ya/tidak): ").lower()
total_belanja = float(input("Masukkan total belanja: Rp "))

# Inisialisasi variabel diskon
diskon_persen = 0

# Logika perhitungan diskon
if status_member == "ya":
    # Aturan untuk member
    if total_belanja > 500000:
        diskon_persen = 10
    elif total_belanja <= 500000:
        diskon_persen = 5
    
    # Tambahan diskon jika belanja > 100.000
    if total_belanja > 100000:
        diskon_persen += 5  # Total menjadi 15%
else:
    # Aturan untuk non-member
    if total_belanja > 100000:
        diskon_persen = 2
    else:
        diskon_persen = 0

# Hitung nominal diskon dan total bayar
nominal_diskon = total_belanja * (diskon_persen / 100)
total_bayar = total_belanja - nominal_diskon

# Tampilkan hasil
print("\n===== STRUK PEMBAYARAN =====")
print(f"Nama Pembeli   : {nama}")
print(f"Status         : {'Member' if status_member == 'ya' else 'Non-Member'}")
print(f"Total Belanja  : Rp {total_belanja:,.0f}")
print(f"Diskon         : {diskon_persen}%")
print(f"Potongan Harga : Rp {nominal_diskon:,.0f}")
print(f"Total Bayar    : Rp {total_bayar:,.0f}")
print("============================")