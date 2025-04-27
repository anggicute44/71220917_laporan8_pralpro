import re
import random #Untuk generate karakter acak (password)
import string

def mencariemail_passwords(text):
    
    # Pola regex untuk mencocokkan email
    pola_Email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pola_Email, text) # untuk mengembalikan semua email yang cocok dengan pola.
    
    for email in emails:
        # untul Ekstrak username (bagian sebelum @)
        username = email.split('@')[0]
        
        # Generate password random 8 karakter (huruf besar, kecil, dan angka)
        karakter = string.ascii_letters + string.digits # Gabung huruf dan angka
        password = ''.join(random.choice(karakter) for _ in range(8))# untuk gabungkan Password 8 karakter
        
        print(f"{email} username: {username}, password: {password}")

# Contoh sesuai soal
kalimat = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

mencariemail_passwords(kalimat)