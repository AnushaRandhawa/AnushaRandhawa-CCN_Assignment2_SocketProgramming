import socket
import time
import statistics
import logging


logging.basicConfig(
    filename='tcp_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Client config
HOST = '127.0.0.1'  # The server's IP add
PORT = 65432        # port used by the server
NUM_MESSAGES = 100  # num of msgs to send

def start_client():
    """Start TCP client, send messages and measure performance."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        print(f"Connecting to TCP server at {HOST}:{PORT}")
        client_socket.connect((HOST, PORT))
        print("Connected to server")
        logging.info(f"Connected to TCP server at {HOST}:{PORT}")
        
        # for measure latency
        latencies = []
        total_bytes_sent = 0
        start_time_throughput = time.time()
        
        # Send multiple messages
        for i in range(1, NUM_MESSAGES + 1):
            message = f"TCP Message #{i}"
            message_bytes = message.encode('utf-8')
            total_bytes_sent += len(message_bytes)
            
            # measure round-trip time
            start_time = time.time()
            client_socket.sendall(message_bytes)
            
            # wait for response back hear
            data = client_socket.recv(1024)
            end_time = time.time()
            
            # calculating latency for this message
            latency = (end_time - start_time) * 1000  # Convert to milliseconds
            latencies.append(latency)
            
            print(f"Sent: {message}, Response: {data.decode('utf-8')}, RTT: {latency:.2f} ms")
            logging.info(f"Sent: {message}, Response: {data.decode('utf-8')}, RTT: {latency:.2f} ms")
            
            # small delay between messages
            time.sleep(0.01)
        
        # calculating the overall throughput
        end_time_throughput = time.time()
        duration = end_time_throughput - start_time_throughput
        throughput = (total_bytes_sent / duration) / 1024  # KB/s
        
        # calculate stats
        avg_latency = statistics.mean(latencies)
        min_latency = min(latencies)
        max_latency = max(latencies)
        
        # PRINT
        print("\n--- TCP Performance Results ---")
        print(f"Messages sent: {NUM_MESSAGES}")
        print(f"Average RTT: {avg_latency:.2f} ms")
        print(f"Min RTT: {min_latency:.2f} ms")
        print(f"Max RTT: {max_latency:.2f} ms")
        print(f"Throughput: {throughput:.2f} KB/s")
        
        #LOG as required for assigment
        logging.info("\n--- TCP Performance Results ---")
        logging.info(f"Messages sent: {NUM_MESSAGES}")
        logging.info(f"Average RTT: {avg_latency:.2f} ms")
        logging.info(f"Min RTT: {min_latency:.2f} ms")
        logging.info(f"Max RTT: {max_latency:.2f} ms")
        logging.info(f"Throughput: {throughput:.2f} KB/s")

if __name__ == "__main__":
    try:
        start_client()
    except ConnectionRefusedError:
        print("Connection failed. Make sure the server is running.")
        logging.error("Connection failed. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")
