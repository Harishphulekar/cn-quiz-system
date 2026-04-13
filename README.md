### Multi-Client Online Quiz System with Real-Time Ranking

## 1.Project Description
  This project implements a secure multi-client online quiz system using TCP socket programming with SSL/TLS encryption.
  It allows multiple clients to connect to a server, participate in a quiz simultaneously, and view real-time leaderboard rankings.


## 2.Features :
            TCP-based client-server communication
            Secure communication using SSL/TLS
            Multi-client support using threading
            Time-bound quiz questions
            Real-time leaderboard updates
            Fair quiz start (synchronization)
            Performance measurement (response time)
            Error handling (invalid input, disconnects)


## 3.System Architecture

>Server
  Handles multiple clients
  Sends quiz questions
  Evaluates answers
  Maintains leaderboard

>Client
  Connects to server
  Receives questions
  Sends answers
  Displays results


## 4.Workflow
    1. Client connects to server
    2. SSL/TLS handshake establishes secure connection
    3. Clients wait until minimum players join
    4. Quiz starts simultaneously for all clients
    5. Clients answer questions
    6. Server evaluates responses
    7. Leaderboard is generated and broadcasted


## 5.Technologies Used
     Python
     TCP Socket Programming
     SSL/TLS (OpenSSL)
     Multithreading


## 6.How to Run : 
      > Generate SSL Certificate (if not already created)
            openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key
      
      > Start Server
            python server.py
      
      > Start Clients (open multiple terminals)
            python client.py



## 7.Performance Evaluation
    The system was tested with multiple clients to measure:
     Response Time
     Latency
     Throughput

Note:
   A self-signed SSL certificate is used for demonstration purposes.
   In real-world applications, certificates are issued by trusted Certificate Authorities (CA).
   The private key (`server.key`) is included only for academic purposes.


## 8.Project Structure

    cn-quiz-system/
    │
    ├── server.py
    ├── client.py
    ├── server.crt
    ├── server.key
    ├── generate_cert.py
    ├── README.md
    ├── .gitignore

## 9. Event Flow 
    
    Client → Connect → Send name
    Server → Accept → Create thread
    Server → Wait for all clients
    Server → Send questions
    Client → Send answers
    Server → Evaluate
    Server → Broadcast leaderboard

## 10.Test Results:
   
  ## Server :
  <br><img width="863" height="515" alt="Screenshot 2026-04-14 013153" src="https://github.com/user-attachments/assets/e101f200-7758-4ca3-bfd6-0b7bdbfeb088" /><br>
  ## Client :
  <br><img width="874" height="469" alt="Screenshot 2026-04-14 013202" src="https://github.com/user-attachments/assets/0d83113e-80b7-42ff-86a5-449d7dd54534" /><br>
  <img width="756" height="613" alt="Screenshot 2026-04-14 013216" src="https://github.com/user-attachments/assets/53bbc05a-e26d-4f49-9183-cb092f68e5e7" /><br>


Conclusion :
This project demonstrates how to build a **secure, scalable, and concurrent network application** using low-level socket programming concepts.

