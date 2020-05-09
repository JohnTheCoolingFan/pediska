import asyncio
import socket

host = 'localhost'
port = 9527
loop = asyncio.get_event_loop()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setblocking(False)
s.bind((host, port))
s.listen(10)



def add(one, two):
    return str(int(one) + int(two))



async def handler(conn):
    while True:
        msg = await loop.sock_recv(conn, 1024)
        print(msg)
        print()
        if b"+" in msg:
            msg = bytes("result " + add(*msg.decode().split("+")), 'utf-8')
            print(msg)

        if not msg:
            break
        await loop.sock_sendall(conn, msg)
    conn.close()

async def server():
    while True:
        conn, addr = await loop.sock_accept(s)
        loop.create_task(handler(conn))

loop.create_task(server())
loop.run_forever()
loop.close()
