from datetime import datetime # untuk manipulasi tanggal dan waktu

def process_dates(text):
   
    import re # Mengimpor modul regex
    
    # Pola regex untuk menemukan tanggal YYYY-MM-DD 
    polaTgl = r'\b\d{4}-\d{2}-\d{2}\b'
    tglKetemu = re.findall(polaTgl, text) # untuk mencocok tgl dengan pola dalam teks
    
    # untuk Mendapatkan tanggal hari ini
    harii = datetime.today()
    
    for i in tglKetemu:
        try:
            # untuk mengubah string tanggal menjadi objek datetime
            tgl_obj = datetime.strptime(i, '%Y-%m-%d')
            
            
            print(f"{i} 00:00:00 selisih {(harii - tgl_obj).days} hari") #Menghitung selisih hari 
        except ValueError:
            continue

# Contoh penggunaan
kalimatsoal = """
Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02).
"""

process_dates(kalimatsoal)