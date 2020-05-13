import socket
#TODO https://ru.stackoverflow.com/questions/684398/Прием-сообщений-в-socket-python
class data_socket:

    def __init__(self,loop):
        self.conn = None # Подключение который мы инициализировали
        self.socket = None  # сам сокет
        self.loop = loop # loop в котором работает бот
        self.work = None # работает ли "сервер"

    #Устоновка сокета
    def set_socket(self,address:str,port:int):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setblocking(False)
        self.socket.bind((address, port))
        self.socket.listen(10)
        return True

    #оброботчик сокета
    async def socket_handler(self):
        while True:
            msg = await self.loop.sock_recv(self.conn, 1024)
            if not msg:
                break
            else:
                print("message in soket",msg)
                #TODO Вот тут будет вызов оброботчика команд
                #TODO реализация через task!
        self.conn.close()
        self.conn = None

    #получить текущее подключение
    #Возращает none если ничего нет
    async def get_current_soket(self): #для реализации костылей
        return self.conn

    #Отправляет сообщение на сокет в случае успеха вернет True иначе False
    async def send(self,msg:str):
        if self.conn:
            try:
                await self.loop.sock_sendall(self.conn, bytes(msg if msg[-1] == '\n' else msg+'\n','utf-8'))
            except:
                return False
            else:
                return True
        else:
            return False

    #запуск обработчика сокета
    async def start_socket_handler(self):
        while True:
            self.conn, addr = await self.loop.sock_accept(self.socket)
            self.loop.create_task(self.socket_handler())