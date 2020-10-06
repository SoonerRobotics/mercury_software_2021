###
# Making a TCP server
###

import socket

#constantly making new temporary instances of streamed data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 25565))
    s.listen()

    connection, address = s.accept()

    with connection:
        print("client connected. ip is: ", address)

        while True:
            data = connection.recv(1024)
            print("data: ", (str(data))[1:len(str(data))])

            if not data:
                break

            connection.sendall(data)
