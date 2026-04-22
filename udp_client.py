import socket

# Ganti dengan IP Ubuntu VM kamu
server_ip = "192.168.18.99"  # contoh (cek pakai ip a di VM)
server_port = 8501

# Buat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Masukkan pesan: ")

    # Kirim ke server
    client_socket.sendto(message.encode(), (server_ip, server_port))

    # Terima balasan dari server
    data, server = client_socket.recvfrom(1024)
    print("Balasan dari server:", data.decode())