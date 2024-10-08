def dekripsi(input_str):
    # Menjumlahkan semua huruf
    total_pergeseran = sum(int(char) for char in input_str if char.isdigit())  
    hasil = []

    for char in input_str:
        # Jika karakter adalah alfabet
        if char.isalpha(): 
            geser = chr((ord(char.lower()) - ord('a') + total_pergeseran) % 26 + ord('a'))
            hasil.append(geser)

    return ''.join(hasil)

# Contoh penggunaan
input_str = "s8al0s5a"
output = dekripsi(input_str)
print(output)