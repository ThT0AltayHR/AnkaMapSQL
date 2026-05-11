import sys
import time
import random
import os

# Renkler
R = '\033[0;31m'; G = '\033[0;32m'; W = '\033[0m'; Y = '\033[0;33m'; B = '\033[0;30m'; C = '\033[0;36m'

def slow_print(text, speed=0.03, color=W):
    for char in text:
        sys.stdout.write(color + char + W)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def glitch_mini_logo():
    color = random.choice([R, G, Y])
    print(f"{color}   [ ANKA RED TEAM MANİFESTOSU ]   {W}")
    print(f"{color}═════════════════════════════════════{W}")

def show_manifesto():
    os.system('clear')
    glitch_mini_logo()
    print(f"\n{C}[!] KOMUTA ZİNCİRİ: {Y}ZoRRoKiN | Saldırgan | B0YNER{W}\n")
    
    sections = [
        (Y + "■ ANKA RED TEAM NEDİR?" + W, [
            "Anka Red Team; hacking & siber güvenlik alanında misyonumuza",
            "bağlı olarak faaliyetlerini sürdürür. Adı gibi küllerinden",
            "yeniden doğan, disiplin ve hiyerarşi odaklı bir ekiptir."
        ]),
        (R + "■ TEMEL GÖREVLERİMİZ" + W, [
            "- Türk Devletlerinin ulusal çıkarlarını korumak.",
            "- Diplomatik duruş sergileyerek 'Düşman' sistemlere mesaj iletmek.",
            "- Vatan topraklarına ve müttefiklere ait sistemleri korumak.",
            "- Bilgili ve bilinçli bir nesil yetişmesine katkı sağlamak."
        ]),
        (G + "■ KIRMIZI ÇİZGİLERİMİZ (NE YAPMAYIZ?)" + W, [
            "- Müttefik ülkelere asla saldırı düzenlemeyiz.",
            "- Kişisel verileri (Kredi kartı, özel hayat) ifşa etmeyiz.",
            "- Para karşılığı iş yapmayız; bizim parayla işimiz olmaz.",
            "- Hiçbir siyasi oluşuma hizmet etmeyiz; tek odak 'TÜRK DEVLETİ'dir."
        ]),
        (B + "--------------------------------------------------" + W, [
            "  'Motto: Türk Devletlerinin Ulusal Çıkarları İçin!'  "
        ])
    ]

    for title, lines in sections:
        slow_print(title, 0.05)
        for line in lines:
            # Satır başlarına siber efekt ekle
            sys.stdout.write(f"{C} [PROT-LOG] {W}")
            slow_print(line, 0.02)
        print()
        time.sleep(0.5)

    print(f"\n{G}[+] Manifesto başarıyla yüklendi. Operasyona hazır mısın, Operatör?{W}")
    print(f"{B}Link: https://www.turkhackteam.org/konular/anka-red-team-manifestosu.1944870/{W}")

if __name__ == "__main__":
    show_manifesto()
