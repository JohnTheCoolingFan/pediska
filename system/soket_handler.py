import socket

print(socket)
class data_socket:

    def __init__(self,port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

        self.socket.bind(("localhost", port))
        self.socket.listen(2)

        self.client,self.address = self.socket.accept()
        #self.socket.setblocking(0)
        self.client.send(bytes("Hey there!!!","utf-8"))
        print("we get")
        print("you sock")

    async def send(self, data):
        print(data)
        self.client.send(bytes(data+"\n","utf-8"))
        return True
    async def recv(self):
        data = self.client.recv(4096)
        return