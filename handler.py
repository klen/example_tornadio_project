import tornado.web


class BroadcastHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('console.html')
