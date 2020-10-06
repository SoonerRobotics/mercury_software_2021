
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 25565))

    while True:
        words = input("TYPE STUFF HERE\n")

        s.sendall(str.encode(words))
        data = s.recv(1024)

        print('Received', (str(data))[1:len(str(data))], "\n")