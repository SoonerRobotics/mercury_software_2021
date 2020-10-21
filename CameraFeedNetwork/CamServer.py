import cv2, socket, pickle, struct


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    dataBytes = b''

    # used for finding size from encoded data
    loadSize = struct.calcsize("Q")

    # normal socket stuff
    s.bind(("0.0.0.0", 25565))
    s.listen()

    # data stuff over socket
    connection, address = s.accept()

    print("socket ready")

    with connection:
        print("client connected. ip is: ", address)

        while True:

            # scraping the data size from encoded socket connection
            while (len(dataBytes) < loadSize):
                dataBytes += connection.recv(4096)

            # decoding the data about data size
            dataSize = struct.unpack("Q", dataBytes[:loadSize])[0]

            # disregard dataSize, now ready for encoded data
            dataBytes = dataBytes[loadSize:]

            # keeps on receiving data until it hits the "pre-written" data size
            while (len(dataBytes) < dataSize):
                dataBytes += connection.recv(4096)

            # separating encoded data itself from any extra stuff sent over
            frameData = dataBytes[:dataSize]
            dataBytes = dataBytes[dataSize:]

            # extracting frame from compression/encoding
            frame = pickle.loads(frameData)

            #height, width, _ = frame.shape
            #cv2.putText(frame, "yeet", (.25 * height, .25 * width), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)

            cv2.imshow("videoFeed", frame)
            cv2.waitKey(1)

    #return frame
