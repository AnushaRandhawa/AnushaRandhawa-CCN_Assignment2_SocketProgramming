import socket
import time
import random
import logging


logging.basicConfig(
    filename='udp_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Server config
HOST = '127.0.0.1'  # localhost
PORT = 65433        # different port from TCP
PACKET_LOSS_RATE = 0.2  # 20% packet loss rate

def start_server():
    """Start the UDP server and handle incoming packets."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, PORT))
        
        print(f"UDP Server is listening on {HOST}:{PORT}")
        print(f"Simulating {PACKET_LOSS_RATE*100}% packet loss rate")
        logging.info(f"UDP Server started on {HOST}:{PORT}")
        logging.info(f"Simulating {PACKET_LOSS_RATE*100}% packet loss rate")
        
        dropped_packets = 0
        received_packets = 0
        
        while True:
            try:
                # Receive data and client address
                data, addr = server_socket.recvfrom(1024)
                received_packets += 1
                
                # run simulation of packet loss by randomly dropping packets
                if random.random() < PACKET_LOSS_RATE:
                    dropped_packets += 1
                    print(f"Dropping packet from {addr}: {data.decode('utf-8')}")
                    logging.info(f"Dropping packet from {addr}: {data.decode('utf-8')}")
                    continue
                
                # process received message
                message = data.decode('utf-8')
                print(f"Received from {addr}: {message}")
                logging.info(f"Received from {addr}: {message}")
                
                # send ack back to client
                response = f"Received: {message}".encode('utf-8')
                server_socket.sendto(response, addr)
                
                # Log stats occasionally
                if received_packets % 10 == 0:
                    print(f"Stats - Received: {received_packets}, Dropped: {dropped_packets}")
                    logging.info(f"Stats - Received: {received_packets}, Dropped: {dropped_packets}")
                    
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")
                logging.error(f"Error: {e}")
        
        print("Server shutdown")
        logging.info("Server shutdown")

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nServer shutdown by user")
        logging.info("Server shutdown by user")
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")