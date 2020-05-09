import socket

print(socket)
class data_socket:

    def __init__(self,loop):
        self.conn = None
        self.loop = loop
        self.last_msg = None

    async def handler(self):
        while True:
            msg = await self.loop.sock_recv(self.conn, 1024)

            if not msg:
                break
            else:
                print("message in soket",msg)
                #TODO Вот тут будет вызов оброботчика команд.... Да костыль но Работате же!!!!
                pass
        print("end conn")
        self.conn.close()
        self.conn = None

    async def sokct(self):
        return self.conn

    async def send(self,msg):
        print(self.conn)
        if self.conn:
            await self.loop.sock_sendall(self.conn, bytes(msg,'utf-8'))
        else:
            return False
    async def server(self,s):
        print("startup")
        while True:
            self.conn, addr = await self.loop.sock_accept(s)
            print(self.loop.create_task(self.handler()))