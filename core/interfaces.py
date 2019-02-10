
class SpeakerInterface:
    """
    Speaker interface all speakers classes should inherit from
    """
    def say(self, file_to_play):
        """
        Saying mechanism
        :param file_to_play: file to be played
        :type file_to_play: list
        """
        raise NotImplementedError()


class PhraseMakerInterface:
    """
    Interface for phrase making
    """
    def build_the_phrase(self, files_map):
        """
        Builds the phrase from the map
        :param files_map: map as a dictionary
        :type files_map: Any
        """
        raise NotImplementedError()
