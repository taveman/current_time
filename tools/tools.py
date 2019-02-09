import logging
import os
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


def check_dir_existence(root_dir, dirs):
    """
    Checks if dirs are exist
    :param root_dir: root dir to be used in the check
    :type root_dir: str
    :param dirs: list of dir names
    :type dirs: list
    :return: True or False
    :rtype: bool
    """
    logger = logging.getLogger('time_speaker')
    for d in dirs:
        if not os.path.exists(os.path.join(root_dir, d)):
            logger.error('check_dir_existence: There is no such a dir as {}'.format(os.path.join(root_dir, d)))
            return False
    return True
