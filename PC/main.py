import socket


class Main:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('0.0.0.0', 10010))
        self.socket.listen(5)
        print("listening on port 10010")
        connection, address = self.socket.accept()
        with connection:
            while True:
                data = connection.recv(1024)
                data_string = data.decode('ascii')
                print("Got data {}".format(data_string))
                data_as_number = int(data_string)
                wait_delay = 200 + data_as_number * 1000
                connection.send(str(wait_delay).encode('ascii'))
                print("Sent {} back".format(wait_delay))

    def __del__(self):
        print("closing connection")
        self.socket.close()


if __name__ == "__main__":
    main = Main()
