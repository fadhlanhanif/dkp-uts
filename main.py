# UTS Dasar Komputer dan Pemrograman
# Kelompok D - Kontrol
# Monitoring Error terhadap Setpoint

SETPOINT = 50

# 15 data inti dari soal + 5 data tambahan
data_output = [
    50, 49, 47, 45, 43,
    52, 54, 57, 51, 48,
    46, 44, 53, 55, 42,
    48, 47, 45, 56, 43
]


def hitung_error(setpoint, output):
    """Menghitung selisih absolut antara setpoint dan output."""
    return abs(setpoint - output)


def status_error(error):
    """Menentukan status sistem berdasarkan nilai error."""
    if error <= 2:
        return "STABIL"
    elif error <= 5:
        return "WARNING"
    else:
        return "TIDAK STABIL"


def rata_rata(data):
    """Menghitung rata-rata sekumpulan data."""
    return sum(data) / len(data)


def hitung_kategori(daftar_status, nama_status):
    """Menghitung jumlah kemunculan suatu status."""
    return daftar_status.count(nama_status)


def main():
    daftar_error = []
    daftar_status = []

    print("=" * 58)
    print("       MONITORING ERROR TERHADAP SETPOINT")
    print("=" * 58)
    print(f"Setpoint: {SETPOINT}")
    print("-" * 58)
    print(f"{'No.':<5}{'Output':<12}{'Error':<12}{'Status'}")
    print("-" * 58)

    # Loop memproses seluruh 20 data output
    for nomor, output in enumerate(data_output, start=1):
        error = hitung_error(SETPOINT, output)
        status = status_error(error)

        daftar_error.append(error)
        daftar_status.append(status)

        print(f"{nomor:<5}{output:<12}{error:<12}{status}")

    # Ringkasan dihitung dari seluruh 20 data
    print("-" * 58)
    print("                    RINGKASAN")
    print("-" * 58)
    print(f"Total data       : {len(data_output)}")
    print(f"Jumlah STABIL    : {hitung_kategori(daftar_status, 'STABIL')}")
    print(f"Jumlah WARNING   : {hitung_kategori(daftar_status, 'WARNING')}")
    print(f"Jumlah TIDAK STABIL: {hitung_kategori(daftar_status, 'TIDAK STABIL')}")
    print(f"Rata-rata error  : {rata_rata(daftar_error):.2f}")
    print(f"Error maksimum  : {max(daftar_error)}")
    print(f"Error minimum   : {min(daftar_error)}")
    print("=" * 58)


if __name__ == "__main__":
    main()
