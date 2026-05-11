import os
import sys
import time
import random
import threading

# Renkler
G = '\033[0;32m'; R = '\033[0;31m'; W = '\033[0m'; B = '\033[0;30m'; Y = '\033[0;33m'

def matrix_bg():
    """Tüm terminalden akan şeffaf görünümlü Matrix kodu"""
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    # Sütunların yükseklik takibi
    drops = [0 for _ in range(width)]
    
    while True:
        # İmleci gizle ve başa al
        sys.stdout.write("\033[?25l\033[H")
        
        output = ""
        for i in range(width):
            # Rastgele karakter seçimi (Siber gürültü)
            char = random.choice("01ABCDEFHIJKLMNOPRSTUVZ!@#$%^&*")
            
            if random.random() > 0.95: # Kodun akış hızı/yoğunluğu
                drops[i] = 0
            
            if drops[i] < height:
                # Sadece arka planda kalması için koyu yeşil/siyah dengesi
                color = G if random.random() > 0.05 else B
                output += f"{color}{char}{W}"
                drops[i] += 1
            else:
                output += " "
                drops[i] = 0 if random.random() > 0.9 else drops[i]
                
        sys.stdout.write(output + "\n")
        sys.stdout.flush()
        time.sleep(0.08)

def anka_logo_glitch():
    """Sarsıntılı ve profesyonel logo katmanı"""
    logo = [
        "   █████╗ ███╗   ██╗██╗  ██╗ █████╗ ",
        "  ██╔══██╗████╗  ██║██║ ██╔╝██╔══██╗",
        "  ███████║██╔██╗ ██║█████╔╝ ███████║",
        "  ██╔══██║██║╚██╗██║██╔═██╗ ██╔══██║",
        "  ██║  ██║██║ ╚████║██║  ██╗██║  ██║",
        "  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝"
    ]
    
    while True:
        # Logoyu ekranın ortasına/üstüne sabitlemek için konumu ayarla
        # \033[s imleci saklar, \033[u geri getirir (Matrix'i bozmamak için)
        sys.stdout.write("\033[s\033[2;0H") 
        
        chance = random.random()
        # Glitch renk paleti (Operatör'ün tercihi: Kırmızı/Yeşil/Siyah)
        color = R if chance < 0.3 else (G if chance < 0.6 else B)
        
        for line in logo:
            jitter = " " * random.randint(0, 1) if random.random() < 0.1 else ""
            sys.stdout.write(f"{jitter}{color}{line}{W}\n")
            
        sys.stdout.write(f"{Y}  [!] KOMUTA: ZoRRoKiN | Saldırgan | B0YNER{W}\n")
        sys.stdout.write("\033[u")
        sys.stdout.flush()
        time.sleep(0.1)

if __name__ == "__main__":
    os.system('clear')
    # İki efekti aynı anda çalıştır
    threading.Thread(target=matrix_bg, daemon=True).start()
    try:
        anka_logo_glitch()
    except KeyboardInterrupt:
        os.system('clear')
        sys.stdout.write("\033[?25h") # İmleci geri göster
        print("Sistem Beklemede...")
