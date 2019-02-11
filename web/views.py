import falcon
from falcon import Request, Response
from core.main import time_speaker
import logging


class CurrentTime:

    def on_get(self, request, response):
        """
        :param request: Falcon request object
        :type request: Request
        :param response: Falcon response object
        :type response: Response
        """
        logger = logging.getLogger('web_interface')
        logger.debug('{}: got GET request'.format(self.__class__.__name__))

        time_speaker.what_is_the_time()
        response.status = falcon.HTTP_200
