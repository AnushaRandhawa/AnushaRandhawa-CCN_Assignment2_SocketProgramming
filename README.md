# Assignment 2 Socket Programming

## Overview
This repository contains a comparison of TCP and UDP protocols through socket programming in Python. The implementation measures and analyzes the differences in latency, packet loss, and throughput between these two fundamental transport protocols.

## Files
- `tcp_server.py`: TCP server implementation
- `tcp_client.py`: TCP client that sends 100 messages and measures round-trip time
- `udp_server.py`: UDP server with simulated packet loss
- `udp_client.py`: UDP client that handles potential packet loss
- `tcp_log.txt`: Log file for TCP operations
- `udp_log.txt`: Log file for UDP operations

## How to Run the Programs

### 1. TCP Test
Open two terminal windows:

**Terminal 1 (Server):**
```
python tcp_server.py
```

**Terminal 2 (Client):**
```
python tcp_client.py
```

### 2. UDP Test
Open two terminal windows:

**Terminal 1 (Server):**
```
python udp_server.py
```

**Terminal 2 (Client):**
```
python udp_client.py
```

## Expected Outputs

### TCP Client Output
The TCP client will show:
- Each message sent with its response and round-trip time (RTT)
- Summary statistics including:
  - Messages sent
  - Average RTT
  - Minimum RTT
  - Maximum RTT
  - Throughput in KB/s

### UDP Client Output
The UDP client will show:
- Each message sent, with either a response and RTT or a timeout notification
- Summary statistics including:
  - Messages sent and responses received
  - Packet loss rate
  - Average RTT (for successful messages)
  - Minimum RTT
  - Maximum RTT
  - Throughput in KB/s

## Observations about TCP vs UDP Behavior

## Comparison and Analysis

### 1. Latency Comparison
- **TCP**: Shows higher average latency due to its connection establishment (3-way handshake) and acknowledgment mechanism.
- **UDP**: Typically demonstrates lower latency as it doesn't require connection establishment or wait for ACKs.

### 2. Reliability and Packet Loss
- **TCP**: Ensures reliable delivery with no packet loss through its acknowledgment and retransmission process. All 100 messages are guaranteed to be received.
- **UDP**: In my implementation, approximately 20% of packets are dropped by the server to simulate real-world conditions. The client detects these as timeouts.

### 3. Throughput Analysis
- **TCP**: Despite higher reliability, TCP often shows lower throughput due to its overhead from acknowledgments, flow control, and congestion control mechanisms.
- **UDP**: Has higher throughput as it doesn't wait for acknowledgments or manage connections, but this comes at the cost of reliability.

### 4. Use Cases
- **TCP is better for**:
  - Web browsing (HTTP/HTTPS)
  - File transfers (FTP)
  - Email (SMTP)
  - Remote terminal access (SSH)
  - Any application requiring guaranteed and ordered delivery

- **UDP is better for**:
  - Voice over IP (VoIP)
  - Video streaming
  - Online gaming
  - DNS lookups
  - Applications where low latency is more important than perfect reliability

## Implementation Approach

This implementation was accomplished by:

1. Understanding socket programming in Python using the built-in `socket` module.
2. Implementing connection-oriented TCP servers and clients with proper connection handling.
3. Creating connectionless UDP servers and clients with timeout mechanisms.
4. Adding performance measurement tools to track latency and throughput.
5. Simulating real-world conditions through artificial packet dropping in UDP.

### References:
- Python socket programming documentation: https://docs.python.org/3/library/socket.html
- Cisco Packet Tracer course for concepts
- Instructor's Lecture Slides for concepts
- Real Python tutorial on socket programming: https://realpython.com/python-sockets/
- Stack Overflow discussions on measuring network performance
