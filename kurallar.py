import sys
import time
import os

# Renk Paleti
R = '\033[0;31m'; G = '\033[0;32m'; W = '\033[0m'; Y = '\033[0;33m'; C = '\033[0;36m'; B = '\033[0;30m'

def protocol_header():
    os.system('clear')
    print(f"{R}╔══════════════════════════════════════════════════════════╗{W}")
    print(f"{R}║ {W}      GÖVDE GÖSTERİSİ OPERASYONEL PROTOKOLLERİ       {R} ║{W}")
    print(f"{R}╚══════════════════════════════════════════════════════════╝{W}")
    print(f"{B}  [!] Güncelleme Tarihi: 02/02/2023 | Komuta: ZoRRoKiN{W}\n")

def slow_scroll(text, color=W):
    for line in text:
        sys.stdout.write(f"{C}[VERİ]{W} " + color + line + W + "\n")
        sys.stdout.flush()
        time.sleep(0.04)

def show_rules():
    protocol_header()
    
    # Protokol Listesi
    p1 = [
        "Tüm deface/data hack işlemlerinde ANKA MANİFESTOSU temeldir.",
        "Türk siteleri için Pentest yapmadan önce YAZILI ONAY şarttır.",
        "Zone-H kaydı 'ZoRRoKiN', diğerleri 'TurkHackTeam' adına alınır.",
        "İndexlerde TurkHackTeam ve Anka Red Team ibaresi ZORUNLUDUR."
    ]
    
    p2 = [
        "Devlet/Kurum/Marka dışı hedeflerde MİNİMUM 50 site sınırı vardır.",
        "Devlet ve Üniversite (.edu, .gov) için alt sınır 1 (BİR) sitedir.",
        "Upload açığı veya XSS gibi zararsız açıklar değerlendirilmez.",
        "Hacklenen sitelere iletişim adresi eklemek KESİNLİKLE YASAKTIR."
    ]

    p3 = [
        "Önemli veri/DB sızıntıları doğrudan yönetime bildirilmelidir.",
        "Sabit İndex kullanımı zorunludur. (Link: turkhackteam.org)",
        "Backdoor (Arka Kapı) bırakanlar özel çalışma ekiplerine alınır.",
        "Mesele sayı değil, ele geçirilen sistemin NİTELİĞİDİR!"
    ]

    print(f"{Y}[ BÖLÜM 1: GENEL ESASLAR ]{W}")
    slow_scroll(p1, G)
    print(f"\n{Y}[ BÖLÜM 2: LİMİTLER VE KALİTE ]{W}")
    slow_scroll(p2, W)
    print(f"\n{Y}[ BÖLÜM 3: ÖZEL OPERASYONLAR ]{W}")
    slow_scroll(p3, C)

    print(f"\n{R}--------------------------------------------------{W}")
    print(f"{R}[!] İHLAL UYARISI:{W} Türk sitelerine zarar verenler veya kart")
    print(f"hırsızlığı yapanlar ADLİ MAKAMLARA bildirilecektir.")
    print(f"{B}Link: https://www.turkhackteam.org/konular/turkhackteam-govde-gosterisi-kurallari-31-03-2023.1949863/{W}")

if __name__ == "__main__":
    show_rules()
