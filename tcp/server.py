import socket

host = "127.0.0.1"
port = 12345

try:
    soket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    print("socket oluşturuldu")

    soket.bind((host, port)) 
    print(f"socket {port} nolu porta bağlandı")

    soket.listen(3)      
    print("socket dinleniyor")

except socket.error as msg:
    print("Bu port üzerinde bir makine açık durumda! Hata Mesajı:\n",msg)

while True:

    conn, addr = soket.accept()
    print(f"Istemci'nin IP Adresi ve Port Numarası:{addr}")

    yanit=conn.recv(1024)
    print(f"Istemci'den Gelen Mesaj: {yanit.decode('utf8')}")

    mesaj = yanit.upper()
    conn.send(mesaj)
    print("Istemci'den Gelen Mesaj Dönüştürüldü ve Gönderildi.")
    
    conn.close()
