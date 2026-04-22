import socket

# Konfigurasi server
server_ip = "0.0.0.0"   
server_port = 8501

# Buat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind ke IP dan port
server_socket.bind((server_ip, server_port))

print(f"Server UDP berjalan di {server_ip}:{server_port}")

while True:
    # Terima data dari client
    data, addr = server_socket.recvfrom(1024)
    print(f"Pesan dari {addr}: {data.decode()}")

    # Kirim balasan ke client
    response = "Pesan diterima oleh server"
    server_socket.sendto(response.encode(), addr)