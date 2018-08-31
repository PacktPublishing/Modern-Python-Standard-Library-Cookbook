import asyncio

class EchoServer:
    MAX_MESSAGE_SIZE = 2**16  # 65k
    MESSAGE_HEADER_LEN = len(str(MAX_MESSAGE_SIZE))

    def __init__(self, host='0.0.0.0', port=9800):
        self._host = host
        self._port = port
        self._server = None
    
    def serve(self, loop):
        coro = asyncio.start_server(self.handle, self._host, self._port,
                                    loop=loop)
        self._server = loop.run_until_complete(coro)
        print('Serving on %s:%s' % (self._host, self._port))
        loop.run_until_complete(self._server.wait_closed())
        print('Done')

    @property
    def started(self):
        return self._server is not None and self._server.sockets

    def stop(self):
        print('Stopping...')
        self._server.close()

    async def handle(self, reader, writer):
        data = await self.recv_message(reader)
        await self.send_message(writer, b'ECHO: %s' % data)
        # Signal we finished handling this request
        # or the server will hang.
        writer.close()

    @classmethod
    async def recv_message(cls, socket):
        data_size = int(await socket.read(cls.MESSAGE_HEADER_LEN))
        data = await socket.read(data_size)
        return data

    @classmethod
    async def send_message(cls, socket, message):
        if len(message) > cls.MAX_MESSAGE_SIZE:
            raise ValueError('Message too big')
        
        message_size = str(len(message)).encode('ascii')
        message_size = message_size.zfill(cls.MESSAGE_HEADER_LEN)
        data = message_size + message
        
        socket.write(data)
        await socket.drain()


import socket

def send_message_to_server(ip, port, message):
    def _recv_message(socket):
        data_size = int(socket.recv(EchoServer.MESSAGE_HEADER_LEN))
        data = socket.recv(data_size)
        return data

    def _prepare_message(message):
        if len(message) > EchoServer.MAX_MESSAGE_SIZE:
            raise ValueError('Message too big')
        
        message_size = str(len(message)).encode('ascii')
        message_size = message_size.zfill(EchoServer.MESSAGE_HEADER_LEN)
        return message_size + message

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(_prepare_message(message))
        response = _recv_message(sock)
        print("ANSWER: {}".format(response))
    finally:
        sock.close()


server = EchoServer()
def serve_for_3_seconds():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.call_later(3, server.stop)
    server.serve(loop)
    loop.close()


import threading
server_thread = threading.Thread(target=serve_for_3_seconds)
server_thread.start()

while not server.started:
    pass

send_message_to_server('localhost', server._port, b"Hello World 1")
send_message_to_server('localhost', server._port, b"Hello World 2")
send_message_to_server('localhost', server._port, b"Hello World 3")

server_thread.join()