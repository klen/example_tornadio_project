from tornadio import SocketConnection
import logging


class ClientConnection(SocketConnection):

    clients = set()

    def on_open(self, *args, **kwargs):
        logging.warning('client connected')
        self.clients.add(self)

    def on_close(self):
        logging.warning('client disconnected')
        self.clients.remove(self)

