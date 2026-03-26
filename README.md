Multi-Client Online Quiz System with Real-Time Ranking

Project Description

This project implements a secure multi-client online quiz system using TCP socket programming with SSL/TLS encryption.
It allows multiple clients to connect to a server, participate in a quiz simultaneously, and view real-time leaderboard rankings.


Features :
TCP-based client-server communication
Secure communication using SSL/TLS
Multi-client support using threading
Time-bound quiz questions
Real-time leaderboard updates
Fair quiz start (synchronization)
Performance measurement (response time)
Error handling (invalid input, disconnects)


System Architecture

Server
  Handles multiple clients
  Sends quiz questions
  Evaluates answers
  Maintains leaderboard

Client
  Connects to server
  Receives questions
  Sends answers
  Displays results


Workflow
1. Client connects to server
2. SSL/TLS handshake establishes secure connection
3. Clients wait until minimum players join
4. Quiz starts simultaneously for all clients
5. Clients answer questions
6. Server evaluates responses
7. Leaderboard is generated and broadcasted


Technologies Used
 Python
 TCP Socket Programming
 SSL/TLS (OpenSSL)
 Multithreading


How to Run : Generate SSL Certificate (if not already created)

    openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key


Start Server
python server.py


Start Clients (open multiple terminals)
python client.py



Performance Evaluation

The system was tested with multiple clients to measure:

 Response Time
 Latency
 Throughput

Example:

| Clients | Avg Response Time |
| ------- | ----------------- |
| 2       | 0.2 sec           |
| 5       | 0.5 sec           |
| 10      | 1.2 sec           |


Note
   A self-signed SSL certificate is used for demonstration purposes.
   In real-world applications, certificates are issued by trusted Certificate Authorities (CA).
   The private key (`server.key`) is included only for academic purposes.


Project Structure

cn-quiz-system/
│
├── server.py
├── client.py
├── server.crt
├── server.key
├── generate_cert.py
├── README.md
├── .gitignore



Concepts Demonstrated

* Client-Server Architecture
* TCP Socket Programming
* SSL/TLS Security
* Multithreading (Concurrency)
* Network Performance Evaluation



Conclusion :
This project demonstrates how to build a **secure, scalable, and concurrent network application** using low-level socket programming concepts.

