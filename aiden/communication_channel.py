```python
import socket

class CommunicationChannel:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def establish_connection(self, host, port):
        try:
            self.socket.connect((host, port))
            print("Connection established with the server.")
        except socket.error as e:
            print(f"Something went wrong: {e}")

    def close_connection(self):
        self.socket.close()
        print("Connection closed with the server.")

    def send_message(self, message):
        try:
            self.socket.sendall(message.encode('utf-8'))
            print("Message sent to the server.")
        except socket.error as e:
            print(f"Something went wrong: {e}")

    def receive_message(self):
        try:
            data = self.socket.recv(1024)
            print(f"Message received from the server: {data.decode('utf-8')}")
        except socket.error as e:
            print(f"Something went wrong: {e}")
```