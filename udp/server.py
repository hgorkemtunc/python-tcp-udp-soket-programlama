import socket

host= "127.0.0.1"
port= 54321

try:
    soket=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    print("socket oluşturuldu")

    soket.bind((host, port))
    print(f"socket {port} nolu porta bağlandı")

except socket.error as msg:
    print("Bu port üzerinde bir makine açık durumda! Hata Mesajı:\n",msg)

while True:
    mesaj,address = soket.recvfrom(1024)
    print(f"Istemci'nin IP Adresi ve Port Numarası: {address}")
    print(f"Istemci'den Gelen Mesaj: {mesaj.decode('utf-8')}")
    servermesaj=mesaj.upper()

    soket.sendto(servermesaj, address)
    print("Istemci'den Gelen Mesaj Dönüştürüldü ve Gönderildi.")
