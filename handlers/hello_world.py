import tornado.ioloop
import tornado.web
from mongotest.handlers.powhandler import PowHandler
from mongotest.lib.application import app, route

@app.make_routes()
class HelloHandler(PowHandler):
    @route(r'/hello', dispatch=["get"])
    def hello(self):
        self.write("Hello world!")