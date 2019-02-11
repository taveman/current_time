from unittest import TestCase
from core.interfaces import PhraseMakerInterface, SpeakerInterface


class WrongPhraseClass(PhraseMakerInterface):

    def __init__(self):
        super().__init__()


class WrongSpeakerClass(SpeakerInterface):

    def __int__(self):
        super().__init__()


class InterfaceTest(TestCase):

    def setUp(self):
        self.phrase_maker_interface = WrongPhraseClass()
        self.speaker_interface = WrongSpeakerClass()

    def test_phrase_maker_interface_fails_without_implementing(self):
        """
        Tests if the instantiated from PhraseMakerInterface class implements expected method
        """
        with self.assertRaises(NotImplementedError):
            self.phrase_maker_interface.build_the_phrase(None)

    def test_phrase_speaker_interface_fails_without_implementing(self):
        """
        Tests if the instantiated from SpeakerInterface class implements expected method
        """
        with self.assertRaises(NotImplementedError):
            self.speaker_interface.say(None)
