import socket
import datetime

def receive_file(filename, conn):
    while True:
        data = conn.recv(1024)
        if not data:
             break
        
        if data.decode() == 'File not found':
            print(f"File {filename} not found")
        else:
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            f = open(timestamp + '_copy_of_' + filename, 'wb')
            f.write(data)
            print(f"File {filename} diterima dan disimpan sebagai {timestamp}_copy_of_{filename}")

def main():
    host = '127.0.0.1'
    port = 3000
    filename = input('Masukan nama file: ')  # Change this to the file you want to request from the server
    
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send the filename request to the server
    client_socket.send(filename.encode())
    
    # Receive the file from the server
    receive_file(filename, client_socket)
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()