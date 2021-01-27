import socket                
       
host = "127.0.0.1"
port = 12345

soket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)   

mesaj= str.encode(input("Server'a gonderilecek mesajinizi giriniz: "))

try:
    soket.connect((host, port))
    soket.send(mesaj)
    
    yanit = soket.recv(1024)
    print(f"Server'dan gelen mesaj: {yanit.decode('utf8')}")

    soket.close()

except socket.error as msg:
    print("Server aktif değil, Hata Mesajı:\n", msg)
