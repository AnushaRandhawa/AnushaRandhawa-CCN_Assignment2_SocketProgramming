import socket
import time
import logging


logging.basicConfig(
    filename='tcp_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Server config
HOST = '127.0.0.1'  # localhost
PORT = 65432

def start_server():
    """Start the TCP server and handle incoming connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        
        print(f"TCP Server is listening on {HOST}:{PORT}")
        logging.info(f"TCP Server started on {HOST}:{PORT}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            logging.info(f"Client connected: {addr}")
            
            while True:
                # receive data from the cleint
                data = conn.recv(1024)
                if not data:
                    break
                
                # log received msg
                message = data.decode('utf-8')
                print(f"Received: {message}")
                logging.info(f"Received: {message}")
                
                # send ack back to client
                response = f"Received: {message}".encode('utf-8')
                conn.sendall(response)
                
            print("Connection closed")
            logging.info("Connection closed")

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nServer shutdown by user")
        logging.info("Server shutdown by user")
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")