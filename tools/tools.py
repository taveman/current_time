import logging
from logging.handlers import TimedRotatingFileHandler


def init_logger(logger_name, info_logger_path, debug_logger_path, debug=False):
    """
    Logger initializer
    :param logger_name: logger name to be used
    :type logger_name: str
    :param info_logger_path: path to the logger with logging level INFO
    :type info_logger_path: str
    :param debug_logger_path: path to the logger with logging level DEBUG
    :type debug_logger_path: str
    :param debug: does logger need to record debug information or doesn't
    :type debug: bool
    """
    logger = logging.getLogger(logger_name)

    formatter_info = logging.Formatter('%(levelname)s: %(asctime)s: %(name)s: %(message)s')
    file_h_info = TimedRotatingFileHandler(info_logger_path, when='D', interval=1, backupCount=50)
    file_h_info.setLevel(logging.INFO)
    file_h_info.setFormatter(formatter_info)

    logger.addHandler(file_h_info)

    if debug:
        formatter_debug = logging.Formatter('%(levelname)s: %(asctime)s: %(name)s: %(message)s')
        file_h_debug = TimedRotatingFileHandler(debug_logger_path, when='D', interval=1, backupCount=50)
        file_h_debug.setLevel(logging.DEBUG)
        file_h_debug.setFormatter(formatter_debug)
        logger.addHandler(file_h_debug)

    logger.setLevel(logging.DEBUG) if debug else logger.setLevel(logging.INFO)
