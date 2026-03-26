import socket
import ssl
import threading
import time

HOST = '127.0.0.1'
PORT = 5000

clients = []
scores = {}
lock = threading.Lock()
start_event = threading.Event()

MIN_CLIENTS = 3  # required clients to start quiz

quiz_questions = [
    ("Which protocol is used for web? \n A. FTP \n B. HTTP \n C. TCP", "B"),
    ("How many layers are in OSI model? \n A. 5 \n B. 9 \n C. 7", "C"),
    ("What does IP stand for? \n A. Internet Process \n B. Internet Protocol \n C. Internal Program", "B"),
    ("Which protocol is used to send emails? \n A. SMTP \n B. HTTP \n C. FTP", "A"),
    ("Which protocol is connection-oriented? \n A. TCP \n B. UDP \n C. ICMP", "A"),
]

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            clients.remove(client)

def handle_client(conn, addr):
    try:
        name = conn.recv(1024).decode()
        with lock:
            scores[name] = 0

        print(f"{name} connected from {addr}")
        broadcast(f"{name} joined the quiz!")

        # Wait until enough clients join
        conn.send("Waiting for other players...\n".encode())
        start_event.wait()

        conn.send("\nQuiz Starting Now!\n".encode())

        for question, answer in quiz_questions:
            try:
                conn.send(f"\nQUESTION:\n{question}\n".encode())

                start_time = time.time()
                client_answer = conn.recv(1024).decode().strip().upper()
                end_time = time.time()

                response_time = end_time - start_time
                print(f"{name} answered in {response_time:.2f} sec")

                if client_answer not in ["A", "B", "C"]:
                    conn.send("Invalid option! Use A/B/C\n".encode())
                    continue

                if client_answer == answer:
                    with lock:
                        scores[name] += 1
                    conn.send("Correct!\n".encode())
                else:
                    conn.send(f"Wrong! Correct answer: {answer}\n".encode())

            except:
                print(f"{name} disconnected during quiz")
                break

        # Send leaderboard ONCE after quiz
        send_leaderboard()

        conn.close()

    except:
        print("Error handling client")


def send_leaderboard():
    leaderboard = "\n--- Leaderboard ---\n"

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    rank = 1
    for player, score in sorted_scores:
        leaderboard += f"{rank}. {player}: {score}\n"
        rank += 1

    broadcast(leaderboard)


def start_server():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print("Quiz Server Started... Waiting for clients...")

    while True:
        client_socket, addr = server_socket.accept()
        conn = context.wrap_socket(client_socket, server_side=True)

        clients.append(conn)

        # Start quiz when enough clients join
        if len(clients) >= MIN_CLIENTS:
            print("Minimum clients reached. Starting quiz...")
            start_event.set()

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start_server()