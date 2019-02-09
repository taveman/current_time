
class SpeakerInterface:
    """
    Speaker interface all speakers classes should inherit from
    """

    def say(self, file_to_play):
        """
        Saying mechanism
        :param file_to_play: file to be played
        :type file_to_play: str
        """
        raise NotImplementedError()
