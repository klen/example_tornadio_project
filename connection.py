from tornadio import SocketConnection
import logging


class ClientConnection(SocketConnection):

    clients = set()

    def __init__(self, *args, **kwargs):
        self.id = None
        super(ClientConnection, self).__init__(*args, **kwargs)

    def on_open(self, *args, **kwargs):
        logging.warning('client connected')
        self.clients.add(self)

    def on_message(self, message):
        logging.warning(message)
        if not self.id:
            self.id = message.get('id', None)
        self.send('Hello client %s' % self.id)

    def on_close(self):
        logging.warning('client disconnected')
        self.clients.remove(self)

