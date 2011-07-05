import tornado.web
from tornadio import server, get_router

from connection import ClientConnection
from handler import BroadcastHandler


urls = [ (r"/", BroadcastHandler), get_router(ClientConnection).route() ]

application = tornado.web.Application( urls )

if __name__ == "__main__":
    server.SocketServer(application)
