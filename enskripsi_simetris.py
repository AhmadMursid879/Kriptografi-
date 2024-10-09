def enkrip(pesan, shift):
    abjad = "abcdefghijklmnopqrstuvwxyz"  # Menggunakan huruf kecil
    cipher = ""

    for char in pesan:
        if char in abjad:
            index = abjad.find(char)
            shifted_index = (index + shift) % len(abjad)
            cipher += abjad[shifted_index]
        else:
            cipher += char  # Menambahkan karakter non-huruf

    return cipher

# Masukkan pesan yang ingin dienkripsi
pesan = input("Masukkan pesan yang ingin dienkripsi: ").lower()
shift = int(input("Masukkan jumlah penggeseran (misal: 3): "))

encrypted_message = enkrip(pesan, shift)
print("Pesan yang terenkripsi:", encrypted_message)