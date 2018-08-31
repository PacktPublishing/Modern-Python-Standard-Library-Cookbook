import socket
import threading
import socketserver


class EchoServer:
    def __init__(self, host='0.0.0.0', port=9800):
        self._host = host
        self._port = port
        self._server = ThreadedTCPServer((host, port), EchoRequestHandler)
        self._thread = threading.Thread(target=self._server.serve_forever)
        self._thread.daemon = True

    def start(self):
        if self._thread.is_alive():
            # Already serving
            return
        
        print('Serving on %s:%s' % (self._host, self._port))
        self._thread.start()

    def stop(self):
        self._server.shutdown()
        self._server.server_close()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


class EchoRequestHandler(socketserver.BaseRequestHandler):
    MAX_MESSAGE_SIZE = 2**16  # 65k
    MESSAGE_HEADER_LEN = len(str(MAX_MESSAGE_SIZE))

    @classmethod
    def recv_message(cls, socket):
        data_size = int(socket.recv(cls.MESSAGE_HEADER_LEN))
        data = socket.recv(data_size)
        return data

    @classmethod
    def prepare_message(cls, message):
        if len(message) > cls.MAX_MESSAGE_SIZE:
            raise ValueError('Message too big')
        
        message_size = str(len(message)).encode('ascii')
        message_size = message_size.zfill(cls.MESSAGE_HEADER_LEN)
        return message_size + message

    def handle(self):
        message = self.recv_message(self.request)
        self.request.sendall(self.prepare_message(b'ECHO: %s' % message))




def send_message_to_server(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        message = EchoRequestHandler.prepare_message(message)
        sock.sendall(message)
        response = EchoRequestHandler.recv_message(sock)
        print("ANSWER: {}".format(response))
    finally:
        sock.close()


server = EchoServer()
server.start()

send_message_to_server('localhost', server._port, b"Hello World 1")
send_message_to_server('localhost', server._port, b"Hello World 2")
send_message_to_server('localhost', server._port, b"Hello World 3")

server.stop()