from logging import Logger

import sounddevice as sd
import soundfile as sf
import numpy as np

from core.interfaces import SpeakerInterface


class Speaker(SpeakerInterface):
    """
    Facade class responsible for pronunciation
    """

    def __init__(self, logger):
        """
        Initialization
        :param logger: logger to be used
        :type logger: Logger
        """
        self.rate = 44100
        self.logger = logger

    def say(self, target_files=None):
        """
        Pronounces all the audio files passed to this method
        :param target_files: files to be played
        :type target_files: Iterable
        """
        if not target_files:
            self.logger.error('{}: say method got an empty list of files'.format(self.__class__.__name__))
        self.logger.debug('{}: got the following files to pronounce:\n{}'.format(
            self.__class__.__name__,
            target_files
        ))
        data_to_play = self._prepare_data(target_files)
        sd.play(data_to_play, self.rate)
        status = sd.wait()

    @classmethod
    def _prepare_data(cls, sound_files):
        """
        Produces concat numpy array to be played
        :param sound_files: list of files to be read and concatenate
        :rtype: np.ndarray
        """
        all_data = []
        for f in sound_files:
            data, _ = sf.read(f, dtype='float64')
            all_data.append(data)

        return np.concatenate(all_data)


if __name__ == '__main__':
    import logging
    files = [
        '../sounds/time/FAC_1A.wav',
        '../sounds/time/FAC_2A.wav',
        '../sounds/time/FAC_3A.wav'
    ]
    a = Speaker(logger=logging.getLogger())
    a.say(files)

