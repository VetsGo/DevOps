import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 4284

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"StatsD-мок сервер запущено на {UDP_IP}:{UDP_PORT}")
print("Очікуємо повідомлення...\n")

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Отримано повідомлення від {addr}: {data.decode()}")