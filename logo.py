import sys
import time
import random
import os

# Renkler
R = '\033[0;31m'; G = '\033[0;32m'; W = '\033[0m'; B = '\033[0;30m'; Y = '\033[0;33m'

def glitch_engine():
    # ANA DEVASA LOGO
    main_logo = [
        "   █████╗ ███╗   ██╗██╗  ██╗ █████╗        ███████╗",
        "  ██╔══██╗████╗  ██║██║ ██╔╝██╔══██╗       ██╔════╝",
        "  ███████║██╔██╗ ██║█████╔╝ ███████║       ███████╗",
        "  ██╔══██║██║╚██╗██║██╔═██╗ ██╔══██║       ╚════██║",
        "  ██║  ██║██║ ╚████║██║  ██╗██║  ██║       ███████║",
        "  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚══════╝"
    ]
    
    # MİNYATÜR İMZALAR VE MESAJLAR (Glitch Odaklı)
    signatures = [
        "[ HACKED BY ANKA RED TEAM ]",
        "[ HACKED BY TURK HACK TEAM ]",
        "[ HELLO ADMIN SYSTEM HACKED ! ]",
        "-------------------------------",
        "   - ZoRRoKiN -   ",
        "   - SALDIRGAN -  ",
        "   - B0YNER -     "
    ]

    os.system('clear')
    try:
        while True:
            chance = random.random()
            # Glitch Renk Dinamiği
            if chance < 0.12: color = B # Siyah Parazit
            elif chance < 0.45: color = R # Agresif Kırmızı
            elif chance < 0.80: color = G # Siber Yeşil
            else: color = W # Beyaz Şok

            sys.stdout.write("\033[H")
            
            # Ana Logo Basımı (Titremeli)
            for line in main_logo:
                jitter = " " * random.randint(0, 1) if random.random() < 0.1 else ""
                sys.stdout.write(f"{color}{jitter}{line}{W}\n")
            
            sys.stdout.write(f"\n{color}      ══════════════════════════════════════════      {W}\n")

            # Minyatür İmza Bloğu (Her satır ayrı glitchlenebilir)
            for sig in signatures:
                # Rastgele karakter bozma (Siber gürültü)
                if random.random() < 0.05:
                    sig_alt = sig.replace("A", "@").replace("E", "3").replace("I", "1").replace("S", "5")
                    sys.stdout.write(f"  {Y}>> {R}{sig_alt}{W}\n")
                else:
                    # İsimler ve Mesajlar için dinamik renk
                    sig_color = color if color != B else B
                    jitter = " " * random.randint(0, 3) if random.random() < 0.15 else "  "
                    sys.stdout.write(f"{jitter}{sig_color}{sig}{W}\n")

            sys.stdout.flush()
            time.sleep(0.06) # Profesyonel, hızlı akış

    except KeyboardInterrupt:
        os.system('clear')
        print(f"\n{G}[+] Mühür Basıldı. Operasyon Hazır.{W}\n")

if __name__ == "__main__":
    glitch_engine()
