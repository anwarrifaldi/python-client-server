import socket

def send_file(filename, conn):
    with open(filename, 'rb') as f:
        data = f.read()
        conn.send(data)

def main():
    host = '127.0.0.1'
    port = 3000
    
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind to the port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    
    while True:
        # Accept a new connection
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        
        # Receive the filename request from the client
        filename = conn.recv(1024).decode()
        print(f"Client requested file: {filename}")
        
        try:
            # Send the file to the client
            send_file(filename, conn)
            print(f"File {filename} sent to client")
        except FileNotFoundError:
            print(f"File {filename} not found")
            conn.send(b"File not found")
        
        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()