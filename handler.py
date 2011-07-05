import tornado.web
from connection import ClientConnection


class BroadcastHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('console.html')

    def post(self):
        message = self.get_argument('message')
        for client in ClientConnection.clients:
            client.send(message)
        self.write('message send.')
