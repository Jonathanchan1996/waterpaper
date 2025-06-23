import socket

UDP_IP = "127.0.0.1"  # Listen on localhost
UDP_PORT = 5005
BUFFER_SIZE = 1024

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address
sock.bind((UDP_IP, UDP_PORT))

print(f"UDP receiver listening on {UDP_IP}:{UDP_PORT}")

try:
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)  # Receive data and sender address
        print(f"Received message: {data.decode('utf-8')} from {addr}")
except KeyboardInterrupt:
    print("\nUDP receiver stopped.")
finally:
    sock.close()