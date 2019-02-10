from datetime import datetime
from logging import Logger

from core.interfaces import SpeakerInterface, PhraseMakerInterface


class TimeManager:

    def __init__(self, speaker, phrase_generator, logger=None):
        """
        Initialization
        :param speaker: speaker to be used to speak
        :type speaker: SpeakerInterface
        :param phrase_generator: phrase generator to be used
        :type phrase_generator: PhraseMakerInterface
        :param logger: logger to be used
        :type logger: Logger
        """
        self.speaker = speaker
        self.logger = logger
        self.phrase_generator = phrase_generator

    def what_is_the_time(self):
        """
        Get current time and feed the result to the speaker
        :return:
        """
        cur_time = datetime.now()
        file_sequence = self.phrase_generator.build_the_phrase(cur_time)
        self.speaker.say(file_sequence)
