import random
import time
import sys

# Renk tanımları
R = '\033[0;31m'; G = '\033[0;32m'; Y = '\033[0;33m'; C = '\033[0;36m'; W = '\033[0m'

def draw_glitch_guide():
    """
    Ekranın boş bir yerine yanıp sönen, glitch efektli rehber kutusu basar.
    """
    # Glitch için rastgele karakterler ve renkler
    glitch_chars = ["!", "@", "#", "$", "%", "&", "*"]
    colors = [R, G, Y, C]
    c = random.choice(colors)
    g = random.choice(glitch_chars)

    guide = [
        f"{c}╔═════════ {g} SALDIRI REHBERİ {g} ═════════╗{W}",
        f"{c}║{W}  1. Modül numarasını seç (01-50)   {c}║{W}",
        f"{c}║{W}  2. Hedef URL'yi eksiksiz gir      {c}║{W}",
        f"{c}║{W}  3. 'ankamap.py' otomatik tetiklenir{c}║{W}",
        f"{c}║{W}  {R}[!] Örnek: http://hedef-site.com/ {c}║{W}",
        f"{c}╚══════════════════════════════════════╝{W}"
    ]

    # Kutuyu her seferinde aynı yere basmak için ANSI kaçış kodları kullanılabilir
    # Veya ana menünün altına/üstüne ekleyebilirsin.
    for line in guide:
        print(f"  {line}")

def fix_tarihce_error():
    """
    Ekran görüntüsündeki 'speed' hatasını düzeltmek için ipucu.
    """
    print(f"\n{Y}[!] Hata Düzeltme Notu:{W}")
    print(f"{C}tarihce.py içindeki glitch_effect(title, speed=0.05) satırını")
    print(f"glitch_effect(title) olarak değiştirin. 'speed' argümanı silinmeli.{W}")

