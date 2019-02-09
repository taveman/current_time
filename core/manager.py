from datetime import datetime
import os
from logging import Logger
from collections import Iterable, namedtuple

from core.interfaces import SpeakerInterface, AudioManipulationInterface
from tools.tools import check_dir_existence

samples_dir_names = namedtuple('SoundSamples', 'hours minutes seconds')
sd = samples_dir_names(hours='hours', minutes='minutes', seconds='seconds')

FILE_PATTERN = '{value}_{name}.wav'


class TimeManager:

    def __init__(self, speaker, root_sound_sample_dir, logger=None):
        """
        Initialization
        :param speaker: speaker to be used to speak
        :type speaker: SpeakerInterface
        :param root_sound_sample_dir: audio manipulator to be used
        :type root_sound_sample_dir: str
        :param logger: logger to be used
        :type logger: Logger
        """
        self.speaker = speaker
        self.root_sound_samples_dir = root_sound_sample_dir
        self.sample_sub_dirs = sd
        self.logger = logger

        if not check_dir_existence(self.root_sound_samples_dir, list(self.sample_sub_dirs)):
            logger.error('{}: error checking sound dirs: {}'.format(
                self.__class__.__name__,
                list(self.sample_sub_dirs)))
            raise IsADirectoryError()

        self.hours_map = self._generate_samples(self.sample_sub_dirs.hours, range(1, 25))
        self.minutes_map = self._generate_samples(self.sample_sub_dirs.minutes, range(1, 61))
        self.seconds_map = self._generate_samples(self.sample_sub_dirs.seconds, range(1, 61))

    def what_is_the_time(self):
        """
        Get current time and feed the result to the speaker
        :return:
        """
        cur_time = datetime.now()
        file_sequence = self._generate_sound_sequence(cur_time)
        self.speaker.say(file_sequence)

    def _generate_sound_sequence(self, cur_time):
        """
        Generate file sequence regarding the current time passed
        :param cur_time: current time to be used
        :return: right ordered sequence of files to be played
        """
        hour_file = self.hours_map[cur_time.hour]
        minute_file = self.hours_map[cur_time.minute]
        second_file = self.hours_map[cur_time.second]

        self.logger.debug('{}:{}\ntime: {}\nhour_file: {}\nminute_file: {}\nsecond_file_{}\n'.format(
            self.__class__.__name__,
            '_generate_sound_sequence',
            cur_time,
            hour_file,
            minute_file,
            second_file
        ))
        return [hour_file, minute_file, second_file]

    def _generate_samples(self, name, time_range):
        """
        Generates maps of sample
        :param name: name to be used
        :return: dict of all the samples for tha name passed
        :param time_range: number of values
        :type time_range: Iterable
        :rtype: dict
        """
        to_return = {}
        sound_dir = os.path.join(self.root_sound_samples_dir, name)

        for t in time_range:
            to_return[t] = os.path.join(sound_dir, FILE_PATTERN.format(value=t, name=name))
        return to_return
