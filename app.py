import tornado.web
from tornadio import server

from handler import BroadcastHandler


urls = [ (r"/", BroadcastHandler) ]

application = tornado.web.Application( urls )

if __name__ == "__main__":
    server.SocketServer(application)
