import socket
import time
import statistics
import logging


logging.basicConfig(
    filename='udp_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Client config
HOST = '127.0.0.1'  #server's IP add
PORT = 65433        #port used by the UDP server
NUM_MESSAGES = 100  
TIMEOUT = 0.5       #Timeout in seconds for waiting for response

def start_client():
    """Start UDP client, send messages and measure performance."""
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        # Set timeout for receiving responses
        client_socket.settimeout(TIMEOUT)
        
        print(f"UDP Client sending to {HOST}:{PORT}")
        logging.info(f"UDP Client sending to {HOST}:{PORT}")
        
        # measure latency and packet loss
        latencies = []
        messages_sent = 0
        responses_received = 0
        total_bytes_sent = 0
        start_time_throughput = time.time()
        
        # send multiple messages
        for i in range(1, NUM_MESSAGES + 1):
            message = f"UDP Message #{i}"
            message_bytes = message.encode('utf-8')
            total_bytes_sent += len(message_bytes)
            messages_sent += 1
            
            # measure round-trip time
            start_time = time.time()
            client_socket.sendto(message_bytes, (HOST, PORT))
            
            # wait for response with timeout
            try:
                data, server = client_socket.recvfrom(1024)
                responses_received += 1
                end_time = time.time()
                
                # calculate latency for this msg
                latency = (end_time - start_time) * 1000  # Convert to milliseconds
                latencies.append(latency)
                
                print(f"Sent: {message}, Response: {data.decode('utf-8')}, RTT: {latency:.2f} ms")
                logging.info(f"Sent: {message}, Response: {data.decode('utf-8')}, RTT: {latency:.2f} ms")
                
            except socket.timeout:
                print(f"Sent: {message}, No response received (timeout)")
                logging.info(f"Sent: {message}, No response received (timeout)")
            
            # small delay btw msgs
            time.sleep(0.01)
        
        # calculate overall throughput
        end_time_throughput = time.time()
        duration = end_time_throughput - start_time_throughput
        throughput = (total_bytes_sent / duration) / 1024  # KB/s
        
        # calculate packet loss rate
        packet_loss_rate = (messages_sent - responses_received) / messages_sent * 100
        
        # calculate stats for latency (only for messages that weren't dropped)
        if latencies:
            avg_latency = statistics.mean(latencies)
            min_latency = min(latencies)
            max_latency = max(latencies)
        else:
            avg_latency = min_latency = max_latency = 0
        
        #PRINT
        print("\n--- UDP Performance Results ---")
        print(f"Messages sent: {messages_sent}")
        print(f"Responses received: {responses_received}")
        print(f"Packet loss rate: {packet_loss_rate:.2f}%")
        print(f"Average RTT: {avg_latency:.2f} ms")
        print(f"Min RTT: {min_latency:.2f} ms")
        print(f"Max RTT: {max_latency:.2f} ms")
        print(f"Throughput: {throughput:.2f} KB/s")
        
        #LOG
        logging.info("\n--- UDP Performance Results ---")
        logging.info(f"Messages sent: {messages_sent}")
        logging.info(f"Responses received: {responses_received}")
        logging.info(f"Packet loss rate: {packet_loss_rate:.2f}%")
        logging.info(f"Average RTT: {avg_latency:.2f} ms")
        logging.info(f"Min RTT: {min_latency:.2f} ms")
        logging.info(f"Max RTT: {max_latency:.2f} ms")
        logging.info(f"Throughput: {throughput:.2f} KB/s")

if __name__ == "__main__":
    try:
        start_client()
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}")