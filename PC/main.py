import socket


class Main:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('127.0.0.1', 10010))
        self.socket.listen(5)
        print("listening on port 10010")
        connection, address = self.socket.accept()
        with connection:
            while True:
                data = connection.recv(1024)
                data_string = data.decode('utf-8')
                print("Got data {}".format(data_string))
                connection.send("hello there".encode('utf-8'))
                print("Sent data back")

    def __del__(self):
        print("closing connection")
        self.socket.close()


if __name__ == "__main__":
    main = Main()
