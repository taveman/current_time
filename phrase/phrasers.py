import os
from logging import Logger
from collections import namedtuple
from core.interfaces import PhraseMakerInterface
from tools.tools import check_dir_existence
from phrase.structures.time.russian.structure import phrase_structure

samples_time_names = namedtuple('SoundSamplesTime', 'hours minutes seconds')
sd = samples_time_names(hours='hours', minutes='minutes', seconds='seconds')


class RusTimePhraseMaker(PhraseMakerInterface):
    """
    Prepares phrases to be pronounced in Russian
    """
    def __init__(self, root_sound_samples_dir, logger, time_dirs=sd):
        """
        Initialization
        :param root_sound_samples_dir: root dir for time samples
        :type root_sound_samples_dir: str
        :param logger: logger
        :type logger: Logger
        :param time_dirs: named tuple with names of sub dirs
        :type time_dirs: namedtuple
        """
        self.logger = logger
        self.lang_dir_name = 'rus'
        self.root_sound_samples_dir = os.path.join(root_sound_samples_dir, self.lang_dir_name)
        self.time_dirs = time_dirs

        if not check_dir_existence(self.root_sound_samples_dir, list(self.time_dirs)):
            logger.error('{}: error checking sound dirs: {}'.format(
                self.__class__.__name__,
                list(self.time_dirs)))
            raise IsADirectoryError()

    def build_the_phrase(self, cur_date):
        """
        Builds the phrase
        :param cur_date: current datetime object
        :type cur_date: datetime
        :return: list of prepared sequence of files
        """
        files_to_return = []

        self.logger.debug('{}: got time: {}'.format(self.__class__.__name__, cur_date))

        hours_files = self._get_phrase_files(cur_date.hour, self.time_dirs.hours)
        for f in hours_files:
            files_to_return.append(os.path.join(self.root_sound_samples_dir, self.time_dirs.hours, f))

        minute_files = self._get_phrase_files(cur_date.minute, self.time_dirs.minutes)
        for f in minute_files:
            files_to_return.append(os.path.join(self.root_sound_samples_dir, self.time_dirs.minutes, f))

        seconds_files = self._get_phrase_files(cur_date.second, self.time_dirs.seconds)
        for f in seconds_files:
            files_to_return.append(os.path.join(self.root_sound_samples_dir, self.time_dirs.seconds, f))

        return files_to_return

    def _get_phrase_files(self, value, postfix):
        """
        Find two suitable sound files for current time
        :param value: value representing amount of time
        :type value: int
        :param postfix: string to be appended to the file name
        :type postfix: str
        :return: list of file names
        :rtype: list
        """
        files_to_return = []
        name_type = self._get_the_right_type(value)

        if value in tuple(range(0, 21)) + tuple(range(30, 61, 10)):
            files_to_return.append('{}_{}.wav'.format(value, postfix))
        else:
            second_sub_file = value % 10
            first_sub_file = value - second_sub_file
            files_to_return.append('{}_{}.wav'.format(first_sub_file, postfix))
            files_to_return.append('{}_{}.wav'.format(second_sub_file, postfix))
        files_to_return.append('{}.wav'.format(name_type))

        return files_to_return

    @staticmethod
    def _get_the_right_type(value):
        """
        Returns the write phrase type
        :param value:
        :return:
        """
        for name, value_set in phrase_structure.items():
            if value in value_set:
                return name


class EngTimePhraseMaker(PhraseMakerInterface):
    """
    Prepares phrases to be pronounced in English
    Not implemented
    """
    def __init__(self):
        pass

    def build_the_phrase(self, files_map):
        """
        Builds the phrase
        :param files_map:
        :return: list of prepared sequence
        """