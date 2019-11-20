import socket

PC_IP = "127.0.0.1"
PC_PORT = 10010


class ClientMock:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((PC_IP, PC_PORT))
        print("connected to PC on IP {0} with port {1}".format(PC_IP, PC_PORT))

        self.i = 0
        while True:
            send_string = "hello " + str(self.i)
            send_bytes = send_string.encode('ascii')
            self.socket.send(send_bytes)
            print("sent '{}'".format(send_string))
            response_data = self.socket.recv(1024)
            response_data_string = response_data.decode('utf-8')
            print("received data: '{}'".format(response_data_string))
            self.i += 1
            input()

    def __del__(self):
        print("closing connection")
        self.socket.close()


if __name__ == "__main__":
    client = ClientMock()