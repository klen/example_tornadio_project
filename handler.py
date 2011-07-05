import tornado.web


class BroadcastHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('Hello from tornadio!')
