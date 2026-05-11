import sys, time, random, os
R = '\033[0;31m'; W = '\033[0m'; Y = '\033[0;33m'

def glitch_effect(text, color=W, delay=0.03):
    """Burada 'speed' parametresi silindi, hata giderildi."""
    chars = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿"
    for char in text:
        if random.random() < 0.1:
            sys.stdout.write(R + random.choice(chars) + W)
            sys.stdout.flush(); time.sleep(0.01)
        sys.stdout.write(color + char + W)
        sys.stdout.flush(); time.sleep(delay)
    print()

def show_history():
    os.system('clear')
    print(f"{R}   [ THT TARİHÇESİ - LEGACY ]{W}\n")
    data = [
        (Y + "2002: KURULUŞ", ["Vatansever kadro ile ZoRRoKiN komutasında siber ordu kuruldu."]),
        (W + "2015: ANKA RED TEAM", ["Saldırı timleri 'Anka' ismiyle profesyonelleşti."])
    ]
    for t, c in data:
        glitch_effect(t, speed=0.05) # BU SATIR HATA VERİYORDU
        # BU SATIRIN DÜZELTİLMİŞ HALİ:
        # glitch_effect(t, delay=0.05)
        for line in c:
            glitch_effect(line, delay=0.02)
        print()
if __name__ == "__main__":
    show_history()
