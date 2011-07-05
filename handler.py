import tornado.web
from connection import ClientConnection


class BroadcastHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('console.html')

    def post(self):
        message = self.get_argument('message')
        key = self.get_argument('id', None)
        for client in ClientConnection.clients:
            if key and not key == client.id:
                continue
            client.send(message)
        self.write('message send.')
