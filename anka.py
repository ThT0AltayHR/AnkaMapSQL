import os
import sys
import time
import random
import threading

# Renk Paleti
R = '\033[0;31m'; G = '\033[0;32m'; W = '\033[0m'; Y = '\033[0;33m'; B = '\033[0;30m'; C = '\033[0;36m'; P = '\033[0;35m'
stop_threads = False

def matrix_bg():
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    drops = [0 for _ in range(width)]
    while not stop_threads:
        sys.stdout.write("\033[?25l\033[s\033[H")
        out = ""
        for i in range(width):
            char = random.choice("01ABCDEFHIJKLMNOPRSTUVZ!@#$%^&*")
            if random.random() > 0.97: drops[i] = 0
            if drops[i] < height:
                color = G if random.random() > 0.08 else B
                out += f"{color}{char}{W}"
                drops[i] += 1
            else:
                out += " "
                drops[i] = 0 if random.random() > 0.9 else drops[i]
        sys.stdout.write(out + "\n\033[u")
        sys.stdout.flush()
        time.sleep(0.1)

def massive_logo_glitch():
    """Ekranı kaplayan devasa ASCII Logo ve Titreyen Yazılar"""
    logo = [
        "   █████╗ ███╗   ██╗██╗  ██╗ █████╗ ",
        "  ██╔══██╗████╗  ██║██║ ██╔╝██╔══██╗",
        "  ███████║██╔██╗ ██║█████╔╝ ███████║",
        "  ██╔══██║██║╚██╗██║██╔═██╗ ██╔══██║",
        "  ██║  ██║██║ ╚████║██║  ██╗██║  ██║",
        "  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝",
        " ██████╗ ███████╗██████╗ ",
        " ██╔══██╗██╔════╝██╔══██╗",
        " ██████╔╝█████╗  ██║  ██║",
        " ██╔══██╗██╔══╝  ██║  ██║",
        " ██║  ██║███████╗██████╔╝",
        " ╚═╝  ╚═╝╚══════╝╚═════╝ ",
        " [ T E A M ] TÜRKİYENİN SİBER GÜCÜ"
        "türkhackteam.org Resmi karargah"
    ]
    texts = [
        "HACKED BY TÜRK HACK TEAM",
        "HACKED BY ANKA RED TEAM",
        "HELLO ADMIN SYSTEM HACKED!",
        "ZoRRoKiN - B0yner - Saldırgan",
        "SQL SERVER CONNECTED",
        "Site mi hackledin al index benden",
        "https://tht0altayhr.github.io/Anka-Red-Team-lndex/",
        "unutmadan sql yapabilmek için aracı durdur ve python3 ankamap.py (sqlmap)",
    ]
    
    while not stop_threads:
        sys.stdout.write("\033[s\033[2;0H") # Logonun başlangıç yeri
        color = R if random.random() < 0.4 else (G if random.random() < 0.7 else B)
        
        # Devasa Logoyu Bas
        for line in logo:
            jitter = " " if random.random() < 0.05 else ""
            sys.stdout.write(f"{jitter}{color}{line}{W}\n")
            
        sys.stdout.write("\n")
        
        # Titreyen ve Yanıp Sönen Metinleri Bas
        for text in texts:
            t_color = random.choice([R, G, Y, W])
            blink = "\033[5m" if random.random() < 0.2 else "" # Yanıp sönme efekti
            glitch = "".join(random.choice("!@#$%^&*") for _ in range(3))
            sys.stdout.write(f"  {blink}{t_color}>> {text} << {R}{glitch}{W}\n")

        sys.stdout.write("\033[u")
        sys.stdout.flush()
        time.sleep(0.1)

def glitch_btn(num, text, color=G):
    chars = "!@#%"
    g = "".join(random.choice(chars) for _ in range(2))
    return f"{R}[{num}]{W} {color}>-- {text:<30} --<{W} {R}{g}{W}"

# 50 MODÜL SÖZLÜĞÜ (Kısaltılmış Görüntü - Kod aynı)
modules = {
    "1": [("01", "Veritabanlarını Listele"), ("02", "Tabloları Çek"), ("03", "Kolonları İncele"), ("04", "Veri Dök (Dump)"), ("05", "Sürüm Analizi"), ("06", "Kullanıcı İncele"), ("07", "Hedef DBS"), ("08", "Yetki Oku"), ("09", "Roller"), ("10", "Full Scan")],
    "2": [("11", "Space2Comment Bypass"), ("12", "RandomCase Tamper"), ("13", "Level 5 Taarruz"), ("14", "Risk 3 Modu"), ("15", "Null Conn"), ("16", "Hex Encode"), ("17", "Charencode"), ("18", "Union Sızma"), ("19", "Error Sızma"), ("20", "Sessiz Sızma")],
    "3": [("21", "OS-Shell Başlat"), ("22", "OS-Pwn Tam Kontrol"), ("23", "/etc/passwd Oku"), ("24", "Dosya Yaz"), ("25", "Reg Oku"), ("26", "Reg Yaz"), ("27", "SQL-Shell"), ("28", "Meterpreter"), ("29", "VNC Aç"), ("30", "UDF Enjekte")],
    "4": [("31", "Admin Panel Bul"), ("32", "Hash Kırıcı"), ("33", "Ortak Tablo Brute"), ("34", "Kolon Brute"), ("35", "XSS Analizi"), ("36", "LFI/RFI Testi"), ("37", "WAF Tespiti"), ("38", "İpucu Çıkarma"), ("39", "Zorla Çek"), ("40", "Full Döküm")],
    "5": [("41", "Tor Bağlantısı"), ("42", "Fake User-Agent"), ("43", "Proxy Zinciri"), ("44", "Mobil Taklit"), ("45", "API Gizleme"), ("46", "CSRF Bypass"), ("47", "Keep-Alive"), ("48", "Cookie Enjekte"), ("49", "Stealth Mod"), ("50", "Hayalet Mod")]
}

def animate_text(text, color=W, delay=0.015):
    """Hacker terminali tarzı daktilo efekti"""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def archive_room():
    """Özenle hazırlanmış, animasyonlu Disiplin Odası"""
    while True:
        os.system('clear')
        print(f"\n{R}╔═════════════[ 📜 ARŞİV VE DİSİPLİN ODASI ]═════════════╗{W}")
        print(f"║  {glitch_btn('H', 'ŞANLI THT TARİHÇESİ', W)}       ║")
        print(f"║  {glitch_btn('M', 'ANKA TEAM MANİFESTO', W)}       ║")
        print(f"║  {glitch_btn('K', 'GÖVDE GÖSTERİSİ KURALLARI', W)} ║")
        print(f"║  {glitch_btn('G', 'ANA MENÜYE DÖN', Y)}            ║")
        print(f"{R}╚════════════════════════════════════════════════════════╝{W}")
        
        cmd = input(f"\n  {G}Okunacak Belge {R}> {W}").upper()
        if cmd == 'G': break
        
        os.system('clear')
        if cmd == 'H':
            animate_text("\n[>>] SİSTEM ARŞİVİNE ERİŞİLİYOR: THT TARİHÇESİ...", R, 0.03)
            time.sleep(0.5)
            animate_text("\n2002 yılında, vatansever bir kadro ile Türk siber sahasını savunmak", W)
            animate_text("ve dış tehditlere karşı taarruz etmek amacıyla Türk Hack Team kuruldu.", W)
            animate_text("ZoRRoKiN komutasında şekillenen bu yapı, yıllar içinde devasa bir", W)
            animate_text("siber orduya dönüştü. Operasyonlar, sadece defansif değil;", R)
            animate_text("tamamen ofansif ve yıkıcı stratejiler üzerine kuruldu.", R)
            
        elif cmd == 'M':
            animate_text("\n[>>] SİSTEM ARŞİVİNE ERİŞİLİYOR: ANKA MANİFESTO...", R, 0.03)
            time.sleep(0.5)
            animate_text("\n1. Hedef sistemin büyüklüğü fark etmeksizin sızılır ve yok edilir.", Y)
            animate_text("2. İz bırakılmaz, sistemin kalbine inilir.", Y)
            animate_text("3. Türk devletinin ve milletinin aleyhine iş yapan her platform", Y)
            animate_text("   Anka Red Team'in doğal hedefidir.", R)
            animate_text("4. B0yner, Saldırgan ve ZoRRoKiN'in açtığı yoldan ilerlenir.", Y)
            
        elif cmd == 'K':
            animate_text("\n[>>] SİSTEM ARŞİVİNE ERİŞİLİYOR: KURALLAR...", R, 0.03)
            time.sleep(0.5)
            animate_text("\n[!] GÖVDE GÖSTERİSİ (ZONE) ADABI:", C)
            animate_text("- Alınan her sistemin ana sayfasına mutlaka index basılacaktır.", W)
            animate_text("- İndexte 'Turk Hack Team' ve 'Anka Red Team' ibaresi zorunludur.", W)
            animate_text("- Kişisel çıkar için sistem vurmak, şantaj yapmak kesinlikle YASAKTIR.", R)
            
        input(f"\n{G}[+] Okuma Tamamlandı. Geri Dönmek İçin ENTER...{W}")

def draw_main_menu():
    os.system('clear')
    print("\n" * 26) # Devasa başlık için ekranın altına in
    print(f"  {C}╔═════════════[ ⚔️ ANA KATALOG ⚔️ ]═══════════════════╗{W}")
    print(f"  ║  {glitch_btn('1', 'TEMEL SIZMA & DB TARAMA', Y)}  ║")
    print(f"  ║  {glitch_btn('2', 'ZoRRoKiN WAF BYPASS MODU', R)}  ║")
    print(f"  ║  {glitch_btn('3', 'B0YNER SİSTEM ENJEKSİYONU', C)}  ║")
    print(f"  ║  {glitch_btn('4', 'SALDIRGAN İNFAZ PROTOKOLÜ', G)}  ║")
    print(f"  ║  {glitch_btn('5', 'GİZLİ SERVİS & TOR AĞI', P)}  ║")
    print(f"  {C}╚════════════════════════════════════════════════════╝{W}")
    print(f"\n  {Y}╔═════════════[ 📜 ARŞİV ODASI ]═════════════════════╗{W}")
    print(f"  ║  {glitch_btn('A', 'Tarihçe / Manifesto / Kurallar', W)}  ║")
    print(f"  {Y}╚════════════════════════════════════════════════════╝{W}")
    print(f"\n  {R}[00] >-- SİSTEMDEN AYRIL --<{W}")

def draw_sub_menu(cat_id, title, color):
    os.system('clear'); print("\n" * 26)
    print(f"  {color}╔═════════════[ {title} ]═════════════════╗{W}")
    for num, name in modules[cat_id]:
        print(f"  ║  {glitch_btn(num, name, color)}  ║")
    print(f"  {color}╚════════════════════════════════════════════════════════════╝{W}")
    print(f"\n  {Y}[G] >-- ANA MENÜYE DÖN --<{W}")

def main():
    global stop_threads
    threading.Thread(target=matrix_bg, daemon=True).start()
    threading.Thread(target=massive_logo_glitch, daemon=True).start()
    
    while True:
        draw_main_menu()
        choice = input(f"\n  {G}Operatör {R}> {W}").upper()
        
        if choice == '00': break
        elif choice == 'A':
            stop_threads = True; time.sleep(0.3)
            archive_room()
            stop_threads = False
            threading.Thread(target=matrix_bg, daemon=True).start()
            threading.Thread(target=massive_logo_glitch, daemon=True).start()
            
        elif choice in ["1", "2", "3", "4", "5"]:
            titles = {"1":"TEMEL SIZMA", "2":"ZoRRoKiN WAF", "3":"B0YNER SIZMA", "4":"SALDIRGAN İNFAZ", "5":"GİZLİLİK"}
            colors = {"1":Y, "2":R, "3":C, "4":G, "5":P}
            while True:
                draw_sub_menu(choice, titles[choice], colors[choice])
                sub_choice = input(f"\n  {G}Modül Seç {R}> {W}").upper()
                if sub_choice == 'G': break
                else:
                    stop_threads = True; time.sleep(0.3); os.system('clear')
                    print(f"\n{R}[!] HEDEF SEÇİLDİ: Modül {sub_choice}{W}")
                    url = input(f"{C}Hedef URL: {W}")
                    print(f"{R}[+] Saldırı İnfaz Ediliyor... Lütfen Bekleyin.{W}")
                    time.sleep(2)
                    stop_threads = False
                    threading.Thread(target=matrix_bg, daemon=True).start()
                    threading.Thread(target=massive_logo_glitch, daemon=True).start()

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: sys.exit()
