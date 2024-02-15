import time
import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from colorama import init,Fore
init(autoreset=True)

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

import random
from colorama import init, Fore

init(autoreset=True)

colors = ([m,k,h,b,u,p])
  # Farklı renk seçenekleri
selected_color = random.choice(colors)  # Rastgele bir renk seç


# API kimlik bilgilerini 'api.txt' dosyasından al
with open('api.txt', 'r') as api_file:
    api_id, api_hash = api_file.read().strip().split(',')

# Mesajı 'message.txt' dosyasından oku
with open('message.txt', 'r', encoding='utf-8') as f:
    # Dosya işlemleri burada yapılır

    message = f.read()

# Mesaj gönderim aralığı (saniye cinsinden)
message_interval = 1  # İhtiyacınıza göre bu değeri ayarlayın
group_wait_interval = 1  # Her grup arasındaki bekleme süresi (saniye)
repeat_interval = 1  # Tüm gruplara mesaj gönderildikten sonra tekrar başlama aralığı (saniye)

async def send_message(client, entity, message):
    try:
        print(selected_color + """

           \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
        

""")
        await client.send_message(entity, message)
        print(f"{entity.title} grubuna mesaj gönderildi")
    except Exception as e:
        print(f"{entity.title} grubuna mesaj gönderilirken hata oluştu: {e}")

async def join_groups(client, group_links):
    try:
        await client.start()
        print("Telegram'a giriş yapıldı.")
        await client(JoinChannelRequest('https://t.me/SorguPaneliCom'))  # Note the corrected string format
    except Exception as e:
        print(f"Error: {str(e)}")


async def main():
    client = TelegramClient('session_name', api_id, api_hash)

    # Grup linklerini 'otogrub.txt' dosyasından oku

    with open('otogrub.txt', 'r') as group_file:
        group_links = group_file.read().strip().splitlines()

    if not group_links:
        while True:
            print(selected_color + """

           \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
        

""")
            group_link = input("Lütfen bir grup linki girin veya işlemi sonlandırmak için 'bitti' yazın: ")
            if group_link.lower() == 'bitti':
                break
            group_links.append(group_link)

    await join_groups(client, group_links)

    while True:  # Sonsuz döngü
        for group_link in group_links:
            if group_link.lower() == 'bitti':
                break

            try:
                entity = await client.get_entity(group_link)
                await send_message(client, entity, message)
                await asyncio.sleep(group_wait_interval)  # Gruplar arası bekleme
            except Exception as e:
                print(f"{group_link} grubuna mesaj gönderilirken hata oluştu: {e}")

        print(f"Tüm gruplara mesaj gönderildi. {repeat_interval} saniye sonra tekrar başlayacak.")
        await asyncio.sleep(repeat_interval)  # Tekrar başlama aralığı

if __name__ == '__main__':
    asyncio.run(main())

