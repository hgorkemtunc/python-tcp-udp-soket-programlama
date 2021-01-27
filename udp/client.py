import socket

host="127.0.0.1"
port=54321

soket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

mesaj=str.encode(input("Server'a gonderilecek mesajinizi giriniz: "))

try:
    soket.sendto(mesaj, (host,port))

    yanit = soket.recvfrom(1024)
    print(f"Server'dan gelen mesaj: {yanit[0].decode('utf-8')}")

except socket.error as msg:
    print("Server aktif degil, Mesaj:\n",msg)
