import sys
import time
import random
import os

# Renkler
R = '\033[0;31m'; G = '\033[0;32m'; W = '\033[0m'; Y = '\033[0;33m'; B = '\033[0;30m'; C = '\033[0;36m'

def glitch_loading(text):
    chars = "!@#$%^&*()_+{}:<>?|-"
    for _ in range(10):
        glitch_str = "".join(random.choice(chars) for _ in range(5))
        sys.stdout.write(f"\r{C}[...] {W}{text} {R}{glitch_str}{W}")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"\r{G}[OK]{W} {text}                                ")

def show_ops():
    os.system('clear')
    print(f"{R}   ██████╗ ██████╗ ███████╗██████╗  █████╗ ███████╗██╗   ██╗ ██████╗ ███╗   ██╗")
    print(f"{R}  ██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝╚██╗ ██╔╝██╔═══██╗████╗  ██║")
    print(f"{Y}  ██║   ██║██████╔╝█████╗  ██████╔╝███████║███████╗ ╚████╔╝ ██║   ██║██╔██╗ ██║")
    print(f"{G}  ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║╚════██║  ╚██╔╝  ██║   ██║██║╚██╗██║")
    print(f"{G}  ╚██████╔╝██║     ███████╗██║  ██║██║  ██║███████║   ██║   ╚██████╔╝██║ ╚████║")
    print(f"{G}   ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝{W}")
    print(f"\n{B}  [!] SİSTEME ÖNEMLİ OPERASYON VERİLERİ ÇEKİLİYOR... [!]{W}\n")
    time.sleep(1)

    ops_list = [
        "WarnerBros.fr Hacked #AnkaTeam",
        "Microsoft Hacked #Comeback",
        "Hyundai.com Hacked #Gecegezen",
        "Lamborghini Hacked #jraa94",
        "Epic Games Hacked #LOEN",
        "NATO / Avrupa Parlamentosu Hacked #SaruH4N",
        "Rus Askeri Belgeleri Ele Geçirildi #OperationRu",
        "FIFA & UEFA & Premier Lig Hacked",
        "10 Kasım Data Operasyonu - 13.2M DB Leak",
        "Milli Duruş Operasyonu V1 - İL & GR Hacked",
        "Asics.com & Venum.com & Kazar.com #Op19May",
        "İsveç & Danimarka Databases Leaked",
        "Oppo Mobile & Realme Italy Hacked",
        "UNICEF & Dünya Bankası Hacked",
        "Faber-Castell & Zippo & Audi Hacked"
    ]

    for op in ops_list:
        glitch_loading(op)
        time.sleep(0.1)

    print(f"\n{R}══════════════════════════════════════════════════════════════════════{W}")
    print(f"{Y}[!] DAHA FAZLASI İÇİN ARŞİVİ ZİYARET EDİN:{W}")
    print(f"{C}LINK: {W}https://www.turkhackteam.org/forumlar/onemli-operasyonlar.431/")
    print(f"{R}══════════════════════════════════════════════════════════════════════{W}")
    
    input(f"\n{G}Ana Terminale Dönmek İçin ENTER...{W}")

if __name__ == "__main__":
    show_ops()
