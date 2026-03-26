import socket
import ssl

HOST = '127.0.0.1'
PORT = 5000

context = ssl._create_unverified_context()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = context.wrap_socket(sock, server_hostname=HOST)

conn.connect((HOST, PORT))

name = input("Enter your name: ")
conn.send(name.encode())

while True:
    try:
        data = conn.recv(1024).decode()

        if not data:
            break

        print(data)

        if "QUESTION" in data:
            answer = input("Your answer: ").strip().upper()
            conn.send(answer.encode())

    except:
        print("Connection closed by server")
        break

conn.close()