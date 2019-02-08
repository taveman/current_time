import sounddevice as sd
import soundfile as sf


class Speaker:
    """
    Facade class responsible for pronunciation
    """

    def __init__(self):
        pass

    def say(self, target):
        """
        Pronounces all the audio files passed to this method
        :param target: files to be played
        :type target: Iterable
        """
        data, fs = sf.read(target, dtype='float32')
        sd.play(data, fs)
        status = sd.wait()
