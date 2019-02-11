import os
import falcon
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
import logging
from logging import Logger

from tools.tools import init_logger
from web.routes import add_routes

root_dir = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
parent_dir = os.path.abspath(os.path.dirname(root_dir))

root_logger = logging.getLogger()
root_logger.setLevel(logging.ERROR)
root_handler = logging.FileHandler(filename=os.path.join(parent_dir, 'logs/errors.log'))
root_handler.setLevel(logging.ERROR)
root_logger.addHandler(root_handler)


class ErrorWsgiLogger:

    def __init__(self, log):
        """
        Logger to be used for error messaging redirection
        :param log: logger
        :rtype log: Logger
        """
        self.logger = log

    def write(self, message):
        self.logger.error(message)

    def flush(self):
        pass


class WSGIRequestHandlerWithLogger(WSGIRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_stderr(self):
        return ErrorWsgiLogger(log=root_logger)


init_logger(
    logger_name='web_interface',
    info_logger_path=os.path.join(parent_dir, 'logs/web_info.log'),
    debug_logger_path=os.path.join(parent_dir, 'logs/web_debug.log'),
    debug=True
)

logger = logging.getLogger('web_interface')
logger.info('Starting web API')
application = falcon.API()

application = add_routes(application)

httpd = simple_server.make_server('127.0.0.1', 8000, application, handler_class=WSGIRequestHandlerWithLogger)
httpd.serve_forever()

